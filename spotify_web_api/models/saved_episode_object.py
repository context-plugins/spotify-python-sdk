from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .episode_object import EpisodeObject, EpisodeObjectDict


class SavedEpisodeObject(SdkBaseModel):
    added_at: Optional[RFC3339DateTime] = UNSET
    """The date and time the episode was saved. Timestamps are returned in ISO 8601 format as Coordinated Universal Time
    (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ."""

    episode: Optional[EpisodeObject] = UNSET


class SavedEpisodeObjectDict(TypedDict):
    added_at: NotRequired[RFC3339DateTime]
    episode: NotRequired[EpisodeObject | EpisodeObjectDict]
