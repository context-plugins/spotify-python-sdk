from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .author_object import AuthorObject, AuthorObjectDict
from .copyright_object import CopyrightObject, CopyrightObjectDict
from .enums.type9 import Type9OrStr
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .image_object import ImageObject, ImageObjectDict
from .narrator_object import NarratorObject, NarratorObjectDict
from .paging_simplified_chapter_object import PagingSimplifiedChapterObject, PagingSimplifiedChapterObjectDict


class AudiobookObject(SdkBaseModel):
    authors: list[AuthorObject]
    """The author(s) for the audiobook."""

    available_markets: list[str]
    """A list of the countries in which the audiobook can be played, identified by their `ISO 3166-1 alpha-2
    <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ code."""

    copyrights: list[CopyrightObject]
    """The copyright statements of the audiobook."""

    description: str
    """A description of the audiobook. HTML tags are stripped away from this field, use ``html_description`` field in
    case HTML tags are needed."""

    html_description: str
    """A description of the audiobook. This field may contain HTML tags."""

    edition: Optional[str] = UNSET
    """The edition of the audiobook."""

    explicit: bool
    """Whether or not the audiobook has explicit content (true = yes it does; false = no it does not OR unknown)."""

    external_urls: ExternalUrlObject
    href: str
    """A link to the Web API endpoint providing full details of the audiobook."""

    id: str
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    audiobook."""

    images: list[ImageObject]
    """The cover art for the audiobook in various sizes, widest first."""

    languages: list[str]
    """A list of the languages used in the audiobook, identified by their `ISO 639
    <https://en.wikipedia.org/wiki/ISO_639>`__ code."""

    media_type: str
    """The media type of the audiobook."""

    name: str
    """The name of the audiobook."""

    narrators: list[NarratorObject]
    """The narrator(s) for the audiobook."""

    publisher: str
    """The publisher of the audiobook."""

    type_: Type9OrStr = Field(alias="type")
    uri: str
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    audiobook."""

    total_chapters: int
    """The number of chapters in this audiobook."""

    chapters: PagingSimplifiedChapterObject


class AudiobookObjectDict(TypedDict):
    authors: list[AuthorObjectDict]
    available_markets: list[str]
    copyrights: list[CopyrightObjectDict]
    description: str
    html_description: str
    edition: NotRequired[str]
    explicit: bool
    external_urls: ExternalUrlObjectDict
    href: str
    id: str
    images: list[ImageObjectDict]
    languages: list[str]
    media_type: str
    name: str
    narrators: list[NarratorObjectDict]
    publisher: str
    type_: Type9OrStr
    uri: str
    total_chapters: int
    chapters: PagingSimplifiedChapterObjectDict
