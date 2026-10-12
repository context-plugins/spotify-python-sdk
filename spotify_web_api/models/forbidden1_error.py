from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error_object import ErrorObject, ErrorObjectDict


class Forbidden1Error(SdkBaseModel):
    error: ErrorObject


class Forbidden1ErrorDict(TypedDict):
    error: ErrorObjectDict
