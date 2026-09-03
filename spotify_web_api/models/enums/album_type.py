from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AlbumType(str, Enum):
    """The type of the album."""

    ALBUM = "album"
    SINGLE = "single"
    COMPILATION = "compilation"

    __str__ = str.__str__


AlbumTypeOrStr: TypeAlias = Annotated[AlbumType | str, open_enum_validator(AlbumType)]
