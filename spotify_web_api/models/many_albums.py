from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .album_object import AlbumObject, AlbumObjectDict


class ManyAlbums(SdkBaseModel):
    albums: list[AlbumObject]


class ManyAlbumsDict(TypedDict):
    albums: list[AlbumObjectDict]
