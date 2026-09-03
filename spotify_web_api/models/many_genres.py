from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ManyGenres(SdkBaseModel):
    genres: list[str]


class ManyGenresDict(TypedDict):
    genres: list[str]
