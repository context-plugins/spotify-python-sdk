from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .artist_object import ArtistObject, ArtistObjectDict
from .enums.type3 import Type3OrStr
from .external_id_object import ExternalIdObject, ExternalIdObjectDict
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .linked_track_object import LinkedTrackObject, LinkedTrackObjectDict
from .simplified_album_object import SimplifiedAlbumObject, SimplifiedAlbumObjectDict
from .track_restriction_object import TrackRestrictionObject, TrackRestrictionObjectDict


class TrackObject(SdkBaseModel):
    album: Optional[SimplifiedAlbumObject] = UNSET
    artists: Optional[list[ArtistObject]] = UNSET
    """The artists who performed the track. Each artist object includes a link in ``href`` to more detailed information
    about the artist."""

    available_markets: Optional[list[str]] = UNSET
    """A list of the countries in which the track can be played, identified by their `ISO 3166-1 alpha-2
    <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ code."""

    disc_number: Optional[int] = UNSET
    """The disc number (usually ``1`` unless the album consists of more than one disc)."""

    duration_ms: Optional[int] = UNSET
    """The track length in milliseconds."""

    explicit: Optional[bool] = UNSET
    """Whether or not the track has explicit lyrics ( ``true`` = yes it does; ``false`` = no it does not OR unknown)."""

    external_ids: Optional[ExternalIdObject] = UNSET
    external_urls: Optional[ExternalUrlObject] = UNSET
    href: Optional[str] = UNSET
    """A link to the Web API endpoint providing full details of the track."""

    id: Optional[str] = UNSET
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    track."""

    is_playable: Optional[bool] = UNSET
    """Part of the response when `Track Relinking
    <https://developer.spotify.com/documentation/web-api/concepts/track-relinking>`__ is applied. If ``true``, the track
    is playable in the given market. Otherwise ``false``."""

    linked_from: Optional[LinkedTrackObject] = UNSET
    restrictions: Optional[TrackRestrictionObject] = UNSET
    name: Optional[str] = UNSET
    """The name of the track."""

    popularity: Optional[int] = UNSET
    """The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.<br/>The
    popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by
    algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays
    are.<br/>Generally speaking, songs that are being played a lot now will have a higher popularity than songs that
    were played a lot in the past. Duplicate tracks (e.g. the same track from a single and an album) are rated
    independently. Artist and album popularity is derived mathematically from track popularity. _**Note**: the
    popularity value may lag actual popularity by a few days: the value is not updated in real time._"""

    preview_url: OptionalNullable[str] = UNSET
    """A link to a 30 second preview (MP3 format) of the track. Can be ``null``"""

    track_number: Optional[int] = UNSET
    """The number of the track. If an album has several discs, the track number is the number on the specified disc."""

    type_: Optional[Type3OrStr] = Field(default=UNSET, alias="type")
    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    track."""

    is_local: Optional[bool] = UNSET
    """Whether or not the track is from a local file."""


class TrackObjectDict(TypedDict):
    album: NotRequired[SimplifiedAlbumObject | SimplifiedAlbumObjectDict]
    artists: NotRequired[list[ArtistObject | ArtistObjectDict]]
    available_markets: NotRequired[list[str]]
    disc_number: NotRequired[int]
    duration_ms: NotRequired[int]
    explicit: NotRequired[bool]
    external_ids: NotRequired[ExternalIdObject | ExternalIdObjectDict]
    external_urls: NotRequired[ExternalUrlObject | ExternalUrlObjectDict]
    href: NotRequired[str]
    id: NotRequired[str]
    is_playable: NotRequired[bool]
    linked_from: NotRequired[LinkedTrackObject | LinkedTrackObjectDict]
    restrictions: NotRequired[TrackRestrictionObject | TrackRestrictionObjectDict]
    name: NotRequired[str]
    popularity: NotRequired[int]
    preview_url: NotRequired[str | None]
    track_number: NotRequired[int]
    type_: NotRequired[Type3OrStr]
    uri: NotRequired[str]
    is_local: NotRequired[bool]
