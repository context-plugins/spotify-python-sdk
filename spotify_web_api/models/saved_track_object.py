from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .track_object import TrackObject, TrackObjectDict


class SavedTrackObject(SdkBaseModel):
    added_at: Optional[RFC3339DateTime] = UNSET
    """The date and time the track was saved. Timestamps are returned in ISO 8601 format as Coordinated Universal Time
    (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ. If the time is imprecise (for example, the date/time of an album
    release), an additional field indicates the precision; see for example, release_date in an album object."""

    track: Optional[TrackObject] = UNSET


class SavedTrackObjectDict(TypedDict):
    added_at: NotRequired[RFC3339DateTime]
    track: NotRequired[TrackObject | TrackObjectDict]
