from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .context_object import ContextObject, ContextObjectDict
from .device_object import DeviceObject, DeviceObjectDict
from .disallows_object import DisallowsObject, DisallowsObjectDict
from .unions.item import Item, ItemDict


class CurrentlyPlayingContextObject(SdkBaseModel):
    device: Optional[DeviceObject] = UNSET
    repeat_state: Optional[str] = UNSET
    """off, track, context"""

    shuffle_state: Optional[bool] = UNSET
    """If shuffle is on or off."""

    context: Optional[ContextObject] = UNSET
    timestamp: Optional[int] = UNSET
    """Unix Millisecond Timestamp when data was fetched."""

    progress_ms: Optional[int] = UNSET
    """Progress into the currently playing track or episode. Can be ``null``."""

    is_playing: Optional[bool] = UNSET
    """If something is currently playing, return ``true``."""

    item: Optional[Item] = UNSET
    """The currently playing track or episode. Can be ``null``."""

    currently_playing_type: Optional[str] = UNSET
    """The object type of the currently playing item. Can be one of ``track``, ``episode``, ``ad`` or ``unknown``."""

    actions: Optional[DisallowsObject] = UNSET


class CurrentlyPlayingContextObjectDict(TypedDict):
    device: NotRequired[DeviceObject | DeviceObjectDict]
    repeat_state: NotRequired[str]
    shuffle_state: NotRequired[bool]
    context: NotRequired[ContextObject | ContextObjectDict]
    timestamp: NotRequired[int]
    progress_ms: NotRequired[int]
    is_playing: NotRequired[bool]
    item: NotRequired[Item | ItemDict]
    currently_playing_type: NotRequired[str]
    actions: NotRequired[DisallowsObject | DisallowsObjectDict]
