from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ErrorObject(SdkBaseModel):
    status: int
    """The HTTP status code (also returned in the response header; see `Response Status Codes
    <https://developer.spotify.com/documentation/web-api/concepts/api-calls#response-status-codes>`__ for more
    information)."""

    message: str
    """A short description of the cause of the error."""


class ErrorObjectDict(TypedDict):
    status: int
    message: str
