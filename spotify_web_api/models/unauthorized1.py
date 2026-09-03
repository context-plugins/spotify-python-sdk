from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error_object import ErrorObject, ErrorObjectDict


class Unauthorized1(SdkBaseModel):
    error: ErrorObject


class Unauthorized1Dict(TypedDict):
    error: ErrorObject | ErrorObjectDict
