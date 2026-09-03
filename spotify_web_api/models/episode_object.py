from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.release_date_precision import ReleaseDatePrecisionOrStr
from .enums.type5 import Type5OrStr
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .image_object import ImageObject, ImageObjectDict
from .resume_point_object import ResumePointObject, ResumePointObjectDict
from .show_base import ShowBase, ShowBaseDict
from .track_restriction_object import TrackRestrictionObject, TrackRestrictionObjectDict


class EpisodeObject(SdkBaseModel):
    audio_preview_url: str | None
    """A URL to a 30 second preview (MP3 format) of the episode. ``null`` if not available."""

    description: str
    """A description of the episode. HTML tags are stripped away from this field, use ``html_description`` field in case
    HTML tags are needed."""

    html_description: str
    """A description of the episode. This field may contain HTML tags."""

    duration_ms: int
    """The episode length in milliseconds."""

    explicit: bool
    """Whether or not the episode has explicit content (true = yes it does; false = no it does not OR unknown)."""

    external_urls: ExternalUrlObject
    href: str
    """A link to the Web API endpoint providing full details of the episode."""

    id: str
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    episode."""

    images: list[ImageObject]
    """The cover art for the episode in various sizes, widest first."""

    is_externally_hosted: bool
    """True if the episode is hosted outside of Spotify's CDN."""

    is_playable: bool
    """True if the episode is playable in the given market. Otherwise false."""

    language: Optional[str] = UNSET
    """The language used in the episode, identified by a `ISO 639 <https://en.wikipedia.org/wiki/ISO_639>`__ code. This
    field is deprecated and might be removed in the future. Please use the ``languages`` field instead."""

    languages: list[str]
    """A list of the languages used in the episode, identified by their `ISO 639-1
    <https://en.wikipedia.org/wiki/ISO_639>`__ code."""

    name: str
    """The name of the episode."""

    release_date: str
    """The date the episode was first released, for example ``"1981-12-15"``. Depending on the precision, it might be
    shown as ``"1981"`` or ``"1981-12"``."""

    release_date_precision: ReleaseDatePrecisionOrStr
    resume_point: Optional[ResumePointObject] = UNSET
    type_: Type5OrStr = Field(alias="type")
    uri: str
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    episode."""

    restrictions: Optional[TrackRestrictionObject] = UNSET
    show: ShowBase


class EpisodeObjectDict(TypedDict):
    audio_preview_url: str | None
    description: str
    html_description: str
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrlObject | ExternalUrlObjectDict
    href: str
    id: str
    images: list[ImageObject | ImageObjectDict]
    is_externally_hosted: bool
    is_playable: bool
    language: NotRequired[str]
    languages: list[str]
    name: str
    release_date: str
    release_date_precision: ReleaseDatePrecisionOrStr
    resume_point: NotRequired[ResumePointObject | ResumePointObjectDict]
    type_: Type5OrStr
    uri: str
    restrictions: NotRequired[TrackRestrictionObject | TrackRestrictionObjectDict]
    show: ShowBase | ShowBaseDict
