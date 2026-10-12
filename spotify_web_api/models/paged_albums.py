from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .paging_simplified_album_object import PagingSimplifiedAlbumObject, PagingSimplifiedAlbumObjectDict


class PagedAlbums(SdkBaseModel):
    albums: PagingSimplifiedAlbumObject


class PagedAlbumsDict(TypedDict):
    albums: PagingSimplifiedAlbumObjectDict
