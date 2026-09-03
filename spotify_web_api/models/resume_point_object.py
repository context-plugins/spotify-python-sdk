from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResumePointObject(SdkBaseModel):
    fully_played: Optional[bool] = UNSET
    """Whether or not the episode has been fully played by the user."""

    resume_position_ms: Optional[int] = UNSET
    """The user's most recent position in the episode in milliseconds."""


class ResumePointObjectDict(TypedDict):
    fully_played: NotRequired[bool]
    resume_position_ms: NotRequired[int]
