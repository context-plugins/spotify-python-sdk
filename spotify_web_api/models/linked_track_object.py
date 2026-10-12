from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict


class LinkedTrackObject(SdkBaseModel):
    external_urls: Optional[ExternalUrlObject] = UNSET
    href: Optional[str] = UNSET
    """A link to the Web API endpoint providing full details of the track."""

    id: Optional[str] = UNSET
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    track."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The object type: "track"."""

    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    track."""


class LinkedTrackObjectDict(TypedDict):
    external_urls: NotRequired[ExternalUrlObjectDict]
    href: NotRequired[str]
    id: NotRequired[str]
    type_: NotRequired[str]
    uri: NotRequired[str]
