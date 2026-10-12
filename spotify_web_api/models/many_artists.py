from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .artist_object import ArtistObject, ArtistObjectDict


class ManyArtists(SdkBaseModel):
    artists: list[ArtistObject]


class ManyArtistsDict(TypedDict):
    artists: list[ArtistObjectDict]
