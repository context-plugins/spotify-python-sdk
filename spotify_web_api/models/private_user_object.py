from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .explicit_content_settings_object import ExplicitContentSettingsObject, ExplicitContentSettingsObjectDict
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .followers_object import FollowersObject, FollowersObjectDict
from .image_object import ImageObject, ImageObjectDict


class PrivateUserObject(SdkBaseModel):
    country: Optional[str] = UNSET
    """The country of the user, as set in the user's account profile. An `ISO 3166-1 alpha-2 country code
    <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__. _This field is only available when the current user has
    granted access to the `user-read-private
    <https://developer.spotify.com/documentation/web-api/concepts/scopes/#list-of-scopes>`__ scope._"""

    display_name: Optional[str] = UNSET
    """The name displayed on the user's profile. ``null`` if not available."""

    email: Optional[str] = UNSET
    """The user's email address, as entered by the user when creating their account. _**Important!** This email address
    is unverified; there is no proof that it actually belongs to the user._ _This field is only available when the
    current user has granted access to the `user-read-email
    <https://developer.spotify.com/documentation/web-api/concepts/scopes/#list-of-scopes>`__ scope._"""

    explicit_content: Optional[ExplicitContentSettingsObject] = UNSET
    external_urls: Optional[ExternalUrlObject] = UNSET
    followers: Optional[FollowersObject] = UNSET
    href: Optional[str] = UNSET
    """A link to the Web API endpoint for this user."""

    id: Optional[str] = UNSET
    """The `Spotify user ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    user."""

    images: Optional[list[ImageObject]] = UNSET
    """The user's profile image."""

    product: Optional[str] = UNSET
    """The user's Spotify subscription level: "premium", "free", etc. (The subscription level "open" can be considered
    the same as "free".) _This field is only available when the current user has granted access to the
    `user-read-private <https://developer.spotify.com/documentation/web-api/concepts/scopes/#list-of-scopes>`__
    scope._"""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The object type: "user"
    """

    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    user."""


class PrivateUserObjectDict(TypedDict):
    country: NotRequired[str]
    display_name: NotRequired[str]
    email: NotRequired[str]
    explicit_content: NotRequired[ExplicitContentSettingsObjectDict]
    external_urls: NotRequired[ExternalUrlObjectDict]
    followers: NotRequired[FollowersObjectDict]
    href: NotRequired[str]
    id: NotRequired[str]
    images: NotRequired[list[ImageObjectDict]]
    product: NotRequired[str]
    type_: NotRequired[str]
    uri: NotRequired[str]
