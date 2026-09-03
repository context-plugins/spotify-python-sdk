from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FollowersObject(SdkBaseModel):
    href: OptionalNullable[str] = UNSET
    """This will always be set to null, as the Web API does not support it at the moment."""

    total: Optional[int] = UNSET
    """The total number of followers."""


class FollowersObjectDict(TypedDict):
    href: NotRequired[str | None]
    total: NotRequired[int]
