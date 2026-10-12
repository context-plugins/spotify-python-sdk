from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error_object import ErrorObject, ErrorObjectDict


class Forbidden1(SdkBaseModel):
    error: ErrorObject


class Forbidden1Dict(TypedDict):
    error: ErrorObjectDict
