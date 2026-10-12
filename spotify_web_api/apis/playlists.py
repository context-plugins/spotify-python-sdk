from __future__ import annotations

from typing import Any
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
    text_body,
    unwrap,
)
from ..errors.add_tracks_to_playlist_error import AddTracksToPlaylistErrorBody, add_tracks_to_playlist_error_mapper
from ..errors.change_playlist_details_error import ChangePlaylistDetailsErrorBody, change_playlist_details_error_mapper
from ..errors.check_if_user_follows_playlist_error import (
    CheckIfUserFollowsPlaylistErrorBody,
    check_if_user_follows_playlist_error_mapper,
)
from ..errors.create_playlist_error import CreatePlaylistErrorBody, create_playlist_error_mapper
from ..errors.follow_playlist_error import FollowPlaylistErrorBody, follow_playlist_error_mapper
from ..errors.get_a_categories_playlists_error import (
    GetACategoriesPlaylistsErrorBody,
    get_a_categories_playlists_error_mapper,
)
from ..errors.get_a_list_of_current_users_playlists_error import (
    GetAListOfCurrentUsersPlaylistsErrorBody,
    get_a_list_of_current_users_playlists_error_mapper,
)
from ..errors.get_featured_playlists_error import GetFeaturedPlaylistsErrorBody, get_featured_playlists_error_mapper
from ..errors.get_list_users_playlists_error import (
    GetListUsersPlaylistsErrorBody,
    get_list_users_playlists_error_mapper,
)
from ..errors.get_playlist_cover_error import GetPlaylistCoverErrorBody, get_playlist_cover_error_mapper
from ..errors.get_playlist_error import GetPlaylistErrorBody, get_playlist_error_mapper
from ..errors.get_playlists_tracks_error import GetPlaylistsTracksErrorBody, get_playlists_tracks_error_mapper
from ..errors.remove_tracks_playlist_error import RemoveTracksPlaylistErrorBody, remove_tracks_playlist_error_mapper
from ..errors.reorder_or_replace_playlists_tracks_error import (
    ReorderOrReplacePlaylistsTracksErrorBody,
    reorder_or_replace_playlists_tracks_error_mapper,
)
from ..errors.unfollow_playlist_error import UnfollowPlaylistErrorBody, unfollow_playlist_error_mapper
from ..errors.upload_custom_playlist_cover_error import (
    UploadCustomPlaylistCoverErrorBody,
    upload_custom_playlist_cover_error_mapper,
)
from ..models.image_object import ImageObject
from ..models.paging_featured_playlist_object import PagingFeaturedPlaylistObject
from ..models.paging_playlist_object import PagingPlaylistObject
from ..models.paging_playlist_track_object import PagingPlaylistTrackObject
from ..models.playlist_object import PlaylistObject
from ..models.playlist_snapshot_id import PlaylistSnapshotId
from ..models.playlists_followers_request import PlaylistsFollowersRequest, PlaylistsFollowersRequestDict
from ..models.playlists_request import PlaylistsRequest, PlaylistsRequestDict
from ..models.playlists_tracks_request import PlaylistsTracksRequest, PlaylistsTracksRequestDict
from ..models.playlists_tracks_request1 import PlaylistsTracksRequest1, PlaylistsTracksRequest1Dict
from ..models.playlists_tracks_request2 import PlaylistsTracksRequest2, PlaylistsTracksRequest2Dict
from ..models.users_playlists_request import UsersPlaylistsRequest, UsersPlaylistsRequestDict
from ..server.server import Server


class Playlists:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PlaylistsWithRawResponse(client, server, auth)

    def add_tracks_to_playlist(
        self,
        playlist_id: str,
        *,
        position: int | None = None,
        uris: str | None = None,
        body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Add one or more items to a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            position: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.add_tracks_to_playlist(
                playlist_id, position=position, uris=uris, body=body, request_options=request_options
            ),
        )

    def change_playlist_details(
        self,
        playlist_id: str,
        *,
        body: PlaylistsRequest | PlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Change a playlist's name and public/private state. (The user must, of course, own the playlist.)

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playlist updated

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.change_playlist_details(playlist_id, body=body, request_options=request_options)
        )

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

    def create_playlist(
        self,
        user_id: str,
        *,
        body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistObject:
        """Create a playlist for a Spotify user. (The playlist will be empty until you `add tracks
        <https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist>`__.) Each user is
        generally limited to a maximum of 11000 playlists.

        Args:
            user_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.create_playlist(user_id, body=body, request_options=request_options))

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

    def get_a_categories_playlists(
        self,
        category_id: str,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingFeaturedPlaylistObject:
        """Get a list of Spotify playlists tagged with a particular category.

        Args:
            category_id: Value sent with the request.
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
            self._with_raw_response.get_a_categories_playlists(
                category_id, limit=limit, offset=offset, request_options=request_options
            ),
        )

    def get_a_list_of_current_users_playlists(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingPlaylistObject:
        """Get a list of the playlists owned or followed by the current Spotify user.

        Args:
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
            self._with_raw_response.get_a_list_of_current_users_playlists(
                limit=limit, offset=offset, request_options=request_options
            ),
        )

    def get_featured_playlists(
        self,
        *,
        locale: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingFeaturedPlaylistObject:
        """Get a list of Spotify featured playlists (shown, for example, on a Spotify player's 'Browse' tab).

        Args:
            locale: Value sent with the request.
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
            self._with_raw_response.get_featured_playlists(
                locale=locale, limit=limit, offset=offset, request_options=request_options
            ),
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

    def get_playlist(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistObject:
        """Get a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_playlist(
                playlist_id,
                market=market,
                fields=fields,
                additional_types=additional_types,
                request_options=request_options,
            ),
        )

    def get_playlist_cover(
        self, playlist_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ImageObject]:
        """Get the current image associated with a specific playlist.

        Args:
            playlist_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of images

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_playlist_cover(playlist_id, request_options=request_options))

    def get_playlists_tracks(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingPlaylistTrackObject:
        """Get full details of the items of a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            additional_types: Value sent with the request.
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
            self._with_raw_response.get_playlists_tracks(
                playlist_id,
                market=market,
                fields=fields,
                limit=limit,
                offset=offset,
                additional_types=additional_types,
                request_options=request_options,
            ),
        )

    def remove_tracks_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Remove one or more items from a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.remove_tracks_playlist(playlist_id, body=body, request_options=request_options)
        )

    def reorder_or_replace_playlists_tracks(
        self,
        playlist_id: str,
        *,
        uris: str | None = None,
        body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Either reorder or replace items in a playlist depending on the request's parameters. To reorder items,
        include ``range_start``, ``insert_before``, ``range_length`` and ``snapshot_id`` in the request's body. To
        replace items, include ``uris`` as either a query parameter or in the request's body. Replacing items in a
        playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a
        playlist. <br/> **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint,
        but have different parameters. These operations can't be applied together in a single request.

        Args:
            playlist_id: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.reorder_or_replace_playlists_tracks(
                playlist_id, uris=uris, body=body, request_options=request_options
            ),
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

    def upload_custom_playlist_cover(
        self, playlist_id: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Replace the image used to represent a specific playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Image uploaded

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.upload_custom_playlist_cover(playlist_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> PlaylistsWithRawResponse:
        return self._with_raw_response


class AsyncPlaylists:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPlaylistsWithRawResponse(client, server, auth)

    async def add_tracks_to_playlist(
        self,
        playlist_id: str,
        *,
        position: int | None = None,
        uris: str | None = None,
        body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Add one or more items to a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            position: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.add_tracks_to_playlist(
                playlist_id, position=position, uris=uris, body=body, request_options=request_options
            ),
        )

    async def change_playlist_details(
        self,
        playlist_id: str,
        *,
        body: PlaylistsRequest | PlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Change a playlist's name and public/private state. (The user must, of course, own the playlist.)

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playlist updated

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.change_playlist_details(
                playlist_id, body=body, request_options=request_options
            ),
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

    async def create_playlist(
        self,
        user_id: str,
        *,
        body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistObject:
        """Create a playlist for a Spotify user. (The playlist will be empty until you `add tracks
        <https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist>`__.) Each user is
        generally limited to a maximum of 11000 playlists.

        Args:
            user_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_playlist(user_id, body=body, request_options=request_options)
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

    async def get_a_categories_playlists(
        self,
        category_id: str,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingFeaturedPlaylistObject:
        """Get a list of Spotify playlists tagged with a particular category.

        Args:
            category_id: Value sent with the request.
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
            await self._with_raw_response.get_a_categories_playlists(
                category_id, limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def get_a_list_of_current_users_playlists(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingPlaylistObject:
        """Get a list of the playlists owned or followed by the current Spotify user.

        Args:
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
            await self._with_raw_response.get_a_list_of_current_users_playlists(
                limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def get_featured_playlists(
        self,
        *,
        locale: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingFeaturedPlaylistObject:
        """Get a list of Spotify featured playlists (shown, for example, on a Spotify player's 'Browse' tab).

        Args:
            locale: Value sent with the request.
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
            await self._with_raw_response.get_featured_playlists(
                locale=locale, limit=limit, offset=offset, request_options=request_options
            ),
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

    async def get_playlist(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistObject:
        """Get a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_playlist(
                playlist_id,
                market=market,
                fields=fields,
                additional_types=additional_types,
                request_options=request_options,
            ),
        )

    async def get_playlist_cover(
        self, playlist_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ImageObject]:
        """Get the current image associated with a specific playlist.

        Args:
            playlist_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of images

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_playlist_cover(playlist_id, request_options=request_options))

    async def get_playlists_tracks(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingPlaylistTrackObject:
        """Get full details of the items of a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            additional_types: Value sent with the request.
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
            await self._with_raw_response.get_playlists_tracks(
                playlist_id,
                market=market,
                fields=fields,
                limit=limit,
                offset=offset,
                additional_types=additional_types,
                request_options=request_options,
            ),
        )

    async def remove_tracks_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Remove one or more items from a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.remove_tracks_playlist(
                playlist_id, body=body, request_options=request_options
            ),
        )

    async def reorder_or_replace_playlists_tracks(
        self,
        playlist_id: str,
        *,
        uris: str | None = None,
        body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Either reorder or replace items in a playlist depending on the request's parameters. To reorder items,
        include ``range_start``, ``insert_before``, ``range_length`` and ``snapshot_id`` in the request's body. To
        replace items, include ``uris`` as either a query parameter or in the request's body. Replacing items in a
        playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a
        playlist. <br/> **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint,
        but have different parameters. These operations can't be applied together in a single request.

        Args:
            playlist_id: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.reorder_or_replace_playlists_tracks(
                playlist_id, uris=uris, body=body, request_options=request_options
            ),
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

    async def upload_custom_playlist_cover(
        self, playlist_id: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Replace the image used to represent a specific playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Image uploaded

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.upload_custom_playlist_cover(
                playlist_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncPlaylistsWithRawResponse:
        return self._with_raw_response


class PlaylistsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_tracks_to_playlist(
        self,
        playlist_id: str,
        *,
        position: int | None = None,
        uris: str | None = None,
        body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, AddTracksToPlaylistErrorBody]:
        """Add one or more items to a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            position: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[int | None]("position", position), param[str | None]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest | PlaylistsTracksRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistSnapshotId],
            error_mapper=add_tracks_to_playlist_error_mapper,
            request_options=request_options,
        )

    def change_playlist_details(
        self,
        playlist_id: str,
        *,
        body: PlaylistsRequest | PlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ChangePlaylistDetailsErrorBody]:
        """Change a playlist's name and public/private state. (The user must, of course, own the playlist.)

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsRequest | PlaylistsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=change_playlist_details_error_mapper,
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

    def create_playlist(
        self,
        user_id: str,
        *,
        body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistObject, CreatePlaylistErrorBody]:
        """Create a playlist for a Spotify user. (The playlist will be empty until you `add tracks
        <https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist>`__.) Each user is
        generally limited to a maximum of 11000 playlists.

        Args:
            user_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/playlists"),
            path_params=[param[str]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPlaylistsRequest | UsersPlaylistsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistObject],
            error_mapper=create_playlist_error_mapper,
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

    def get_a_categories_playlists(
        self,
        category_id: str,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingFeaturedPlaylistObject, GetACategoriesPlaylistsErrorBody]:
        """Get a list of Spotify playlists tagged with a particular category.

        Args:
            category_id: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/categories/{category_id}/playlists"),
            path_params=[param[str]("category_id", category_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingFeaturedPlaylistObject],
            error_mapper=get_a_categories_playlists_error_mapper,
            request_options=request_options,
        )

    def get_a_list_of_current_users_playlists(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingPlaylistObject, GetAListOfCurrentUsersPlaylistsErrorBody]:
        """Get a list of the playlists owned or followed by the current Spotify user.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/playlists"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingPlaylistObject],
            error_mapper=get_a_list_of_current_users_playlists_error_mapper,
            request_options=request_options,
        )

    def get_featured_playlists(
        self,
        *,
        locale: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingFeaturedPlaylistObject, GetFeaturedPlaylistsErrorBody]:
        """Get a list of Spotify featured playlists (shown, for example, on a Spotify player's 'Browse' tab).

        Args:
            locale: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/featured-playlists"),
            query_params=[
                param[str | None]("locale", locale),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingFeaturedPlaylistObject],
            error_mapper=get_featured_playlists_error_mapper,
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

    def get_playlist(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistObject, GetPlaylistErrorBody]:
        """Get a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[
                param[str | None]("market", market),
                param[str | None]("fields", fields),
                param[str | None]("additional_types", additional_types),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistObject],
            error_mapper=get_playlist_error_mapper,
            request_options=request_options,
        )

    def get_playlist_cover(
        self, playlist_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ImageObject], GetPlaylistCoverErrorBody]:
        """Get the current image associated with a specific playlist.

        Args:
            playlist_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}/images"),
            path_params=[param[str]("playlist_id", playlist_id)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[ImageObject]],
            error_mapper=get_playlist_cover_error_mapper,
            request_options=request_options,
        )

    def get_playlists_tracks(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingPlaylistTrackObject, GetPlaylistsTracksErrorBody]:
        """Get full details of the items of a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[
                param[str | None]("market", market),
                param[str | None]("fields", fields),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("additional_types", additional_types),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingPlaylistTrackObject],
            error_mapper=get_playlists_tracks_error_mapper,
            request_options=request_options,
        )

    def remove_tracks_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, RemoveTracksPlaylistErrorBody]:
        """Remove one or more items from a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistSnapshotId],
            error_mapper=remove_tracks_playlist_error_mapper,
            request_options=request_options,
        )

    def reorder_or_replace_playlists_tracks(
        self,
        playlist_id: str,
        *,
        uris: str | None = None,
        body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, ReorderOrReplacePlaylistsTracksErrorBody]:
        """Either reorder or replace items in a playlist depending on the request's parameters. To reorder items,
        include ``range_start``, ``insert_before``, ``range_length`` and ``snapshot_id`` in the request's body. To
        replace items, include ``uris`` as either a query parameter or in the request's body. Replacing items in a
        playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a
        playlist. <br/> **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint,
        but have different parameters. These operations can't be applied together in a single request.

        Args:
            playlist_id: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[str | None]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistSnapshotId],
            error_mapper=reorder_or_replace_playlists_tracks_error_mapper,
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

    def upload_custom_playlist_cover(
        self, playlist_id: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UploadCustomPlaylistCoverErrorBody]:
        """Replace the image used to represent a specific playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}/images"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=text_body[Any](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=upload_custom_playlist_cover_error_mapper,
            request_options=request_options,
        )


class AsyncPlaylistsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_tracks_to_playlist(
        self,
        playlist_id: str,
        *,
        position: int | None = None,
        uris: str | None = None,
        body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, AddTracksToPlaylistErrorBody]:
        """Add one or more items to a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            position: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[int | None]("position", position), param[str | None]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest | PlaylistsTracksRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PlaylistSnapshotId],
            error_mapper=add_tracks_to_playlist_error_mapper,
            request_options=request_options,
        )

    async def change_playlist_details(
        self,
        playlist_id: str,
        *,
        body: PlaylistsRequest | PlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ChangePlaylistDetailsErrorBody]:
        """Change a playlist's name and public/private state. (The user must, of course, own the playlist.)

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsRequest | PlaylistsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=change_playlist_details_error_mapper,
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

    async def create_playlist(
        self,
        user_id: str,
        *,
        body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistObject, CreatePlaylistErrorBody]:
        """Create a playlist for a Spotify user. (The playlist will be empty until you `add tracks
        <https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist>`__.) Each user is
        generally limited to a maximum of 11000 playlists.

        Args:
            user_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/playlists"),
            path_params=[param[str]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPlaylistsRequest | UsersPlaylistsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PlaylistObject],
            error_mapper=create_playlist_error_mapper,
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

    async def get_a_categories_playlists(
        self,
        category_id: str,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingFeaturedPlaylistObject, GetACategoriesPlaylistsErrorBody]:
        """Get a list of Spotify playlists tagged with a particular category.

        Args:
            category_id: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/categories/{category_id}/playlists"),
            path_params=[param[str]("category_id", category_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingFeaturedPlaylistObject],
            error_mapper=get_a_categories_playlists_error_mapper,
            request_options=request_options,
        )

    async def get_a_list_of_current_users_playlists(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingPlaylistObject, GetAListOfCurrentUsersPlaylistsErrorBody]:
        """Get a list of the playlists owned or followed by the current Spotify user.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/playlists"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingPlaylistObject],
            error_mapper=get_a_list_of_current_users_playlists_error_mapper,
            request_options=request_options,
        )

    async def get_featured_playlists(
        self,
        *,
        locale: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingFeaturedPlaylistObject, GetFeaturedPlaylistsErrorBody]:
        """Get a list of Spotify featured playlists (shown, for example, on a Spotify player's 'Browse' tab).

        Args:
            locale: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/featured-playlists"),
            query_params=[
                param[str | None]("locale", locale),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingFeaturedPlaylistObject],
            error_mapper=get_featured_playlists_error_mapper,
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

    async def get_playlist(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistObject, GetPlaylistErrorBody]:
        """Get a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[
                param[str | None]("market", market),
                param[str | None]("fields", fields),
                param[str | None]("additional_types", additional_types),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PlaylistObject],
            error_mapper=get_playlist_error_mapper,
            request_options=request_options,
        )

    async def get_playlist_cover(
        self, playlist_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ImageObject], GetPlaylistCoverErrorBody]:
        """Get the current image associated with a specific playlist.

        Args:
            playlist_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}/images"),
            path_params=[param[str]("playlist_id", playlist_id)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[list[ImageObject]],
            error_mapper=get_playlist_cover_error_mapper,
            request_options=request_options,
        )

    async def get_playlists_tracks(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingPlaylistTrackObject, GetPlaylistsTracksErrorBody]:
        """Get full details of the items of a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[
                param[str | None]("market", market),
                param[str | None]("fields", fields),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("additional_types", additional_types),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingPlaylistTrackObject],
            error_mapper=get_playlists_tracks_error_mapper,
            request_options=request_options,
        )

    async def remove_tracks_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, RemoveTracksPlaylistErrorBody]:
        """Remove one or more items from a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PlaylistSnapshotId],
            error_mapper=remove_tracks_playlist_error_mapper,
            request_options=request_options,
        )

    async def reorder_or_replace_playlists_tracks(
        self,
        playlist_id: str,
        *,
        uris: str | None = None,
        body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, ReorderOrReplacePlaylistsTracksErrorBody]:
        """Either reorder or replace items in a playlist depending on the request's parameters. To reorder items,
        include ``range_start``, ``insert_before``, ``range_length`` and ``snapshot_id`` in the request's body. To
        replace items, include ``uris`` as either a query parameter or in the request's body. Replacing items in a
        playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a
        playlist. <br/> **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint,
        but have different parameters. These operations can't be applied together in a single request.

        Args:
            playlist_id: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[str | None]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PlaylistSnapshotId],
            error_mapper=reorder_or_replace_playlists_tracks_error_mapper,
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

    async def upload_custom_playlist_cover(
        self, playlist_id: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UploadCustomPlaylistCoverErrorBody]:
        """Replace the image used to represent a specific playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}/images"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=text_body[Any](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=upload_custom_playlist_cover_error_mapper,
            request_options=request_options,
        )
