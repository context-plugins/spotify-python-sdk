from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type import TypeOrStr
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .followers_object import FollowersObject, FollowersObjectDict
from .image_object import ImageObject, ImageObjectDict


class ArtistObject(SdkBaseModel):
    external_urls: Optional[ExternalUrlObject] = UNSET
    followers: Optional[FollowersObject] = UNSET
    genres: Optional[list[str]] = UNSET
    """A list of the genres the artist is associated with. If not yet classified, the array is empty."""

    href: Optional[str] = UNSET
    """A link to the Web API endpoint providing full details of the artist."""

    id: Optional[str] = UNSET
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    artist."""

    images: Optional[list[ImageObject]] = UNSET
    """Images of the artist in various sizes, widest first."""

    name: Optional[str] = UNSET
    """The name of the artist."""

    popularity: Optional[int] = UNSET
    """The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's
    popularity is calculated from the popularity of all the artist's tracks."""

    type_: Optional[TypeOrStr] = Field(default=UNSET, alias="type")
    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    artist."""


class ArtistObjectDict(TypedDict):
    external_urls: NotRequired[ExternalUrlObjectDict]
    followers: NotRequired[FollowersObjectDict]
    genres: NotRequired[list[str]]
    href: NotRequired[str]
    id: NotRequired[str]
    images: NotRequired[list[ImageObjectDict]]
    name: NotRequired[str]
    popularity: NotRequired[int]
    type_: NotRequired[TypeOrStr]
    uri: NotRequired[str]
