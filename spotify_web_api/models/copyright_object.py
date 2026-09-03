from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CopyrightObject(SdkBaseModel):
    text: Optional[str] = UNSET
    """The copyright text for this content."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of copyright: ``C`` = the copyright, ``P`` = the sound recording (performance) copyright."""


class CopyrightObjectDict(TypedDict):
    text: NotRequired[str]
    type_: NotRequired[str]
