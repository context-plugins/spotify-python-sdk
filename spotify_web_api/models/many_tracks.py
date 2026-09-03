from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .track_object import TrackObject, TrackObjectDict


class ManyTracks(SdkBaseModel):
    tracks: list[TrackObject]


class ManyTracksDict(TypedDict):
    tracks: list[TrackObject | TrackObjectDict]
