from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .chapter_object import ChapterObject, ChapterObjectDict


class ManyChapters(SdkBaseModel):
    chapters: list[ChapterObject]


class ManyChaptersDict(TypedDict):
    chapters: list[ChapterObject | ChapterObjectDict]
