from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .paging_playlist_object import PagingPlaylistObject, PagingPlaylistObjectDict


class PagingFeaturedPlaylistObject(SdkBaseModel):
    message: Optional[str] = UNSET
    """The localized message of a playlist."""

    playlists: Optional[PagingPlaylistObject] = UNSET


class PagingFeaturedPlaylistObjectDict(TypedDict):
    message: NotRequired[str]
    playlists: NotRequired[PagingPlaylistObject | PagingPlaylistObjectDict]
