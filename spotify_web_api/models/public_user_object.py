from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.type4 import Type4OrStr
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .followers_object import FollowersObject, FollowersObjectDict
from .image_object import ImageObject, ImageObjectDict


class PublicUserObject(SdkBaseModel):
    display_name: OptionalNullable[str] = UNSET
    """The name displayed on the user's profile. ``null`` if not available."""

    external_urls: Optional[ExternalUrlObject] = UNSET
    followers: Optional[FollowersObject] = UNSET
    href: Optional[str] = UNSET
    """A link to the Web API endpoint for this user."""

    id: Optional[str] = UNSET
    """The `Spotify user ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for this
    user."""

    images: Optional[list[ImageObject]] = UNSET
    """The user's profile image."""

    type_: Optional[Type4OrStr] = Field(default=UNSET, alias="type")
    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for this
    user."""


class PublicUserObjectDict(TypedDict):
    display_name: NotRequired[str | None]
    external_urls: NotRequired[ExternalUrlObjectDict]
    followers: NotRequired[FollowersObjectDict]
    href: NotRequired[str]
    id: NotRequired[str]
    images: NotRequired[list[ImageObjectDict]]
    type_: NotRequired[Type4OrStr]
    uri: NotRequired[str]
