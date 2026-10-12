from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .image_object import ImageObject, ImageObjectDict


class CategoryObject(SdkBaseModel):
    href: str
    """A link to the Web API endpoint returning full details of the category."""

    icons: list[ImageObject]
    """The category icon, in various sizes."""

    id: str
    """The `Spotify category ID <https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids>`__ of
    the category."""

    name: str
    """The name of the category."""


class CategoryObjectDict(TypedDict):
    href: str
    icons: list[ImageObjectDict]
    id: str
    name: str
