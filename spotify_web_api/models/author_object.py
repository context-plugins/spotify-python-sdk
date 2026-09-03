from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AuthorObject(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the author."""


class AuthorObjectDict(TypedDict):
    name: NotRequired[str]
