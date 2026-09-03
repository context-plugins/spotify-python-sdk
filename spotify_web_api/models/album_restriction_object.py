from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reason import ReasonOrStr


class AlbumRestrictionObject(SdkBaseModel):
    reason: Optional[ReasonOrStr] = UNSET


class AlbumRestrictionObjectDict(TypedDict):
    reason: NotRequired[ReasonOrStr]
