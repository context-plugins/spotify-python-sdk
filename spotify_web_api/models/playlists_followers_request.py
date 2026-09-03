from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PlaylistsFollowersRequest(SdkBaseModel):
    public: Optional[bool] = UNSET
    """Defaults to ``true``. If ``true`` the playlist will be included in user's public playlists, if ``false`` it will
    remain private."""


class PlaylistsFollowersRequestDict(TypedDict):
    public: NotRequired[bool]
