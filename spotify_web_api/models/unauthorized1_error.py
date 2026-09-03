from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error_object import ErrorObject, ErrorObjectDict


class Unauthorized1Error(SdkBaseModel):
    error: ErrorObject


class Unauthorized1ErrorDict(TypedDict):
    error: ErrorObject | ErrorObjectDict
