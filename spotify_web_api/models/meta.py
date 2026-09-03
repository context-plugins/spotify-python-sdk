from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta(SdkBaseModel):
    analyzer_version: Optional[str] = UNSET
    """The version of the Analyzer used to analyze this track."""

    platform: Optional[str] = UNSET
    """The platform used to read the track's audio data."""

    detailed_status: Optional[str] = UNSET
    """A detailed status code for this track. If analysis data is missing, this code may explain why."""

    status_code: Optional[int] = UNSET
    """The return code of the analyzer process. 0 if successful, 1 if any errors occurred."""

    timestamp: Optional[int] = UNSET
    """The Unix timestamp (in seconds) at which this track was analyzed."""

    analysis_time: Optional[float] = UNSET
    """The amount of time taken to analyze this track."""

    input_process: Optional[str] = UNSET
    """The method used to read the track's audio data."""


class MetaDict(TypedDict):
    analyzer_version: NotRequired[str]
    platform: NotRequired[str]
    detailed_status: NotRequired[str]
    status_code: NotRequired[int]
    timestamp: NotRequired[int]
    analysis_time: NotRequired[float]
    input_process: NotRequired[str]
