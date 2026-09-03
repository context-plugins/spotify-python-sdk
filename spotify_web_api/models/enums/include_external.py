from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludeExternal(str, Enum):
    """If ``include_external=audio`` is specified it signals that the client can play externally hosted audio content,
    and marks the content as playable in the response. By default externally hosted audio content is marked as
    unplayable in the response."""

    AUDIO = "audio"

    __str__ = str.__str__


IncludeExternalOrStr: TypeAlias = Annotated[IncludeExternal | str, open_enum_validator(IncludeExternal)]
