from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict


class ContextObject(SdkBaseModel):
    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The object type, e.g. "artist", "playlist", "album", "show"."""

    href: Optional[str] = UNSET
    """A link to the Web API endpoint providing full details of the track."""

    external_urls: Optional[ExternalUrlObject] = UNSET
    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    context."""


class ContextObjectDict(TypedDict):
    type_: NotRequired[str]
    href: NotRequired[str]
    external_urls: NotRequired[ExternalUrlObjectDict]
    uri: NotRequired[str]
