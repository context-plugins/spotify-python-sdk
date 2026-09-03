from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .audiobook_base import AudiobookBase, AudiobookBaseDict
from .chapter_restriction_object import ChapterRestrictionObject, ChapterRestrictionObjectDict
from .enums.release_date_precision import ReleaseDatePrecisionOrStr
from .enums.type5 import Type5OrStr
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .image_object import ImageObject, ImageObjectDict
from .resume_point_object import ResumePointObject, ResumePointObjectDict


class ChapterObject(SdkBaseModel):
    audio_preview_url: str | None
    """A URL to a 30 second preview (MP3 format) of the chapter. ``null`` if not available."""

    available_markets: Optional[list[str]] = UNSET
    """A list of the countries in which the chapter can be played, identified by their `ISO 3166-1 alpha-2
    <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ code."""

    chapter_number: int
    """The number of the chapter"""

    description: str
    """A description of the chapter. HTML tags are stripped away from this field, use ``html_description`` field in case
    HTML tags are needed."""

    html_description: str
    """A description of the chapter. This field may contain HTML tags."""

    duration_ms: int
    """The chapter length in milliseconds."""

    explicit: bool
    """Whether or not the chapter has explicit content (true = yes it does; false = no it does not OR unknown)."""

    external_urls: ExternalUrlObject
    href: str
    """A link to the Web API endpoint providing full details of the chapter."""

    id: str
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    chapter."""

    images: list[ImageObject]
    """The cover art for the chapter in various sizes, widest first."""

    is_playable: bool
    """True if the chapter is playable in the given market. Otherwise false."""

    languages: list[str]
    """A list of the languages used in the chapter, identified by their `ISO 639-1
    <https://en.wikipedia.org/wiki/ISO_639>`__ code."""

    name: str
    """The name of the chapter."""

    release_date: str
    """The date the chapter was first released, for example ``"1981-12-15"``. Depending on the precision, it might be
    shown as ``"1981"`` or ``"1981-12"``."""

    release_date_precision: ReleaseDatePrecisionOrStr
    resume_point: Optional[ResumePointObject] = UNSET
    type_: Type5OrStr = Field(alias="type")
    uri: str
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    chapter."""

    restrictions: Optional[ChapterRestrictionObject] = UNSET
    audiobook: AudiobookBase


class ChapterObjectDict(TypedDict):
    audio_preview_url: str | None
    available_markets: NotRequired[list[str]]
    chapter_number: int
    description: str
    html_description: str
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrlObject | ExternalUrlObjectDict
    href: str
    id: str
    images: list[ImageObject | ImageObjectDict]
    is_playable: bool
    languages: list[str]
    name: str
    release_date: str
    release_date_precision: ReleaseDatePrecisionOrStr
    resume_point: NotRequired[ResumePointObject | ResumePointObjectDict]
    type_: Type5OrStr
    uri: str
    restrictions: NotRequired[ChapterRestrictionObject | ChapterRestrictionObjectDict]
    audiobook: AudiobookBase | AudiobookBaseDict
