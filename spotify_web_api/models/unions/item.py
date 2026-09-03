from __future__ import annotations

from typing import TypeAlias

from ..episode_object import EpisodeObject, EpisodeObjectDict
from ..track_object import TrackObject, TrackObjectDict

Item: TypeAlias = TrackObject | EpisodeObject
"""The currently playing track or episode. Can be ``null``."""

ItemDict: TypeAlias = TrackObjectDict | EpisodeObjectDict
