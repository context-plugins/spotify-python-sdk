from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PlaylistsTracksRequest(SdkBaseModel):
    uris: Optional[list[str]] = UNSET
    """A JSON array of the `Spotify URIs
    <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ to add. For example: ``{"uris":
    ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98MSxVHPZCA6M",
    "spotify:episode:512ojhOuo1ktJprKbVcKyQ"]}``<br/>A maximum of 100 items can be added in one request. _**Note**: if
    the ``uris`` parameter is present in the query string, any URIs listed here in the body will be ignored._"""

    position: Optional[int] = UNSET
    """The position to insert the items, a zero-based index. For example, to insert the items in the first position:
    ``position=0`` ; to insert the items in the third position: ``position=2``. If omitted, the items will be appended
    to the playlist. Items are added in the order they appear in the uris array. For example: ``{"uris":
    ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98MSxVHPZCA6M"], "position": 3}``"""


class PlaylistsTracksRequestDict(TypedDict):
    uris: NotRequired[list[str]]
    position: NotRequired[int]
