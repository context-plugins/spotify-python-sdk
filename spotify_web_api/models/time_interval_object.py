from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TimeIntervalObject(SdkBaseModel):
    start: Optional[float] = UNSET
    """The starting point (in seconds) of the time interval."""

    duration: Optional[float] = UNSET
    """The duration (in seconds) of the time interval."""

    confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the interval."""


class TimeIntervalObjectDict(TypedDict):
    start: NotRequired[float]
    duration: NotRequired[float]
    confidence: NotRequired[float]
