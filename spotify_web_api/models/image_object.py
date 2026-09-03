from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ImageObject(SdkBaseModel):
    url: str
    """The source URL of the image."""

    height: int | None
    """The image height in pixels."""

    width: int | None
    """The image width in pixels."""


class ImageObjectDict(TypedDict):
    url: str
    height: int | None
    width: int | None
