from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .linked_track_object import LinkedTrackObject, LinkedTrackObjectDict
from .simplified_artist_object import SimplifiedArtistObject, SimplifiedArtistObjectDict
from .track_restriction_object import TrackRestrictionObject, TrackRestrictionObjectDict


class SimplifiedTrackObject(SdkBaseModel):
    artists: Optional[list[SimplifiedArtistObject]] = UNSET
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

    external_urls: Optional[ExternalUrlObject] = UNSET
    href: Optional[str] = UNSET
    """A link to the Web API endpoint providing full details of the track."""

    id: Optional[str] = UNSET
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    track."""

    is_playable: Optional[bool] = UNSET
    """Part of the response when `Track Relinking
    <https://developer.spotify.com/documentation/web-api/concepts/track-relinking/>`__ is applied. If ``true``, the
    track is playable in the given market. Otherwise ``false``."""

    linked_from: Optional[LinkedTrackObject] = UNSET
    restrictions: Optional[TrackRestrictionObject] = UNSET
    name: Optional[str] = UNSET
    """The name of the track."""

    preview_url: OptionalNullable[str] = UNSET
    """A URL to a 30 second preview (MP3 format) of the track."""

    track_number: Optional[int] = UNSET
    """The number of the track. If an album has several discs, the track number is the number on the specified disc."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The object type: "track"."""

    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    track."""

    is_local: Optional[bool] = UNSET
    """Whether or not the track is from a local file."""


class SimplifiedTrackObjectDict(TypedDict):
    artists: NotRequired[list[SimplifiedArtistObjectDict]]
    available_markets: NotRequired[list[str]]
    disc_number: NotRequired[int]
    duration_ms: NotRequired[int]
    explicit: NotRequired[bool]
    external_urls: NotRequired[ExternalUrlObjectDict]
    href: NotRequired[str]
    id: NotRequired[str]
    is_playable: NotRequired[bool]
    linked_from: NotRequired[LinkedTrackObjectDict]
    restrictions: NotRequired[TrackRestrictionObjectDict]
    name: NotRequired[str]
    preview_url: NotRequired[str | None]
    track_number: NotRequired[int]
    type_: NotRequired[str]
    uri: NotRequired[str]
    is_local: NotRequired[bool]
