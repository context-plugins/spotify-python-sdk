from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .album_restriction_object import AlbumRestrictionObject, AlbumRestrictionObjectDict
from .enums.album_group import AlbumGroupOrStr
from .enums.album_type import AlbumTypeOrStr
from .enums.release_date_precision import ReleaseDatePrecisionOrStr
from .enums.type2 import Type2OrStr
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .image_object import ImageObject, ImageObjectDict
from .simplified_artist_object import SimplifiedArtistObject, SimplifiedArtistObjectDict


class ArtistDiscographyAlbumObject(SdkBaseModel):
    album_type: AlbumTypeOrStr
    total_tracks: int
    """The number of tracks in the album."""

    available_markets: Optional[list[str]] = UNSET
    """The markets in which the album is available: `ISO 3166-1 alpha-2 country codes
    <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__. _**NOTE**: an album is considered available in a market when
    at least 1 of its tracks is available in that market._"""

    external_urls: ExternalUrlObject
    href: str
    """A link to the Web API endpoint providing full details of the album."""

    id: str
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    album."""

    images: list[ImageObject]
    """The cover art for the album in various sizes, widest first."""

    name: str
    """The name of the album. In case of an album takedown, the value may be an empty string."""

    release_date: str
    """The date the album was first released."""

    release_date_precision: ReleaseDatePrecisionOrStr
    restrictions: Optional[AlbumRestrictionObject] = UNSET
    type_: Type2OrStr = Field(alias="type")
    uri: str
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    album."""

    artists: list[SimplifiedArtistObject]
    """The artists of the album. Each artist object includes a link in ``href`` to more detailed information about the
    artist."""

    album_group: Optional[AlbumGroupOrStr] = UNSET


class ArtistDiscographyAlbumObjectDict(TypedDict):
    album_type: AlbumTypeOrStr
    total_tracks: int
    available_markets: NotRequired[list[str]]
    external_urls: ExternalUrlObjectDict
    href: str
    id: str
    images: list[ImageObjectDict]
    name: str
    release_date: str
    release_date_precision: ReleaseDatePrecisionOrStr
    restrictions: NotRequired[AlbumRestrictionObjectDict]
    type_: Type2OrStr
    uri: str
    artists: list[SimplifiedArtistObjectDict]
    album_group: NotRequired[AlbumGroupOrStr]
