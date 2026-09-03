from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CursorObject(SdkBaseModel):
    after: Optional[str] = UNSET
    """The cursor to use as key to find the next page of items."""

    before: Optional[str] = UNSET
    """The cursor to use as key to find the previous page of items."""


class CursorObjectDict(TypedDict):
    after: NotRequired[str]
    before: NotRequired[str]
