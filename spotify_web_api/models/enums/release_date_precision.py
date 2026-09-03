from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReleaseDatePrecision(str, Enum):
    """The precision with which ``release_date`` value is known."""

    YEAR = "year"
    MONTH = "month"
    DAY = "day"

    __str__ = str.__str__


ReleaseDatePrecisionOrStr: TypeAlias = Annotated[ReleaseDatePrecision | str, open_enum_validator(ReleaseDatePrecision)]
