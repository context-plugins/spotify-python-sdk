from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PlaylistTracksRefObject(SdkBaseModel):
    href: Optional[str] = UNSET
    """A link to the Web API endpoint where full details of the playlist's tracks can be retrieved."""

    total: Optional[int] = UNSET
    """Number of tracks in the playlist."""


class PlaylistTracksRefObjectDict(TypedDict):
    href: NotRequired[str]
    total: NotRequired[int]
