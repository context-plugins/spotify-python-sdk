from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Itemtype(str, Enum):
    ALBUM = "album"
    ARTIST = "artist"
    PLAYLIST = "playlist"
    TRACK = "track"
    SHOW = "show"
    EPISODE = "episode"
    AUDIOBOOK = "audiobook"

    __str__ = str.__str__


ItemtypeOrStr: TypeAlias = Annotated[Itemtype | str, open_enum_validator(Itemtype)]
