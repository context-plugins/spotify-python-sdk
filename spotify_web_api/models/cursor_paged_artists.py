from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cursor_paging_simplified_artist_object import (
    CursorPagingSimplifiedArtistObject,
    CursorPagingSimplifiedArtistObjectDict,
)


class CursorPagedArtists(SdkBaseModel):
    artists: CursorPagingSimplifiedArtistObject


class CursorPagedArtistsDict(TypedDict):
    artists: CursorPagingSimplifiedArtistObjectDict
