from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .saved_album_object import SavedAlbumObject, SavedAlbumObjectDict


class PagingSavedAlbumObject(SdkBaseModel):
    href: str
    """A link to the Web API endpoint returning the full result of the request"""

    limit: int
    """The maximum number of items in the response (as set in the query or by default)."""

    next: str | None
    """URL to the next page of items. ( ``null`` if none)"""

    offset: int
    """The offset of the items returned (as set in the query or by default)"""

    previous: str | None
    """URL to the previous page of items. ( ``null`` if none)"""

    total: int
    """The total number of items available to return."""

    items: list[SavedAlbumObject]


class PagingSavedAlbumObjectDict(TypedDict):
    href: str
    limit: int
    next: str | None
    offset: int
    previous: str | None
    total: int
    items: list[SavedAlbumObjectDict]
