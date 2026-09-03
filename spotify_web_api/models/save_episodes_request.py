from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SaveEpisodesRequest(SdkBaseModel):
    ids: list[str]
    """A JSON array of the `Spotify IDs
    <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__. <br/>A maximum of 50 items can
    be specified in one request. _**Note**: if the ``ids`` parameter is present in the query string, any IDs listed here
    in the body will be ignored._"""


class SaveEpisodesRequestDict(TypedDict):
    ids: list[str]
