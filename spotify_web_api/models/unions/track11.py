from __future__ import annotations

from typing import TypeAlias

from ..episode_object import EpisodeObject, EpisodeObjectDict
from ..track_object import TrackObject, TrackObjectDict

Track11: TypeAlias = TrackObject | EpisodeObject
"""Information about the track or episode."""

Track11Dict: TypeAlias = TrackObjectDict | EpisodeObjectDict
