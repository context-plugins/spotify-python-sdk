from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type8(str, Enum):
    """The object type."""

    AUDIO_FEATURES = "audio_features"

    __str__ = str.__str__


Type8OrStr: TypeAlias = Annotated[Type8 | str, open_enum_validator(Type8)]
