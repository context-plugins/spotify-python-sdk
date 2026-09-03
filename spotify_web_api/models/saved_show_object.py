from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .show_base import ShowBase, ShowBaseDict


class SavedShowObject(SdkBaseModel):
    added_at: Optional[RFC3339DateTime] = UNSET
    """The date and time the show was saved. Timestamps are returned in ISO 8601 format as Coordinated Universal Time
    (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ. If the time is imprecise (for example, the date/time of an album
    release), an additional field indicates the precision; see for example, release_date in an album object."""

    show: Optional[ShowBase] = UNSET


class SavedShowObjectDict(TypedDict):
    added_at: NotRequired[RFC3339DateTime]
    show: NotRequired[ShowBase | ShowBaseDict]
