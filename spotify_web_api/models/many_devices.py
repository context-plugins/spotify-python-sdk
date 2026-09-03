from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_object import DeviceObject, DeviceObjectDict


class ManyDevices(SdkBaseModel):
    devices: list[DeviceObject]


class ManyDevicesDict(TypedDict):
    devices: list[DeviceObject | DeviceObjectDict]
