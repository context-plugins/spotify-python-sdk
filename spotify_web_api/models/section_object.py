from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.mode import ModeOrInt


class SectionObject(SdkBaseModel):
    start: Optional[float] = UNSET
    """The starting point (in seconds) of the section."""

    duration: Optional[float] = UNSET
    """The duration (in seconds) of the section."""

    confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the section's "designation"."""

    loudness: Optional[float] = UNSET
    """The overall loudness of the section in decibels (dB). Loudness values are useful for comparing relative loudness
    of sections within tracks."""

    tempo: Optional[float] = UNSET
    """The overall estimated tempo of the section in beats per minute (BPM). In musical terminology, tempo is the speed
    or pace of a given piece and derives directly from the average beat duration."""

    tempo_confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the tempo. Some tracks contain tempo changes or sounds
    which don't contain tempo (like pure speech) which would correspond to a low value in this field."""

    key: Optional[int] = UNSET
    """The estimated overall key of the section. The values in this field ranging from 0 to 11 mapping to pitches using
    standard Pitch Class notation (E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on). If no key was detected, the value is -1."""

    key_confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the key. Songs with many key changes may correspond to low
    values in this field."""

    mode: Optional[ModeOrInt] = UNSET
    mode_confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the ``mode``."""

    time_signature: Optional[int] = UNSET
    """An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are
    in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4"."""

    time_signature_confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the ``time_signature``. Sections with time signature
    changes may correspond to low values in this field."""


class SectionObjectDict(TypedDict):
    start: NotRequired[float]
    duration: NotRequired[float]
    confidence: NotRequired[float]
    loudness: NotRequired[float]
    tempo: NotRequired[float]
    tempo_confidence: NotRequired[float]
    key: NotRequired[int]
    key_confidence: NotRequired[float]
    mode: NotRequired[ModeOrInt]
    mode_confidence: NotRequired[float]
    time_signature: NotRequired[int]
    time_signature_confidence: NotRequired[float]
