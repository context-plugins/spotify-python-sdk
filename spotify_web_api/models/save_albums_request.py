from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaveAlbumsRequest(SdkBaseModel):
    ids: Optional[list[str]] = UNSET
    """A JSON array of the `Spotify IDs
    <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__. For example:
    ``["4iV5W9uYEdYUVa79Axb7Rh", "1301WleyT98MSxVHPZCA6M"]``<br/>A maximum of 50 items can be specified in one request.
    _**Note**: if the ``ids`` parameter is present in the query string, any IDs listed here in the body will be
    ignored._"""


class SaveAlbumsRequestDict(TypedDict):
    ids: NotRequired[list[str]]
