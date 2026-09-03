from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemType3(str, Enum):
    """The ID type: either ``artist`` or ``user``."""

    ARTIST = "artist"
    USER = "user"

    __str__ = str.__str__


ItemType3OrStr: TypeAlias = Annotated[ItemType3 | str, open_enum_validator(ItemType3)]
