from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
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
from ..errors.follow_artists_users_error import FollowArtistsUsersErrorBody, follow_artists_users_error_mapper
from ..errors.get_an_artist_error import GetAnArtistErrorBody, get_an_artist_error_mapper
from ..errors.get_an_artists_albums_error import GetAnArtistsAlbumsErrorBody, get_an_artists_albums_error_mapper
from ..errors.get_an_artists_related_artists_error import (
    GetAnArtistsRelatedArtistsErrorBody,
    get_an_artists_related_artists_error_mapper,
)
from ..errors.get_an_artists_top_tracks_error import (
    GetAnArtistsTopTracksErrorBody,
    get_an_artists_top_tracks_error_mapper,
)
from ..errors.get_followed_error import GetFollowedErrorBody, get_followed_error_mapper
from ..errors.get_multiple_artists_error import GetMultipleArtistsErrorBody, get_multiple_artists_error_mapper
from ..errors.get_users_top_artists_error import GetUsersTopArtistsErrorBody, get_users_top_artists_error_mapper
from ..errors.unfollow_artists_users_error import UnfollowArtistsUsersErrorBody, unfollow_artists_users_error_mapper
from ..models.artist_object import ArtistObject
from ..models.cursor_paged_artists import CursorPagedArtists
from ..models.enums.item_type1 import ItemType1OrStr
from ..models.enums.item_type2 import ItemType2OrStr
from ..models.enums.item_type3 import ItemType3OrStr
from ..models.follow_artists_or_users_request import FollowArtistsOrUsersRequest, FollowArtistsOrUsersRequestDict
from ..models.many_artists import ManyArtists
from ..models.many_tracks import ManyTracks
from ..models.paging_artist_discography_album_object import PagingArtistDiscographyAlbumObject
from ..models.paging_artist_object import PagingArtistObject
from ..models.unfollow_artists_or_users_request import UnfollowArtistsOrUsersRequest, UnfollowArtistsOrUsersRequestDict
from ..server.server import Server


class Artists:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ArtistsWithRawResponse(client, server, auth)

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

    def get_an_artist(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> ArtistObject:
        """Get Spotify catalog information for a single artist identified by their unique Spotify ID.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An artist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_an_artist(id_, request_options=request_options))

    def get_an_artists_albums(
        self,
        id_: str,
        *,
        include_groups: str | None = None,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingArtistDiscographyAlbumObject:
        """Get Spotify catalog information about an artist's albums.

        Args:
            id_: Value sent with the request.
            include_groups: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_an_artists_albums(
                id_,
                include_groups=include_groups,
                market=market,
                limit=limit,
                offset=offset,
                request_options=request_options,
            ),
        )

    def get_an_artists_related_artists(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManyArtists:
        """Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of
        the Spotify community's listening history.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_an_artists_related_artists(id_, request_options=request_options))

    def get_an_artists_top_tracks(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyTracks:
        """Get Spotify catalog information about an artist's top tracks by country.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_an_artists_top_tracks(id_, market=market, request_options=request_options)
        )

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

    def get_multiple_artists(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> ManyArtists:
        """Get Spotify catalog information for several artists based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_multiple_artists(ids, request_options=request_options))

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

    @property
    def with_raw_response(self) -> ArtistsWithRawResponse:
        return self._with_raw_response


class AsyncArtists:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncArtistsWithRawResponse(client, server, auth)

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

    async def get_an_artist(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> ArtistObject:
        """Get Spotify catalog information for a single artist identified by their unique Spotify ID.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An artist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_an_artist(id_, request_options=request_options))

    async def get_an_artists_albums(
        self,
        id_: str,
        *,
        include_groups: str | None = None,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingArtistDiscographyAlbumObject:
        """Get Spotify catalog information about an artist's albums.

        Args:
            id_: Value sent with the request.
            include_groups: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_an_artists_albums(
                id_,
                include_groups=include_groups,
                market=market,
                limit=limit,
                offset=offset,
                request_options=request_options,
            ),
        )

    async def get_an_artists_related_artists(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManyArtists:
        """Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of
        the Spotify community's listening history.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_an_artists_related_artists(id_, request_options=request_options)
        )

    async def get_an_artists_top_tracks(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyTracks:
        """Get Spotify catalog information about an artist's top tracks by country.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_an_artists_top_tracks(id_, market=market, request_options=request_options)
        )

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

    async def get_multiple_artists(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManyArtists:
        """Get Spotify catalog information for several artists based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_multiple_artists(ids, request_options=request_options))

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

    @property
    def with_raw_response(self) -> AsyncArtistsWithRawResponse:
        return self._with_raw_response


class ArtistsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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

    def get_an_artist(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ArtistObject, GetAnArtistErrorBody]:
        """Get Spotify catalog information for a single artist identified by their unique Spotify ID.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[ArtistObject],
            error_mapper=get_an_artist_error_mapper,
            request_options=request_options,
        )

    def get_an_artists_albums(
        self,
        id_: str,
        *,
        include_groups: str | None = None,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingArtistDiscographyAlbumObject, GetAnArtistsAlbumsErrorBody]:
        """Get Spotify catalog information about an artist's albums.

        Args:
            id_: Value sent with the request.
            include_groups: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/albums"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[str | None]("include_groups", include_groups),
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=AnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[PagingArtistDiscographyAlbumObject],
            error_mapper=get_an_artists_albums_error_mapper,
            request_options=request_options,
        )

    def get_an_artists_related_artists(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyArtists, GetAnArtistsRelatedArtistsErrorBody]:
        """Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of
        the Spotify community's listening history.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/related-artists"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyArtists],
            error_mapper=get_an_artists_related_artists_error_mapper,
            request_options=request_options,
        )

    def get_an_artists_top_tracks(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyTracks, GetAnArtistsTopTracksErrorBody]:
        """Get Spotify catalog information about an artist's top tracks by country.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/top-tracks"),
            path_params=[param[str]("id", id_)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyTracks],
            error_mapper=get_an_artists_top_tracks_error_mapper,
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

    def get_multiple_artists(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyArtists, GetMultipleArtistsErrorBody]:
        """Get Spotify catalog information for several artists based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyArtists],
            error_mapper=get_multiple_artists_error_mapper,
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


class AsyncArtistsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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

    async def get_an_artist(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ArtistObject, GetAnArtistErrorBody]:
        """Get Spotify catalog information for a single artist identified by their unique Spotify ID.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=async_json_decoder[ArtistObject],
            error_mapper=get_an_artist_error_mapper,
            request_options=request_options,
        )

    async def get_an_artists_albums(
        self,
        id_: str,
        *,
        include_groups: str | None = None,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingArtistDiscographyAlbumObject, GetAnArtistsAlbumsErrorBody]:
        """Get Spotify catalog information about an artist's albums.

        Args:
            id_: Value sent with the request.
            include_groups: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/albums"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[str | None]("include_groups", include_groups),
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=async_json_decoder[PagingArtistDiscographyAlbumObject],
            error_mapper=get_an_artists_albums_error_mapper,
            request_options=request_options,
        )

    async def get_an_artists_related_artists(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyArtists, GetAnArtistsRelatedArtistsErrorBody]:
        """Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of
        the Spotify community's listening history.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/related-artists"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[ManyArtists],
            error_mapper=get_an_artists_related_artists_error_mapper,
            request_options=request_options,
        )

    async def get_an_artists_top_tracks(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyTracks, GetAnArtistsTopTracksErrorBody]:
        """Get Spotify catalog information about an artist's top tracks by country.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/top-tracks"),
            path_params=[param[str]("id", id_)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[ManyTracks],
            error_mapper=get_an_artists_top_tracks_error_mapper,
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

    async def get_multiple_artists(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyArtists, GetMultipleArtistsErrorBody]:
        """Get Spotify catalog information for several artists based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[ManyArtists],
            error_mapper=get_multiple_artists_error_mapper,
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
