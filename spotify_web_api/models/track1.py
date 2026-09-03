from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Track1(SdkBaseModel):
    uri: Optional[str] = UNSET
    """Spotify URI"""


class Track1Dict(TypedDict):
    uri: NotRequired[str]
