from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExplicitContentSettingsObject(SdkBaseModel):
    filter_enabled: Optional[bool] = UNSET
    """When ``true``, indicates that explicit content should not be played."""

    filter_locked: Optional[bool] = UNSET
    """When ``true``, indicates that the explicit content setting is locked and can't be changed by the user."""


class ExplicitContentSettingsObjectDict(TypedDict):
    filter_enabled: NotRequired[bool]
    filter_locked: NotRequired[bool]
