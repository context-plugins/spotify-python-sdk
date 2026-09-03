from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.type4 import Type4OrStr
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .followers_object import FollowersObject, FollowersObjectDict


class PlaylistOwnerObject(SdkBaseModel):
    external_urls: Optional[ExternalUrlObject] = UNSET
    followers: Optional[FollowersObject] = UNSET
    href: Optional[str] = UNSET
    """A link to the Web API endpoint for this user."""

    id: Optional[str] = UNSET
    """The `Spotify user ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for this
    user."""

    type_: Optional[Type4OrStr] = Field(default=UNSET, alias="type")
    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for this
    user."""

    display_name: OptionalNullable[str] = UNSET
    """The name displayed on the user's profile. ``null`` if not available."""


class PlaylistOwnerObjectDict(TypedDict):
    external_urls: NotRequired[ExternalUrlObject | ExternalUrlObjectDict]
    followers: NotRequired[FollowersObject | FollowersObjectDict]
    href: NotRequired[str]
    id: NotRequired[str]
    type_: NotRequired[Type4OrStr]
    uri: NotRequired[str]
    display_name: NotRequired[str | None]
