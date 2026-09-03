from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .audiobook_object import AudiobookObject, AudiobookObjectDict


class ManyAudiobooks(SdkBaseModel):
    audiobooks: list[AudiobookObject]


class ManyAudiobooksDict(TypedDict):
    audiobooks: list[AudiobookObject | AudiobookObjectDict]
