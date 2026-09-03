from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    oauth_2_0: AuthScheme
    oauth_2_0_client_credentials: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    oauth_2_0: AsyncAuthScheme
    oauth_2_0_client_credentials: AsyncAuthScheme


Oauth20Scope: TypeAlias = Literal[
    "app-remote-control",
    "playlist-read-private",
    "playlist-read-collaborative",
    "playlist-modify-public",
    "playlist-modify-private",
    "user-library-read",
    "user-library-modify",
    "user-read-private",
    "user-read-email",
    "user-follow-read",
    "user-follow-modify",
    "user-top-read",
    "user-read-playback-position",
    "user-read-playback-state",
    "user-read-recently-played",
    "user-read-currently-playing",
    "user-modify-playback-state",
    "ugc-image-upload",
    "streaming",
]
"""``app-remote-control``: Communicate with the Spotify app on your device. ``playlist-read-private``: Access your
private playlists. ``playlist-read-collaborative``: Access your collaborative playlists. ``playlist-modify-public``:
Manage your public playlists. ``playlist-modify-private``: Manage your private playlists. ``user-library-read``: Access
your saved content. ``user-library-modify``: Manage your saved content. ``user-read-private``: Access your subscription
details. ``user-read-email``: Get your real email address. ``user-follow-read``: Access your followers and who you are
following. ``user-follow-modify``: Manage your saved content. ``user-top-read``: Read your top artists and content.
``user-read-playback-position``: Read your position in content you have played. ``user-read-playback-state``: Read your
currently playing content and Spotify Connect devices information. ``user-read-recently-played``: Access your recently
played items. ``user-read-currently-playing``: Read your currently playing content. ``user-modify-playback-state``:
Control playback on your Spotify clients and Spotify Connect devices. ``ugc-image-upload``: Upload images to Spotify on
your behalf. ``streaming``: Play content and control playback on your other devices."""
