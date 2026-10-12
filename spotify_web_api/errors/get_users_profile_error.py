from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.forbidden1 import Forbidden1
from ..models.too_many_requests1 import TooManyRequests1
from ..models.unauthorized1 import Unauthorized1

GetUsersProfileErrorBody: TypeAlias = Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError


@dataclass(frozen=True, slots=True)
class _GetUsersProfileError:
    def map(self, status_code: int, content: bytes) -> GetUsersProfileErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized1](content)
            case 403:
                return decode_json[Forbidden1](content)
            case 429:
                return decode_json[TooManyRequests1](content)
            case _:
                return RawError(status_code, content)


get_users_profile_error_mapper: Final[ErrorMapper[GetUsersProfileErrorBody]] = _GetUsersProfileError()
