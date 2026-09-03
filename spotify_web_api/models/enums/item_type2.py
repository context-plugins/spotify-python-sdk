from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemType2(str, Enum):
    """The ID type."""

    ARTIST = "artist"
    USER = "user"

    __str__ = str.__str__


ItemType2OrStr: TypeAlias = Annotated[ItemType2 | str, open_enum_validator(ItemType2)]
