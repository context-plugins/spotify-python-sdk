from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemType1(str, Enum):
    """The ID type: currently only ``artist`` is supported."""

    ARTIST = "artist"

    __str__ = str.__str__


ItemType1OrStr: TypeAlias = Annotated[ItemType1 | str, open_enum_validator(ItemType1)]
