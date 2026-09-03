from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MePlayerRequest(SdkBaseModel):
    device_ids: list[str]
    """A JSON array containing the ID of the device on which playback should be started/transferred.<br/>For
    example:``{device_ids:["74ASZWbe4lXaubB36ztrGX"]}``<br/>_**Note**: Although an array is accepted, only a single
    device_id is currently supported. Supplying more than one will return ``400 Bad Request``_"""

    play: Optional[bool] = UNSET
    """**true**: ensure playback happens on new device.<br/>**false** or not provided: keep the current playback
    state."""


class MePlayerRequestDict(TypedDict):
    device_ids: list[str]
    play: NotRequired[bool]
