from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type import TypeOrStr
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict


class SimplifiedArtistObject(SdkBaseModel):
    external_urls: Optional[ExternalUrlObject] = UNSET
    href: Optional[str] = UNSET
    """A link to the Web API endpoint providing full details of the artist."""

    id: Optional[str] = UNSET
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    artist."""

    name: Optional[str] = UNSET
    """The name of the artist."""

    type_: Optional[TypeOrStr] = Field(default=UNSET, alias="type")
    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    artist."""


class SimplifiedArtistObjectDict(TypedDict):
    external_urls: NotRequired[ExternalUrlObject | ExternalUrlObjectDict]
    href: NotRequired[str]
    id: NotRequired[str]
    name: NotRequired[str]
    type_: NotRequired[TypeOrStr]
    uri: NotRequired[str]
