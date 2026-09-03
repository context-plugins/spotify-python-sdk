from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .context_object import ContextObject, ContextObjectDict
from .track_object import TrackObject, TrackObjectDict


class PlayHistoryObject(SdkBaseModel):
    track: Optional[TrackObject] = UNSET
    played_at: Optional[RFC3339DateTime] = UNSET
    """The date and time the track was played."""

    context: Optional[ContextObject] = UNSET


class PlayHistoryObjectDict(TypedDict):
    track: NotRequired[TrackObject | TrackObjectDict]
    played_at: NotRequired[RFC3339DateTime]
    context: NotRequired[ContextObject | ContextObjectDict]
