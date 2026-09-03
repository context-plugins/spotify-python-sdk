from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .paging_artist_object import PagingArtistObject, PagingArtistObjectDict
from .paging_playlist_object import PagingPlaylistObject, PagingPlaylistObjectDict
from .paging_simplified_album_object import PagingSimplifiedAlbumObject, PagingSimplifiedAlbumObjectDict
from .paging_simplified_audiobook_object import PagingSimplifiedAudiobookObject, PagingSimplifiedAudiobookObjectDict
from .paging_simplified_episode_object import PagingSimplifiedEpisodeObject, PagingSimplifiedEpisodeObjectDict
from .paging_simplified_show_object import PagingSimplifiedShowObject, PagingSimplifiedShowObjectDict
from .paging_track_object import PagingTrackObject, PagingTrackObjectDict


class SearchItems(SdkBaseModel):
    tracks: Optional[PagingTrackObject] = UNSET
    artists: Optional[PagingArtistObject] = UNSET
    albums: Optional[PagingSimplifiedAlbumObject] = UNSET
    playlists: Optional[PagingPlaylistObject] = UNSET
    shows: Optional[PagingSimplifiedShowObject] = UNSET
    episodes: Optional[PagingSimplifiedEpisodeObject] = UNSET
    audiobooks: Optional[PagingSimplifiedAudiobookObject] = UNSET


class SearchItemsDict(TypedDict):
    tracks: NotRequired[PagingTrackObject | PagingTrackObjectDict]
    artists: NotRequired[PagingArtistObject | PagingArtistObjectDict]
    albums: NotRequired[PagingSimplifiedAlbumObject | PagingSimplifiedAlbumObjectDict]
    playlists: NotRequired[PagingPlaylistObject | PagingPlaylistObjectDict]
    shows: NotRequired[PagingSimplifiedShowObject | PagingSimplifiedShowObjectDict]
    episodes: NotRequired[PagingSimplifiedEpisodeObject | PagingSimplifiedEpisodeObjectDict]
    audiobooks: NotRequired[PagingSimplifiedAudiobookObject | PagingSimplifiedAudiobookObjectDict]
