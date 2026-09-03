from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.currently_playing import CurrentlyPlaying, CurrentlyPlayingDict
from .unions.queue import Queue, QueueDict


class QueueObject(SdkBaseModel):
    currently_playing: Optional[CurrentlyPlaying] = UNSET
    """The currently playing track or episode. Can be ``null``."""

    queue: Optional[list[Queue]] = UNSET
    """The tracks or episodes in the queue. Can be empty."""


class QueueObjectDict(TypedDict):
    currently_playing: NotRequired[CurrentlyPlaying | CurrentlyPlayingDict]
    queue: NotRequired[list[Queue | QueueDict]]
