from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .followers_object import FollowersObject, FollowersObjectDict
from .image_object import ImageObject, ImageObjectDict
from .paging_playlist_track_object import PagingPlaylistTrackObject, PagingPlaylistTrackObjectDict
from .playlist_owner_object import PlaylistOwnerObject, PlaylistOwnerObjectDict


class PlaylistObject(SdkBaseModel):
    collaborative: Optional[bool] = UNSET
    """``true`` if the owner allows other users to modify the playlist."""

    description: OptionalNullable[str] = UNSET
    """The playlist description. _Only returned for modified, verified playlists, otherwise_ ``null``."""

    external_urls: Optional[ExternalUrlObject] = UNSET
    followers: Optional[FollowersObject] = UNSET
    href: Optional[str] = UNSET
    """A link to the Web API endpoint providing full details of the playlist."""

    id: Optional[str] = UNSET
    """The `Spotify ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    playlist."""

    images: Optional[list[ImageObject]] = UNSET
    """Images for the playlist. The array may be empty or contain up to three images. The images are returned by size in
    descending order. See `Working with Playlists
    <https://developer.spotify.com/documentation/web-api/concepts/playlists>`__. _**Note**: If returned, the source URL
    for the image (``url``) is temporary and will expire in less than a day._"""

    name: Optional[str] = UNSET
    """The name of the playlist."""

    owner: Optional[PlaylistOwnerObject] = UNSET
    public: Optional[bool] = UNSET
    """The playlist's public/private status: ``true`` the playlist is public, ``false`` the playlist is private,
    ``null`` the playlist status is not relevant. For more about public/private status, see `Working with Playlists
    <https://developer.spotify.com/documentation/web-api/concepts/playlists>`__"""

    snapshot_id: Optional[str] = UNSET
    """The version identifier for the current playlist. Can be supplied in other requests to target a specific playlist
    version"""

    tracks: Optional[PagingPlaylistTrackObject] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The object type: "playlist"
    """

    uri: Optional[str] = UNSET
    """The `Spotify URI <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ for the
    playlist."""


class PlaylistObjectDict(TypedDict):
    collaborative: NotRequired[bool]
    description: NotRequired[str | None]
    external_urls: NotRequired[ExternalUrlObjectDict]
    followers: NotRequired[FollowersObjectDict]
    href: NotRequired[str]
    id: NotRequired[str]
    images: NotRequired[list[ImageObjectDict]]
    name: NotRequired[str]
    owner: NotRequired[PlaylistOwnerObjectDict]
    public: NotRequired[bool]
    snapshot_id: NotRequired[str]
    tracks: NotRequired[PagingPlaylistTrackObjectDict]
    type_: NotRequired[str]
    uri: NotRequired[str]
