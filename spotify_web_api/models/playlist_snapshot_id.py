from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PlaylistSnapshotId(SdkBaseModel):
    snapshot_id: Optional[str] = UNSET


class PlaylistSnapshotIdDict(TypedDict):
    snapshot_id: NotRequired[str]
