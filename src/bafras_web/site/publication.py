"""Elegibilidad de publicación por modo. Lee estados editoriales; nunca los cambia."""

from __future__ import annotations

from typing import Literal

from bafras_web.editorial.pages import PageContent

from .routes import SiteRouting

PublicationMode = Literal["preview", "release"]

# La salida pública (dist/, canonical, hreflang, sitemap, medios con crédito) no existe todavía:
# hasta entonces release se bloquea siempre, además de por los motivos de contenido.
RELEASE_NOT_AVAILABLE = "release aún no implementado: requiere cierre de publicación / G4"


def publication_blockers(page: PageContent, locale: str, routing: SiteRouting, mode: PublicationMode) -> list[str]:
    """Motivos que impiden generar `page` en `mode`. Preview admite borradores (revisión interna)."""
    if mode == "preview":
        return []
    blockers = [RELEASE_NOT_AVAILABLE]
    if locale not in routing.locales.published_codes:
        blockers.append(f"idioma {locale!r} no publicado (config/locales.yaml)")
    elif routing.url(page.page_id, locale) is None:
        blockers.append(f"sin URL pública para {page.page_id!r} en {locale!r}")
    if page.review.status != "approved":
        blockers.append(f"revisión editorial {page.review.status!r}, se requiere 'approved'")
    if page.seo.title is None or page.seo.description is None:
        blockers.append("SEO editorial incompleto (title/description nulos)")
    # D-W3 pendiente: mientras no se decida qué motivos son admisibles, todo pendiente bloquea.
    blockers.extend(f"pendiente {p.field} ({p.reason_code})" for p in page.pending)
    return blockers


def entity_publication_blockers(review_status: str, locale: str, routing: SiteRouting, mode: PublicationMode) -> list[str]:
    """Fichas de entidad: mismas reglas de idioma y revisión que las páginas. Preview admite borradores."""
    if mode == "preview":
        return []
    blockers = [RELEASE_NOT_AVAILABLE]
    if locale not in routing.locales.published_codes:
        blockers.append(f"idioma {locale!r} no publicado (config/locales.yaml)")
    if review_status != "approved":
        blockers.append(f"revisión editorial {review_status!r}, se requiere 'approved'")
    return blockers
