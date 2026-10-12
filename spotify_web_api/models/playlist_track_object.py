from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .playlist_user_object import PlaylistUserObject, PlaylistUserObjectDict
from .unions.track11 import Track11, Track11Dict


class PlaylistTrackObject(SdkBaseModel):
    added_at: Optional[RFC3339DateTime] = UNSET
    """The date and time the track or episode was added. _**Note**: some very old playlists may return ``null`` in this
    field._"""

    added_by: Optional[PlaylistUserObject] = UNSET
    is_local: Optional[bool] = UNSET
    """Whether this track or episode is a `local file
    <https://developer.spotify.com/documentation/web-api/concepts/playlists/#local-files>`__ or not."""

    track: Optional[Track11] = UNSET
    """Information about the track or episode."""


class PlaylistTrackObjectDict(TypedDict):
    added_at: NotRequired[RFC3339DateTime]
    added_by: NotRequired[PlaylistUserObjectDict]
    is_local: NotRequired[bool]
    track: NotRequired[Track11Dict]
