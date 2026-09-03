from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .show_base import ShowBase, ShowBaseDict


class ManySimplifiedShows(SdkBaseModel):
    shows: list[ShowBase]


class ManySimplifiedShowsDict(TypedDict):
    shows: list[ShowBase | ShowBaseDict]
