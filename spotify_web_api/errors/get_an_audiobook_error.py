from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.bad_request1 import BadRequest1
from ..models.forbidden1 import Forbidden1
from ..models.not_found1 import NotFound1
from ..models.too_many_requests1 import TooManyRequests1
from ..models.unauthorized1 import Unauthorized1

GetAnAudiobookErrorBody: TypeAlias = BadRequest1 | Unauthorized1 | Forbidden1 | NotFound1 | TooManyRequests1 | RawError


@dataclass(frozen=True, slots=True)
class _GetAnAudiobookError:
    def map(self, status_code: int, content: bytes) -> GetAnAudiobookErrorBody:
        match status_code:
            case 400:
                return decode_json[BadRequest1](content)
            case 401:
                return decode_json[Unauthorized1](content)
            case 403:
                return decode_json[Forbidden1](content)
            case 404:
                return decode_json[NotFound1](content)
            case 429:
                return decode_json[TooManyRequests1](content)
            case _:
                return RawError(status_code, content)


get_an_audiobook_error_mapper: Final[ErrorMapper[GetAnAudiobookErrorBody]] = _GetAnAudiobookError()
