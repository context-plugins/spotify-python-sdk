from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .categories import Categories, CategoriesDict


class PagedCategories(SdkBaseModel):
    categories: Categories


class PagedCategoriesDict(TypedDict):
    categories: Categories | CategoriesDict
