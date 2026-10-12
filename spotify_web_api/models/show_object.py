from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .copyright_object import CopyrightObject, CopyrightObjectDict
from .enums.type6 import Type6OrStr
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .image_object import ImageObject, ImageObjectDict
from .paging_simplified_episode_object import PagingSimplifiedEpisodeObject, PagingSimplifiedEpisodeObjectDict


class ShowObject(SdkBaseModel):
    available_markets: list[str]
    """A list of the countries in which the show can be played, identified by their `ISO 3166-1 alpha-2
    <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ code."""

    copyrights: list[CopyrightObject]
    """The copyright statements of the show."""

    description: str
    """A description of the show. HTML tags are stripped away from this field, use ``html_description`` field in case
    HTML tags are needed."""

    html_description: str
    """A description of the show. This field may contain HTML tags."""

    explicit: bool
    """Whether or not the show has explicit content (true = yes it does; false = no it does not OR unknown)."""

    external_urls: ExternalUrlObject
    href: str
    """A link to the Web API endpoint providing full details of the show."""

    id: str
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    show."""

    images: list[ImageObject]
    """The cover art for the show in various sizes, widest first."""

    is_externally_hosted: bool
    """True if all of the shows episodes are hosted outside of Spotify's CDN. This field might be ``null`` in some
    cases."""

    languages: list[str]
    """A list of the languages used in the show, identified by their `ISO 639 <https://en.wikipedia.org/wiki/ISO_639>`__
    code."""

    media_type: str
    """The media type of the show."""

    name: str
    """The name of the episode."""

    publisher: str
    """The publisher of the show."""

    type_: Type6OrStr = Field(alias="type")
    uri: str
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    show."""

    total_episodes: int
    """The total number of episodes in the show."""

    episodes: PagingSimplifiedEpisodeObject


class ShowObjectDict(TypedDict):
    available_markets: list[str]
    copyrights: list[CopyrightObjectDict]
    description: str
    html_description: str
    explicit: bool
    external_urls: ExternalUrlObjectDict
    href: str
    id: str
    images: list[ImageObjectDict]
    is_externally_hosted: bool
    languages: list[str]
    media_type: str
    name: str
    publisher: str
    type_: Type6OrStr
    uri: str
    total_episodes: int
    episodes: PagingSimplifiedEpisodeObjectDict
