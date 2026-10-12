from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .section_object import SectionObject, SectionObjectDict
from .segment_object import SegmentObject, SegmentObjectDict
from .time_interval_object import TimeIntervalObject, TimeIntervalObjectDict
from .track import Track, TrackDict


class AudioAnalysisObject(SdkBaseModel):
    meta: Optional[Meta] = UNSET
    track: Optional[Track] = UNSET
    bars: Optional[list[TimeIntervalObject]] = UNSET
    """The time intervals of the bars throughout the track. A bar (or measure) is a segment of time defined as a given
    number of beats."""

    beats: Optional[list[TimeIntervalObject]] = UNSET
    """The time intervals of beats throughout the track. A beat is the basic time unit of a piece of music; for example,
    each tick of a metronome. Beats are typically multiples of tatums."""

    sections: Optional[list[SectionObject]] = UNSET
    """Sections are defined by large variations in rhythm or timbre, e.g. chorus, verse, bridge, guitar solo, etc. Each
    section contains its own descriptions of tempo, key, mode, time_signature, and loudness."""

    segments: Optional[list[SegmentObject]] = UNSET
    """Each segment contains a roughly conisistent sound throughout its duration."""

    tatums: Optional[list[TimeIntervalObject]] = UNSET
    """A tatum represents the lowest regular pulse train that a listener intuitively infers from the timing of perceived
    musical events (segments)."""


class AudioAnalysisObjectDict(TypedDict):
    meta: NotRequired[MetaDict]
    track: NotRequired[TrackDict]
    bars: NotRequired[list[TimeIntervalObjectDict]]
    beats: NotRequired[list[TimeIntervalObjectDict]]
    sections: NotRequired[list[SectionObjectDict]]
    segments: NotRequired[list[SegmentObjectDict]]
    tatums: NotRequired[list[TimeIntervalObjectDict]]
