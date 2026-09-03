from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Mode(int, Enum):
    """Indicates the modality (major or minor) of a section, the type of scale from which its melodic content is
    derived. This field will contain a 0 for "minor", a 1 for "major", or a -1 for no result. Note that the major key
    (e.g. C major) could more likely be confused with the minor key at 3 semitones lower (e.g. A minor) as both keys
    carry the same pitches."""

    NEGATIVE_1 = -1
    """No result."""

    VALUE_0 = 0
    """Minor modality."""

    VALUE_1 = 1
    """Major modality."""

    __str__ = str.__str__


ModeOrInt: TypeAlias = Annotated[Mode | int, open_enum_validator(Mode)]
