from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .audio_features_object import AudioFeaturesObject, AudioFeaturesObjectDict


class ManyAudioFeatures(SdkBaseModel):
    audio_features: list[AudioFeaturesObject]


class ManyAudioFeaturesDict(TypedDict):
    audio_features: list[AudioFeaturesObject | AudioFeaturesObjectDict]
