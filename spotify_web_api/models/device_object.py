from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DeviceObject(SdkBaseModel):
    id: OptionalNullable[str] = UNSET
    """The device ID. This ID is unique and persistent to some extent. However, this is not guaranteed and any cached
    ``device_id`` should periodically be cleared out and refetched as necessary."""

    is_active: Optional[bool] = UNSET
    """If this device is the currently active device."""

    is_private_session: Optional[bool] = UNSET
    """If this device is currently in a private session."""

    is_restricted: Optional[bool] = UNSET
    """Whether controlling this device is restricted. At present if this is "true" then no Web API commands will be
    accepted by this device."""

    name: Optional[str] = UNSET
    r"""A human-readable name for the device. Some devices have a name that the user can configure (e.g. \"Loudest
    speaker\") and some devices have a generic name associated with the manufacturer or device model."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Device type, such as "computer", "smartphone" or "speaker"."""

    volume_percent: OptionalNullable[int] = UNSET
    """The current volume in percent."""

    supports_volume: Optional[bool] = UNSET
    """If this device can be used to set the volume."""


class DeviceObjectDict(TypedDict):
    id: NotRequired[str | None]
    is_active: NotRequired[bool]
    is_private_session: NotRequired[bool]
    is_restricted: NotRequired[bool]
    name: NotRequired[str]
    type_: NotRequired[str]
    volume_percent: NotRequired[int | None]
    supports_volume: NotRequired[bool]
