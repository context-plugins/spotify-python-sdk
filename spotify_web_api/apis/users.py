from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.check_current_user_follows_error import (
    CheckCurrentUserFollowsErrorBody,
    check_current_user_follows_error_mapper,
)
from ..errors.check_if_user_follows_playlist_error import (
    CheckIfUserFollowsPlaylistErrorBody,
    check_if_user_follows_playlist_error_mapper,
)
from ..errors.follow_artists_users_error import FollowArtistsUsersErrorBody, follow_artists_users_error_mapper
from ..errors.follow_playlist_error import FollowPlaylistErrorBody, follow_playlist_error_mapper
from ..errors.get_current_users_profile_error import (
    GetCurrentUsersProfileErrorBody,
    get_current_users_profile_error_mapper,
)
from ..errors.get_followed_error import GetFollowedErrorBody, get_followed_error_mapper
from ..errors.get_list_users_playlists_error import (
    GetListUsersPlaylistsErrorBody,
    get_list_users_playlists_error_mapper,
)
from ..errors.get_users_profile_error import GetUsersProfileErrorBody, get_users_profile_error_mapper
from ..errors.get_users_top_artists_error import GetUsersTopArtistsErrorBody, get_users_top_artists_error_mapper
from ..errors.get_users_top_tracks_error import GetUsersTopTracksErrorBody, get_users_top_tracks_error_mapper
from ..errors.unfollow_artists_users_error import UnfollowArtistsUsersErrorBody, unfollow_artists_users_error_mapper
from ..errors.unfollow_playlist_error import UnfollowPlaylistErrorBody, unfollow_playlist_error_mapper
from ..models.cursor_paged_artists import CursorPagedArtists
from ..models.enums.item_type1 import ItemType1OrStr
from ..models.enums.item_type2 import ItemType2OrStr
from ..models.enums.item_type3 import ItemType3OrStr
from ..models.follow_artists_or_users_request import FollowArtistsOrUsersRequest, FollowArtistsOrUsersRequestDict
from ..models.paging_artist_object import PagingArtistObject
from ..models.paging_playlist_object import PagingPlaylistObject
from ..models.paging_track_object import PagingTrackObject
from ..models.playlists_followers_request import PlaylistsFollowersRequest, PlaylistsFollowersRequestDict
from ..models.private_user_object import PrivateUserObject
from ..models.public_user_object import PublicUserObject
from ..models.unfollow_artists_or_users_request import UnfollowArtistsOrUsersRequest, UnfollowArtistsOrUsersRequestDict
from ..server.server import Server


class Users:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersWithRawResponse(client, server, auth)

    def check_current_user_follows(
        self, type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check to see if the current user is following one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.check_current_user_follows(type_, ids, request_options=request_options))

    def check_if_user_follows_playlist(
        self, playlist_id: str, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check to see if one or more Spotify users are following a specified playlist.

        Args:
            playlist_id: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.check_if_user_follows_playlist(playlist_id, ids, request_options=request_options)
        )

    def follow_artists_users(
        self,
        type_: ItemType2OrStr,
        ids: str,
        *,
        body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Add the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Artist or user followed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.follow_artists_users(type_, ids, body=body, request_options=request_options)
        )

    def follow_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsFollowersRequest | PlaylistsFollowersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Add the current user as a follower of a playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playlist followed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.follow_playlist(playlist_id, body=body, request_options=request_options))

    def get_current_users_profile(self, *, request_options: RequestOptionsOrDict | None = None) -> PrivateUserObject:
        """Get detailed profile information about the current user (including the current user's username).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A user

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_current_users_profile(request_options=request_options))

    def get_followed(
        self,
        type_: ItemType1OrStr,
        *,
        after: str | None = None,
        limit: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CursorPagedArtists:
        """Get the current user's followed artists.

        Args:
            type_: Value sent with the request.
            after: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A paged set of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_followed(type_, after=after, limit=limit, request_options=request_options)
        )

    def get_list_users_playlists(
        self,
        user_id: str,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingPlaylistObject:
        """Get a list of the playlists owned or followed by a Spotify user.

        Args:
            user_id: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A paged set of playlists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_list_users_playlists(
                user_id, limit=limit, offset=offset, request_options=request_options
            ),
        )

    def get_users_profile(
        self, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PublicUserObject:
        """Get public profile information about a Spotify user.

        Args:
            user_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A user

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_users_profile(user_id, request_options=request_options))

    def get_users_top_artists(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingArtistObject:
        """Get the current user's top artists based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_users_top_artists(
                time_range=time_range, limit=limit, offset=offset, request_options=request_options
            ),
        )

    def get_users_top_tracks(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingTrackObject:
        """Get the current user's top tracks based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_users_top_tracks(
                time_range=time_range, limit=limit, offset=offset, request_options=request_options
            ),
        )

    def unfollow_artists_users(
        self,
        type_: ItemType3OrStr,
        ids: str,
        *,
        body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Artist or user unfollowed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.unfollow_artists_users(type_, ids, body=body, request_options=request_options)
        )

    def unfollow_playlist(self, playlist_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove the current user as a follower of a playlist.

        Args:
            playlist_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playlist unfollowed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.unfollow_playlist(playlist_id, request_options=request_options))

    @property
    def with_raw_response(self) -> UsersWithRawResponse:
        return self._with_raw_response


class AsyncUsers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersWithRawResponse(client, server, auth)

    async def check_current_user_follows(
        self, type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check to see if the current user is following one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.check_current_user_follows(type_, ids, request_options=request_options)
        )

    async def check_if_user_follows_playlist(
        self, playlist_id: str, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check to see if one or more Spotify users are following a specified playlist.

        Args:
            playlist_id: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.check_if_user_follows_playlist(
                playlist_id, ids, request_options=request_options
            ),
        )

    async def follow_artists_users(
        self,
        type_: ItemType2OrStr,
        ids: str,
        *,
        body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Add the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Artist or user followed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.follow_artists_users(type_, ids, body=body, request_options=request_options)
        )

    async def follow_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsFollowersRequest | PlaylistsFollowersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Add the current user as a follower of a playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playlist followed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.follow_playlist(playlist_id, body=body, request_options=request_options)
        )

    async def get_current_users_profile(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> PrivateUserObject:
        """Get detailed profile information about the current user (including the current user's username).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A user

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_current_users_profile(request_options=request_options))

    async def get_followed(
        self,
        type_: ItemType1OrStr,
        *,
        after: str | None = None,
        limit: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CursorPagedArtists:
        """Get the current user's followed artists.

        Args:
            type_: Value sent with the request.
            after: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A paged set of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_followed(type_, after=after, limit=limit, request_options=request_options)
        )

    async def get_list_users_playlists(
        self,
        user_id: str,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingPlaylistObject:
        """Get a list of the playlists owned or followed by a Spotify user.

        Args:
            user_id: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A paged set of playlists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_list_users_playlists(
                user_id, limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def get_users_profile(
        self, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PublicUserObject:
        """Get public profile information about a Spotify user.

        Args:
            user_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A user

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_users_profile(user_id, request_options=request_options))

    async def get_users_top_artists(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingArtistObject:
        """Get the current user's top artists based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_users_top_artists(
                time_range=time_range, limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def get_users_top_tracks(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingTrackObject:
        """Get the current user's top tracks based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_users_top_tracks(
                time_range=time_range, limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def unfollow_artists_users(
        self,
        type_: ItemType3OrStr,
        ids: str,
        *,
        body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Artist or user unfollowed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.unfollow_artists_users(type_, ids, body=body, request_options=request_options)
        )

    async def unfollow_playlist(self, playlist_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove the current user as a follower of a playlist.

        Args:
            playlist_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playlist unfollowed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.unfollow_playlist(playlist_id, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncUsersWithRawResponse:
        return self._with_raw_response


class UsersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_current_user_follows(
        self, type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckCurrentUserFollowsErrorBody]:
        """Check to see if the current user is following one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following/contains"),
            query_params=[param[ItemType3OrStr]("type", type_), param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_current_user_follows_error_mapper,
            request_options=request_options,
        )

    def check_if_user_follows_playlist(
        self, playlist_id: str, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckIfUserFollowsPlaylistErrorBody]:
        """Check to see if one or more Spotify users are following a specified playlist.

        Args:
            playlist_id: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}/followers/contains"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_if_user_follows_playlist_error_mapper,
            request_options=request_options,
        )

    def follow_artists_users(
        self,
        type_: ItemType2OrStr,
        ids: str,
        *,
        body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, FollowArtistsUsersErrorBody]:
        """Add the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/following"),
            query_params=[param[ItemType2OrStr]("type", type_), param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=follow_artists_users_error_mapper,
            request_options=request_options,
        )

    def follow_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsFollowersRequest | PlaylistsFollowersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, FollowPlaylistErrorBody]:
        """Add the current user as a follower of a playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}/followers"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsFollowersRequest | PlaylistsFollowersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=follow_playlist_error_mapper,
            request_options=request_options,
        )

    def get_current_users_profile(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PrivateUserObject, GetCurrentUsersProfileErrorBody]:
        """Get detailed profile information about the current user (including the current user's username).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PrivateUserObject],
            error_mapper=get_current_users_profile_error_mapper,
            request_options=request_options,
        )

    def get_followed(
        self,
        type_: ItemType1OrStr,
        *,
        after: str | None = None,
        limit: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CursorPagedArtists, GetFollowedErrorBody]:
        """Get the current user's followed artists.

        Args:
            type_: Value sent with the request.
            after: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following"),
            query_params=[
                param[ItemType1OrStr]("type", type_),
                param[str | None]("after", after),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[CursorPagedArtists],
            error_mapper=get_followed_error_mapper,
            request_options=request_options,
        )

    def get_list_users_playlists(
        self,
        user_id: str,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingPlaylistObject, GetListUsersPlaylistsErrorBody]:
        """Get a list of the playlists owned or followed by a Spotify user.

        Args:
            user_id: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/playlists"),
            path_params=[param[str]("user_id", user_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingPlaylistObject],
            error_mapper=get_list_users_playlists_error_mapper,
            request_options=request_options,
        )

    def get_users_profile(
        self, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PublicUserObject, GetUsersProfileErrorBody]:
        """Get public profile information about a Spotify user.

        Args:
            user_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}"),
            path_params=[param[str]("user_id", user_id)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PublicUserObject],
            error_mapper=get_users_profile_error_mapper,
            request_options=request_options,
        )

    def get_users_top_artists(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingArtistObject, GetUsersTopArtistsErrorBody]:
        """Get the current user's top artists based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/top/artists"),
            query_params=[
                param[str | None]("time_range", time_range),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingArtistObject],
            error_mapper=get_users_top_artists_error_mapper,
            request_options=request_options,
        )

    def get_users_top_tracks(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingTrackObject, GetUsersTopTracksErrorBody]:
        """Get the current user's top tracks based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/top/tracks"),
            query_params=[
                param[str | None]("time_range", time_range),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingTrackObject],
            error_mapper=get_users_top_tracks_error_mapper,
            request_options=request_options,
        )

    def unfollow_artists_users(
        self,
        type_: ItemType3OrStr,
        ids: str,
        *,
        body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UnfollowArtistsUsersErrorBody]:
        """Remove the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/following"),
            query_params=[param[ItemType3OrStr]("type", type_), param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=unfollow_artists_users_error_mapper,
            request_options=request_options,
        )

    def unfollow_playlist(
        self, playlist_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnfollowPlaylistErrorBody]:
        """Remove the current user as a follower of a playlist.

        Args:
            playlist_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/playlists/{playlist_id}/followers"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=unfollow_playlist_error_mapper,
            request_options=request_options,
        )


class AsyncUsersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_current_user_follows(
        self, type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckCurrentUserFollowsErrorBody]:
        """Check to see if the current user is following one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following/contains"),
            query_params=[param[ItemType3OrStr]("type", type_), param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[list[bool]],
            error_mapper=check_current_user_follows_error_mapper,
            request_options=request_options,
        )

    async def check_if_user_follows_playlist(
        self, playlist_id: str, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckIfUserFollowsPlaylistErrorBody]:
        """Check to see if one or more Spotify users are following a specified playlist.

        Args:
            playlist_id: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}/followers/contains"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[list[bool]],
            error_mapper=check_if_user_follows_playlist_error_mapper,
            request_options=request_options,
        )

    async def follow_artists_users(
        self,
        type_: ItemType2OrStr,
        ids: str,
        *,
        body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, FollowArtistsUsersErrorBody]:
        """Add the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/following"),
            query_params=[param[ItemType2OrStr]("type", type_), param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=follow_artists_users_error_mapper,
            request_options=request_options,
        )

    async def follow_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsFollowersRequest | PlaylistsFollowersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, FollowPlaylistErrorBody]:
        """Add the current user as a follower of a playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}/followers"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsFollowersRequest | PlaylistsFollowersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=follow_playlist_error_mapper,
            request_options=request_options,
        )

    async def get_current_users_profile(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PrivateUserObject, GetCurrentUsersProfileErrorBody]:
        """Get detailed profile information about the current user (including the current user's username).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PrivateUserObject],
            error_mapper=get_current_users_profile_error_mapper,
            request_options=request_options,
        )

    async def get_followed(
        self,
        type_: ItemType1OrStr,
        *,
        after: str | None = None,
        limit: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CursorPagedArtists, GetFollowedErrorBody]:
        """Get the current user's followed artists.

        Args:
            type_: Value sent with the request.
            after: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following"),
            query_params=[
                param[ItemType1OrStr]("type", type_),
                param[str | None]("after", after),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[CursorPagedArtists],
            error_mapper=get_followed_error_mapper,
            request_options=request_options,
        )

    async def get_list_users_playlists(
        self,
        user_id: str,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingPlaylistObject, GetListUsersPlaylistsErrorBody]:
        """Get a list of the playlists owned or followed by a Spotify user.

        Args:
            user_id: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/playlists"),
            path_params=[param[str]("user_id", user_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingPlaylistObject],
            error_mapper=get_list_users_playlists_error_mapper,
            request_options=request_options,
        )

    async def get_users_profile(
        self, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PublicUserObject, GetUsersProfileErrorBody]:
        """Get public profile information about a Spotify user.

        Args:
            user_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}"),
            path_params=[param[str]("user_id", user_id)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PublicUserObject],
            error_mapper=get_users_profile_error_mapper,
            request_options=request_options,
        )

    async def get_users_top_artists(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingArtistObject, GetUsersTopArtistsErrorBody]:
        """Get the current user's top artists based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/top/artists"),
            query_params=[
                param[str | None]("time_range", time_range),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingArtistObject],
            error_mapper=get_users_top_artists_error_mapper,
            request_options=request_options,
        )

    async def get_users_top_tracks(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingTrackObject, GetUsersTopTracksErrorBody]:
        """Get the current user's top tracks based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/top/tracks"),
            query_params=[
                param[str | None]("time_range", time_range),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingTrackObject],
            error_mapper=get_users_top_tracks_error_mapper,
            request_options=request_options,
        )

    async def unfollow_artists_users(
        self,
        type_: ItemType3OrStr,
        ids: str,
        *,
        body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UnfollowArtistsUsersErrorBody]:
        """Remove the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/following"),
            query_params=[param[ItemType3OrStr]("type", type_), param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=unfollow_artists_users_error_mapper,
            request_options=request_options,
        )

    async def unfollow_playlist(
        self, playlist_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnfollowPlaylistErrorBody]:
        """Remove the current user as a follower of a playlist.

        Args:
            playlist_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/playlists/{playlist_id}/followers"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=unfollow_playlist_error_mapper,
            request_options=request_options,
        )
