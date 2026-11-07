"""Inspección de HTML/recursos físicos; no decide contenido ni construye URLs editoriales."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class SiteIntegrityError(ValueError):
    def __init__(self, problems: list[str]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


class HtmlDocument(HTMLParser):
    def __init__(self, source: str) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.duplicates: list[str] = []
        self.references: list[tuple[str, bool]] = []
        self.h1_count = 0
        self.feed(source)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        identity = data.get("id")
        if identity:
            if identity in self.ids:
                self.duplicates.append(identity)
            self.ids.add(identity)
        self.h1_count += tag == "h1"
        for key in ("href", "src", "action", "poster"):
            if key in data:
                self.references.append((data[key] or "", tag == "a" and key == "href"))


def validate_site_tree(root: Path, *, allowed_missing_pages: set[str | None] | None = None) -> None:
    """Comprobar destinos reales, fragmentos, IDs y h1. No realiza peticiones de red.

    Un build individual permite únicamente páginas conocidas de SITE fuera de su selección.
    Un build completo no admite destinos ausentes.
    """
    root = root.resolve()
    documents = {p.resolve(): HtmlDocument(p.read_text(encoding="utf-8")) for p in sorted(root.rglob("*.html"))}
    problems = []
    allowed = allowed_missing_pages or set()
    for path, doc in documents.items():
        relative = path.relative_to(root).as_posix()
        if doc.h1_count != 1:
            problems.append(f"{relative}: se requiere un h1, encontrados {doc.h1_count}")
        problems.extend(f"{relative}: id duplicado {identity}" for identity in doc.duplicates)
        for reference, is_link in doc.references:
            if not reference or reference == "#":
                problems.append(f"{relative}: destino vacío {reference!r}")
                continue
            url = urlsplit(urljoin("/" + relative, reference))
            if url.scheme or url.netloc:
                if url.scheme and url.scheme not in ("https", "http", "mailto", "tel"):
                    problems.append(f"{relative}: esquema no admitido {reference!r}")
                continue
            decoded = unquote(url.path)
            target = (root / decoded.lstrip("/")).resolve()
            if not target.is_relative_to(root):
                problems.append(f"{relative}: destino fuera de salida {reference!r}")
                continue
            if decoded.endswith("/") or target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                if not (is_link and url.path in allowed):
                    problems.append(f"{relative}: destino inexistente {reference!r}")
            elif url.fragment and (target not in documents or unquote(url.fragment) not in documents[target].ids):
                problems.append(f"{relative}: fragmento inexistente {reference!r}")
    if not documents:
        problems.append("sitio sin HTML")
    if problems:
        raise SiteIntegrityError(problems)
