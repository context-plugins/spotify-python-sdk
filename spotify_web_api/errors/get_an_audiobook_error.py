from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.bad_request1 import BadRequest1
from ..models.forbidden1 import Forbidden1
from ..models.not_found1 import NotFound1
from ..models.too_many_requests1 import TooManyRequests1
from ..models.unauthorized1 import Unauthorized1

GetAnAudiobookErrorBody: TypeAlias = BadRequest1 | Unauthorized1 | Forbidden1 | NotFound1 | TooManyRequests1 | RawError


@dataclass(frozen=True, slots=True)
class _GetAnAudiobookError:
    def map(self, response: HttpResponse) -> GetAnAudiobookErrorBody:
        match response.status_code:
            case 400:
                return decode_json[BadRequest1](response)
            case 401:
                return decode_json[Unauthorized1](response)
            case 403:
                return decode_json[Forbidden1](response)
            case 404:
                return decode_json[NotFound1](response)
            case 429:
                return decode_json[TooManyRequests1](response)
            case _:
                return RawError(response)


get_an_audiobook_error_mapper: Final[ErrorMapper[GetAnAudiobookErrorBody]] = _GetAnAudiobookError()
