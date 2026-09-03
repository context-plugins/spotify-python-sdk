from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.forbidden1 import Forbidden1
from ..models.too_many_requests1 import TooManyRequests1
from ..models.unauthorized1 import Unauthorized1

CheckUsersSavedAudiobooksErrorBody: TypeAlias = Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError


@dataclass(frozen=True, slots=True)
class _CheckUsersSavedAudiobooksError:
    def map(self, response: HttpResponse) -> CheckUsersSavedAudiobooksErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized1](response)
            case 403:
                return decode_json[Forbidden1](response)
            case 429:
                return decode_json[TooManyRequests1](response)
            case _:
                return RawError(response)


check_users_saved_audiobooks_error_mapper: Final[
    ErrorMapper[CheckUsersSavedAudiobooksErrorBody]
] = _CheckUsersSavedAudiobooksError()
