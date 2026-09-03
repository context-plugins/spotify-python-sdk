from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .track1 import Track1, Track1Dict


class PlaylistsTracksRequest2(SdkBaseModel):
    tracks: list[Track1]
    """An array of objects containing `Spotify URIs
    <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ of the tracks or episodes to
    remove. For example: ``{ "tracks": [{ "uri": "spotify:track:4iV5W9uYEdYUVa79Axb7Rh" },{ "uri":
    "spotify:track:1301WleyT98MSxVHPZCA6M" }] }``. A maximum of 100 objects can be sent at once."""

    snapshot_id: Optional[str] = UNSET
    """The playlist's snapshot ID against which you want to make the changes. The API will validate that the specified
    items exist and in the specified positions and make the changes, even if more recent changes have been made to the
    playlist."""


class PlaylistsTracksRequest2Dict(TypedDict):
    tracks: list[Track1 | Track1Dict]
    snapshot_id: NotRequired[str]
