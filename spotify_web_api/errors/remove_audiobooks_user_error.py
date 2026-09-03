from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.forbidden1 import Forbidden1
from ..models.too_many_requests1 import TooManyRequests1
from ..models.unauthorized1 import Unauthorized1

RemoveAudiobooksUserErrorBody: TypeAlias = Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError


@dataclass(frozen=True, slots=True)
class _RemoveAudiobooksUserError:
    def map(self, response: HttpResponse) -> RemoveAudiobooksUserErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized1](response)
            case 403:
                return decode_json[Forbidden1](response)
            case 429:
                return decode_json[TooManyRequests1](response)
            case _:
                return RawError(response)


remove_audiobooks_user_error_mapper: Final[ErrorMapper[RemoveAudiobooksUserErrorBody]] = _RemoveAudiobooksUserError()
