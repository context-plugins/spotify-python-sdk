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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.check_users_saved_albums_error import (
    CheckUsersSavedAlbumsErrorBody,
    check_users_saved_albums_error_mapper,
)
from ..errors.get_an_album_error import GetAnAlbumErrorBody, get_an_album_error_mapper
from ..errors.get_an_albums_tracks_error import GetAnAlbumsTracksErrorBody, get_an_albums_tracks_error_mapper
from ..errors.get_an_artists_albums_error import GetAnArtistsAlbumsErrorBody, get_an_artists_albums_error_mapper
from ..errors.get_multiple_albums_error import GetMultipleAlbumsErrorBody, get_multiple_albums_error_mapper
from ..errors.get_new_releases_error import GetNewReleasesErrorBody, get_new_releases_error_mapper
from ..errors.get_users_saved_albums_error import GetUsersSavedAlbumsErrorBody, get_users_saved_albums_error_mapper
from ..errors.remove_albums_user_error import RemoveAlbumsUserErrorBody, remove_albums_user_error_mapper
from ..errors.save_albums_user_error import SaveAlbumsUserErrorBody, save_albums_user_error_mapper
from ..models.album_object import AlbumObject
from ..models.many_albums import ManyAlbums
from ..models.paged_albums import PagedAlbums
from ..models.paging_artist_discography_album_object import PagingArtistDiscographyAlbumObject
from ..models.paging_saved_album_object import PagingSavedAlbumObject
from ..models.paging_simplified_track_object import PagingSimplifiedTrackObject
from ..models.remove_albums_request import RemoveAlbumsRequest, RemoveAlbumsRequestDict
from ..models.save_albums_request import SaveAlbumsRequest, SaveAlbumsRequestDict
from ..server.server import Server


class Albums:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AlbumsWithRawResponse(client, server, auth)

    def check_users_saved_albums(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]:
        """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.check_users_saved_albums(ids, request_options=request_options).unwrap()

    def get_an_album(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> AlbumObject:
        """Get Spotify catalog information for a single album.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An album

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_an_album(id, market=market, request_options=request_options).unwrap()

    def get_an_albums_tracks(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedTrackObject:
        """Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number
        of tracks returned.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_an_albums_tracks(
            id, market=market, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_an_artists_albums(
        self,
        id: str,
        *,
        include_groups: str | None = None,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingArtistDiscographyAlbumObject:
        """Get Spotify catalog information about an artist's albums.

        Args:
            id: Value sent with the request.
            include_groups: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_an_artists_albums(
            id,
            include_groups=include_groups,
            market=market,
            limit=limit,
            offset=offset,
            request_options=request_options,
        ).unwrap()

    def get_multiple_albums(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyAlbums:
        """Get Spotify catalog information for multiple albums identified by their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_multiple_albums(ids, market=market, request_options=request_options).unwrap()

    def get_new_releases(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagedAlbums:
        """Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse”
        tab).

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_new_releases(
            limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_users_saved_albums(
        self,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        market: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedAlbumObject:
        """Get a list of the albums saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_users_saved_albums(
            limit=limit, offset=offset, market=market, request_options=request_options
        ).unwrap()

    def remove_albums_user(
        self,
        ids: str,
        *,
        body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more albums from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Album(s) have been removed from the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.remove_albums_user(ids, body=body, request_options=request_options).unwrap()

    def save_albums_user(
        self,
        ids: str,
        *,
        body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more albums to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The album is saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.save_albums_user(ids, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AlbumsWithRawResponse:
        return self._with_raw_response


class AsyncAlbums:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAlbumsWithRawResponse(client, server, auth)

    async def check_users_saved_albums(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.check_users_saved_albums(ids, request_options=request_options)).unwrap()

    async def get_an_album(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> AlbumObject:
        """Get Spotify catalog information for a single album.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An album

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.get_an_album(id, market=market, request_options=request_options)).unwrap()

    async def get_an_albums_tracks(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedTrackObject:
        """Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number
        of tracks returned.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_an_albums_tracks(
                id, market=market, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def get_an_artists_albums(
        self,
        id: str,
        *,
        include_groups: str | None = None,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingArtistDiscographyAlbumObject:
        """Get Spotify catalog information about an artist's albums.

        Args:
            id: Value sent with the request.
            include_groups: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_an_artists_albums(
                id,
                include_groups=include_groups,
                market=market,
                limit=limit,
                offset=offset,
                request_options=request_options,
            )
        ).unwrap()

    async def get_multiple_albums(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyAlbums:
        """Get Spotify catalog information for multiple albums identified by their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_multiple_albums(ids, market=market, request_options=request_options)
        ).unwrap()

    async def get_new_releases(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagedAlbums:
        """Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse”
        tab).

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_new_releases(limit=limit, offset=offset, request_options=request_options)
        ).unwrap()

    async def get_users_saved_albums(
        self,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        market: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedAlbumObject:
        """Get a list of the albums saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_users_saved_albums(
                limit=limit, offset=offset, market=market, request_options=request_options
            )
        ).unwrap()

    async def remove_albums_user(
        self,
        ids: str,
        *,
        body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more albums from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Album(s) have been removed from the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.remove_albums_user(ids, body=body, request_options=request_options)
        ).unwrap()

    async def save_albums_user(
        self,
        ids: str,
        *,
        body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more albums to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The album is saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.save_albums_user(ids, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAlbumsWithRawResponse:
        return self._with_raw_response


class AlbumsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_users_saved_albums(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedAlbumsErrorBody]:
        """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_albums_error_mapper,
            request_options=request_options,
        )

    def get_an_album(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AlbumObject, GetAnAlbumErrorBody]:
        """Get Spotify catalog information for a single album.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=AnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[AlbumObject],
            error_mapper=get_an_album_error_mapper,
            request_options=request_options,
        )

    def get_an_albums_tracks(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedTrackObject, GetAnAlbumsTracksErrorBody]:
        """Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number
        of tracks returned.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{id}/tracks"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=AnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[PagingSimplifiedTrackObject],
            error_mapper=get_an_albums_tracks_error_mapper,
            request_options=request_options,
        )

    def get_an_artists_albums(
        self,
        id: str,
        *,
        include_groups: str | None = None,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingArtistDiscographyAlbumObject, GetAnArtistsAlbumsErrorBody]:
        """Get Spotify catalog information about an artist's albums.

        Args:
            id: Value sent with the request.
            include_groups: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/albums"),
            path_params=[param[str]("id", id)],
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

    def get_multiple_albums(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyAlbums, GetMultipleAlbumsErrorBody]:
        """Get Spotify catalog information for multiple albums identified by their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyAlbums],
            error_mapper=get_multiple_albums_error_mapper,
            request_options=request_options,
        )

    def get_new_releases(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagedAlbums, GetNewReleasesErrorBody]:
        """Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse”
        tab).

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/new-releases"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagedAlbums],
            error_mapper=get_new_releases_error_mapper,
            request_options=request_options,
        )

    def get_users_saved_albums(
        self,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        market: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedAlbumObject, GetUsersSavedAlbumsErrorBody]:
        """Get a list of the albums saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums"),
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("market", market),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedAlbumObject],
            error_mapper=get_users_saved_albums_error_mapper,
            request_options=request_options,
        )

    def remove_albums_user(
        self,
        ids: str,
        *,
        body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveAlbumsUserErrorBody]:
        """Remove one or more albums from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/albums"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveAlbumsRequest | RemoveAlbumsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_albums_user_error_mapper,
            request_options=request_options,
        )

    def save_albums_user(
        self,
        ids: str,
        *,
        body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveAlbumsUserErrorBody]:
        """Save one or more albums to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/albums"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveAlbumsRequest | SaveAlbumsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_albums_user_error_mapper,
            request_options=request_options,
        )


class AsyncAlbumsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_users_saved_albums(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedAlbumsErrorBody]:
        """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_albums_error_mapper,
            request_options=request_options,
        )

    async def get_an_album(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AlbumObject, GetAnAlbumErrorBody]:
        """Get Spotify catalog information for a single album.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=AsyncAnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[AlbumObject],
            error_mapper=get_an_album_error_mapper,
            request_options=request_options,
        )

    async def get_an_albums_tracks(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedTrackObject, GetAnAlbumsTracksErrorBody]:
        """Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number
        of tracks returned.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{id}/tracks"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[PagingSimplifiedTrackObject],
            error_mapper=get_an_albums_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_an_artists_albums(
        self,
        id: str,
        *,
        include_groups: str | None = None,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingArtistDiscographyAlbumObject, GetAnArtistsAlbumsErrorBody]:
        """Get Spotify catalog information about an artist's albums.

        Args:
            id: Value sent with the request.
            include_groups: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/albums"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str | None]("include_groups", include_groups),
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[PagingArtistDiscographyAlbumObject],
            error_mapper=get_an_artists_albums_error_mapper,
            request_options=request_options,
        )

    async def get_multiple_albums(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyAlbums, GetMultipleAlbumsErrorBody]:
        """Get Spotify catalog information for multiple albums identified by their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyAlbums],
            error_mapper=get_multiple_albums_error_mapper,
            request_options=request_options,
        )

    async def get_new_releases(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagedAlbums, GetNewReleasesErrorBody]:
        """Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse”
        tab).

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/new-releases"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagedAlbums],
            error_mapper=get_new_releases_error_mapper,
            request_options=request_options,
        )

    async def get_users_saved_albums(
        self,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        market: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedAlbumObject, GetUsersSavedAlbumsErrorBody]:
        """Get a list of the albums saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums"),
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("market", market),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedAlbumObject],
            error_mapper=get_users_saved_albums_error_mapper,
            request_options=request_options,
        )

    async def remove_albums_user(
        self,
        ids: str,
        *,
        body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveAlbumsUserErrorBody]:
        """Remove one or more albums from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/albums"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveAlbumsRequest | RemoveAlbumsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_albums_user_error_mapper,
            request_options=request_options,
        )

    async def save_albums_user(
        self,
        ids: str,
        *,
        body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveAlbumsUserErrorBody]:
        """Save one or more albums to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/albums"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveAlbumsRequest | SaveAlbumsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_albums_user_error_mapper,
            request_options=request_options,
        )
