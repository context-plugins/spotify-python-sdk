from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PlaylistsRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """The new name for the playlist, for example ``"My New Playlist Title"``"""

    public: Optional[bool] = UNSET
    """If ``true`` the playlist will be public, if ``false`` it will be private."""

    collaborative: Optional[bool] = UNSET
    """If ``true``, the playlist will become collaborative and other users will be able to modify the playlist in their
    Spotify client. <br/> _**Note**: You can only set ``collaborative`` to ``true`` on non-public playlists._"""

    description: Optional[str] = UNSET
    """Value for playlist description as displayed in Spotify Clients and in the Web API."""


class PlaylistsRequestDict(TypedDict):
    name: NotRequired[str]
    public: NotRequired[bool]
    collaborative: NotRequired[bool]
    description: NotRequired[str]
