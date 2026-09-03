from __future__ import annotations

from typing import TypeAlias

from ..episode_object import EpisodeObject, EpisodeObjectDict
from ..track_object import TrackObject, TrackObjectDict

Queue: TypeAlias = TrackObject | EpisodeObject

QueueDict: TypeAlias = TrackObjectDict | EpisodeObjectDict
