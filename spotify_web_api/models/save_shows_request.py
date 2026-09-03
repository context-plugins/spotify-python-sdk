from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaveShowsRequest(SdkBaseModel):
    ids: Optional[list[str]] = UNSET
    """A JSON array of the `Spotify IDs
    <https://developer.spotify.comhttps://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids>`__. A
    maximum of 50 items can be specified in one request. *Note: if the ``ids`` parameter is present in the query string,
    any IDs listed here in the body will be ignored.*"""


class SaveShowsRequestDict(TypedDict):
    ids: NotRequired[list[str]]
