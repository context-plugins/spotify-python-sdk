from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reason(str, Enum):
    """The reason for the restriction. Albums may be restricted if the content is not available in a given market, to
    the user's subscription type, or when the user's account is set to not play explicit content. Additional reasons may
    be added in the future."""

    MARKET = "market"
    PRODUCT = "product"
    EXPLICIT = "explicit"

    __str__ = str.__str__


ReasonOrStr: TypeAlias = Annotated[Reason | str, open_enum_validator(Reason)]
