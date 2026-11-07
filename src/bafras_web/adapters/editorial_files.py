"""Bounded filesystem discovery; all YAML reading belongs to yaml_files."""

from pathlib import Path
from typing import Literal

from pydantic import model_validator

from bafras_web.editorial.inspection import RelativeSource
from bafras_web.editorial.primitives import EditorialModel


class EditorialSource(EditorialModel):
    source: RelativeSource
    path: Path | None = None
    error: Literal["access", "outside_locale", "not_file"] | None = None

    @model_validator(mode="after")
    def _readable_or_error(self) -> "EditorialSource":
        if (self.path is None) == (self.error is None):
            raise ValueError("source requires either a readable path or a discovery error")
        return self


def discover_editorial_sources(
    content_root: Path, locale: str, expected_sources: tuple[str, ...],
) -> tuple[EditorialSource, ...]:
    """Expected paths plus YAML candidates in exactly three directories.

    No atomic snapshot is promised. Validate again immediately before reading.
    """
    if not locale.isascii() or not locale.isalpha() or len(locale) != 2:
        raise ValueError("discovery requires a validated locale code")
    root = content_root.resolve()
    allowed = root / locale
    candidates = set(expected_sources)
    problems: dict[str, EditorialSource] = {}
    for directory in (allowed, allowed / "pages", allowed / "entities"):
        source = directory.relative_to(root).as_posix()
        try:
            if not directory.resolve().is_relative_to(allowed):
                problems[source] = EditorialSource(source=source, error="outside_locale")
                continue
            entries = tuple(directory.iterdir())
        except FileNotFoundError:
            continue
        except (OSError, RuntimeError):
            problems[source] = EditorialSource(source=source, error="access")
            continue
        for entry in entries:
            if entry.suffix.lower() in (".yaml", ".yml"):
                candidates.add(entry.relative_to(root).as_posix())
    for source in sorted(candidates):
        # RelativeSource validates the boundary even if the caller supplies paths.
        entry = EditorialSource(source=source, path=root / source)
        if not source.startswith(f"{locale}/"):
            raise ValueError("expected source outside requested locale")
        path = entry.path
        try:
            if not path.resolve().is_relative_to(allowed):
                problems[source] = EditorialSource(source=source, error="outside_locale")
            elif not path.is_file():
                if path.exists() or path.is_symlink():
                    problems[source] = EditorialSource(source=source, error="not_file")
            else:
                problems[source] = entry
        except (OSError, RuntimeError):
            problems[source] = EditorialSource(source=source, error="access")
    return tuple(problems[key] for key in sorted(problems))


def editorial_path_for_reading(content_root: Path, locale: str, source: EditorialSource) -> Path:
    """Recheck containment/type to narrow discovery/read races before the loader."""
    allowed = content_root.resolve() / locale
    if source.path is None or source.error:
        raise OSError("editorial source is not readable")
    if not source.path.resolve().is_relative_to(allowed) or not source.path.is_file():
        raise OSError("editorial source changed after discovery")
    return source.path
