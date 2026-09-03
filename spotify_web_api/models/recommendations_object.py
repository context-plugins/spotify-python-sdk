from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .recommendation_seed_object import RecommendationSeedObject, RecommendationSeedObjectDict
from .track_object import TrackObject, TrackObjectDict


class RecommendationsObject(SdkBaseModel):
    seeds: list[RecommendationSeedObject]
    """An array of recommendation seed objects."""

    tracks: list[TrackObject]
    """An array of track objects ordered according to the parameters supplied."""


class RecommendationsObjectDict(TypedDict):
    seeds: list[RecommendationSeedObject | RecommendationSeedObjectDict]
    tracks: list[TrackObject | TrackObjectDict]
