from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DisallowsObject(SdkBaseModel):
    interrupting_playback: Optional[bool] = UNSET
    """Interrupting playback. Optional field."""

    pausing: Optional[bool] = UNSET
    """Pausing. Optional field."""

    resuming: Optional[bool] = UNSET
    """Resuming. Optional field."""

    seeking: Optional[bool] = UNSET
    """Seeking playback location. Optional field."""

    skipping_next: Optional[bool] = UNSET
    """Skipping to the next context. Optional field."""

    skipping_prev: Optional[bool] = UNSET
    """Skipping to the previous context. Optional field."""

    toggling_repeat_context: Optional[bool] = UNSET
    """Toggling repeat context flag. Optional field."""

    toggling_shuffle: Optional[bool] = UNSET
    """Toggling shuffle flag. Optional field."""

    toggling_repeat_track: Optional[bool] = UNSET
    """Toggling repeat track flag. Optional field."""

    transferring_playback: Optional[bool] = UNSET
    """Transfering playback between devices. Optional field."""


class DisallowsObjectDict(TypedDict):
    interrupting_playback: NotRequired[bool]
    pausing: NotRequired[bool]
    resuming: NotRequired[bool]
    seeking: NotRequired[bool]
    skipping_next: NotRequired[bool]
    skipping_prev: NotRequired[bool]
    toggling_repeat_context: NotRequired[bool]
    toggling_shuffle: NotRequired[bool]
    toggling_repeat_track: NotRequired[bool]
    transferring_playback: NotRequired[bool]
