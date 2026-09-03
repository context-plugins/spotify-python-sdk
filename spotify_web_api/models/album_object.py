from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .album_restriction_object import AlbumRestrictionObject, AlbumRestrictionObjectDict
from .copyright_object import CopyrightObject, CopyrightObjectDict
from .enums.album_type import AlbumTypeOrStr
from .enums.release_date_precision import ReleaseDatePrecisionOrStr
from .enums.type2 import Type2OrStr
from .external_id_object import ExternalIdObject, ExternalIdObjectDict
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .image_object import ImageObject, ImageObjectDict
from .paging_simplified_track_object import PagingSimplifiedTrackObject, PagingSimplifiedTrackObjectDict
from .simplified_artist_object import SimplifiedArtistObject, SimplifiedArtistObjectDict


class AlbumObject(SdkBaseModel):
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

    tracks: PagingSimplifiedTrackObject
    copyrights: list[CopyrightObject]
    """The copyright statements of the album."""

    external_ids: ExternalIdObject
    genres: list[str]
    """A list of the genres the album is associated with. If not yet classified, the array is empty."""

    label: Optional[str] = UNSET
    """The label associated with the album."""

    popularity: Optional[int] = UNSET
    """The popularity of the album. The value will be between 0 and 100, with 100 being the most popular."""


class AlbumObjectDict(TypedDict):
    album_type: AlbumTypeOrStr
    total_tracks: int
    available_markets: NotRequired[list[str]]
    external_urls: ExternalUrlObject | ExternalUrlObjectDict
    href: str
    id: str
    images: list[ImageObject | ImageObjectDict]
    name: str
    release_date: str
    release_date_precision: ReleaseDatePrecisionOrStr
    restrictions: NotRequired[AlbumRestrictionObject | AlbumRestrictionObjectDict]
    type_: Type2OrStr
    uri: str
    artists: list[SimplifiedArtistObject | SimplifiedArtistObjectDict]
    tracks: PagingSimplifiedTrackObject | PagingSimplifiedTrackObjectDict
    copyrights: list[CopyrightObject | CopyrightObjectDict]
    external_ids: ExternalIdObject | ExternalIdObjectDict
    genres: list[str]
    label: NotRequired[str]
    popularity: NotRequired[int]
