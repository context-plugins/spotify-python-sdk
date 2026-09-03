from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Markets(SdkBaseModel):
    markets: Optional[list[str]] = UNSET


class MarketsDict(TypedDict):
    markets: NotRequired[list[str]]
