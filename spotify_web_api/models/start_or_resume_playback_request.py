from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StartOrResumePlaybackRequest(SdkBaseModel):
    context_uri: Optional[str] = UNSET
    """Optional. Spotify URI of the context to play. Valid contexts are albums, artists & playlists.
    ``{context_uri:"spotify:album:1Je1IMUlBXcx1Fz0WE7oPT"}``"""

    uris: Optional[list[str]] = UNSET
    """Optional. A JSON array of the Spotify track URIs to play. For example: ``{"uris":
    ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh", "spotify:track:1301WleyT98MSxVHPZCA6M"]}``"""

    offset: Optional[Any] = UNSET
    """Optional. Indicates from where in the context playback should start. Only available when context_uri corresponds
    to an album or playlist object "position" is zero based and can’t be negative. Example: ``"offset": {"position":
    5}`` "uri" is a string representing the uri of the item to start at. Example: ``"offset": {"uri":
    "spotify:track:1301WleyT98MSxVHPZCA6M"}``"""

    position_ms: Optional[int] = UNSET
    """Indicates from what position to start playback. Must be a positive number. Passing in a position that is greater
    than the length of the track will cause the player to start playing the next song."""


class StartOrResumePlaybackRequestDict(TypedDict):
    context_uri: NotRequired[str]
    uris: NotRequired[list[str]]
    offset: NotRequired[Any]
    position_ms: NotRequired[int]
