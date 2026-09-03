from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .artist_object import ArtistObject, ArtistObjectDict
from .cursor_object import CursorObject, CursorObjectDict


class CursorPagingSimplifiedArtistObject(SdkBaseModel):
    href: Optional[str] = UNSET
    """A link to the Web API endpoint returning the full result of the request."""

    limit: Optional[int] = UNSET
    """The maximum number of items in the response (as set in the query or by default)."""

    next: Optional[str] = UNSET
    """URL to the next page of items. ( ``null`` if none)"""

    cursors: Optional[CursorObject] = UNSET
    total: Optional[int] = UNSET
    """The total number of items available to return."""

    items: Optional[list[ArtistObject]] = UNSET


class CursorPagingSimplifiedArtistObjectDict(TypedDict):
    href: NotRequired[str]
    limit: NotRequired[int]
    next: NotRequired[str]
    cursors: NotRequired[CursorObject | CursorObjectDict]
    total: NotRequired[int]
    items: NotRequired[list[ArtistObject | ArtistObjectDict]]
