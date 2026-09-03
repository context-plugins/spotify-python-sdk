from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error_object import ErrorObject, ErrorObjectDict


class TooManyRequests1(SdkBaseModel):
    error: ErrorObject


class TooManyRequests1Dict(TypedDict):
    error: ErrorObject | ErrorObjectDict
