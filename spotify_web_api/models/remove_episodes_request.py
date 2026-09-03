from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RemoveEpisodesRequest(SdkBaseModel):
    ids: Optional[list[str]] = UNSET
    """A JSON array of the `Spotify IDs
    <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__. <br/>A maximum of 50 items can
    be specified in one request. _**Note**: if the ``ids`` parameter is present in the query string, any IDs listed here
    in the body will be ignored._"""


class RemoveEpisodesRequestDict(TypedDict):
    ids: NotRequired[list[str]]
