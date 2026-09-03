from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExternalUrlObject(SdkBaseModel):
    spotify: Optional[str] = UNSET
    """The `Spotify URL <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    object."""


class ExternalUrlObjectDict(TypedDict):
    spotify: NotRequired[str]
