from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersPlaylistsRequest(SdkBaseModel):
    name: str
    """The name for the new playlist, for example ``"Your Coolest Playlist"``. This name does not need to be unique; a
    user may have several playlists with the same name."""

    public: Optional[bool] = UNSET
    """Defaults to ``true``. If ``true`` the playlist will be public, if ``false`` it will be private. To be able to
    create private playlists, the user must have granted the ``playlist-modify-private`` `scope
    <https://developer.spotify.com/documentation/web-api/concepts/scopes/#list-of-scopes>`__"""

    collaborative: Optional[bool] = UNSET
    """Defaults to ``false``. If ``true`` the playlist will be collaborative. _**Note**: to create a collaborative
    playlist you must also set ``public`` to ``false``. To create collaborative playlists you must have granted
    ``playlist-modify-private`` and ``playlist-modify-public`` `scopes
    <https://developer.spotify.com/documentation/web-api/concepts/scopes/#list-of-scopes>`__._"""

    description: Optional[str] = UNSET
    """value for playlist description as displayed in Spotify Clients and in the Web API."""


class UsersPlaylistsRequestDict(TypedDict):
    name: str
    public: NotRequired[bool]
    collaborative: NotRequired[bool]
    description: NotRequired[str]
