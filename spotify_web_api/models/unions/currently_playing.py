from __future__ import annotations

from typing import TypeAlias

from ..episode_object import EpisodeObject, EpisodeObjectDict
from ..track_object import TrackObject, TrackObjectDict

CurrentlyPlaying: TypeAlias = TrackObject | EpisodeObject
"""The currently playing track or episode. Can be ``null``."""

CurrentlyPlayingDict: TypeAlias = TrackObjectDict | EpisodeObjectDict
