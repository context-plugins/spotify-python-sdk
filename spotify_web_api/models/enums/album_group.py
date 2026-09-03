from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AlbumGroup(str, Enum):
    """This field describes the relationship between the artist and the album."""

    ALBUM = "album"
    SINGLE = "single"
    COMPILATION = "compilation"
    APPEARS_ON = "appears_on"

    __str__ = str.__str__


AlbumGroupOrStr: TypeAlias = Annotated[AlbumGroup | str, open_enum_validator(AlbumGroup)]
