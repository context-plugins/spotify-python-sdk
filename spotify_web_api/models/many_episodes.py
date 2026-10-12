from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .episode_object import EpisodeObject, EpisodeObjectDict


class ManyEpisodes(SdkBaseModel):
    episodes: list[EpisodeObject]


class ManyEpisodesDict(TypedDict):
    episodes: list[EpisodeObjectDict]
