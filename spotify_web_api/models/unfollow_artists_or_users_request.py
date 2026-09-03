from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UnfollowArtistsOrUsersRequest(SdkBaseModel):
    ids: Optional[list[str]] = UNSET
    """A JSON array of the artist or user `Spotify IDs
    <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__. For example:
    ``{ids:["74ASZWbe4lXaubB36ztrGX", "08td7MxkoHQkXnWAYD8d6Q"]}``. A maximum of 50 IDs can be sent in one request.
    _**Note**: if the ``ids`` parameter is present in the query string, any IDs listed here in the body will be
    ignored._"""


class UnfollowArtistsOrUsersRequestDict(TypedDict):
    ids: NotRequired[list[str]]
