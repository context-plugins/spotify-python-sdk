from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_a_categories_playlists_error import (
    GetACategoriesPlaylistsErrorBody,
    get_a_categories_playlists_error_mapper,
)
from ..errors.get_a_category_error import GetACategoryErrorBody, get_a_category_error_mapper
from ..errors.get_categories_error import GetCategoriesErrorBody, get_categories_error_mapper
from ..models.category_object import CategoryObject
from ..models.paged_categories import PagedCategories
from ..models.paging_featured_playlist_object import PagingFeaturedPlaylistObject
from ..server.server import Server


class CategoriesApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CategoriesApiWithRawResponse(client, server, auth)

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of playlists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_a_categories_playlists(
            category_id, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_a_category(
        self, category_id: str, *, locale: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CategoryObject:
        """Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

        Args:
            category_id: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A category

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_a_category(
            category_id, locale=locale, request_options=request_options
        ).unwrap()

    def get_categories(
        self,
        *,
        locale: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagedCategories:
        """Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

        Args:
            locale: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of categories

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_categories(
            locale=locale, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CategoriesApiWithRawResponse:
        return self._with_raw_response


class AsyncCategoriesApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCategoriesApiWithRawResponse(client, server, auth)

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of playlists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_a_categories_playlists(
                category_id, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def get_a_category(
        self, category_id: str, *, locale: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CategoryObject:
        """Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

        Args:
            category_id: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A category

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_a_category(category_id, locale=locale, request_options=request_options)
        ).unwrap()

    async def get_categories(
        self,
        *,
        locale: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagedCategories:
        """Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

        Args:
            locale: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of categories

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_categories(
                locale=locale, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCategoriesApiWithRawResponse:
        return self._with_raw_response


class CategoriesApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

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

    def get_a_category(
        self, category_id: str, *, locale: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoryObject, GetACategoryErrorBody]:
        """Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

        Args:
            category_id: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/categories/{category_id}"),
            path_params=[param[str]("category_id", category_id)],
            query_params=[param[str | None]("locale", locale)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[CategoryObject],
            error_mapper=get_a_category_error_mapper,
            request_options=request_options,
        )

    def get_categories(
        self,
        *,
        locale: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagedCategories, GetCategoriesErrorBody]:
        """Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

        Args:
            locale: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/categories"),
            query_params=[
                param[str | None]("locale", locale),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagedCategories],
            error_mapper=get_categories_error_mapper,
            request_options=request_options,
        )


class AsyncCategoriesApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/categories/{category_id}/playlists"),
            path_params=[param[str]("category_id", category_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingFeaturedPlaylistObject],
            error_mapper=get_a_categories_playlists_error_mapper,
            request_options=request_options,
        )

    async def get_a_category(
        self, category_id: str, *, locale: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoryObject, GetACategoryErrorBody]:
        """Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

        Args:
            category_id: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/categories/{category_id}"),
            path_params=[param[str]("category_id", category_id)],
            query_params=[param[str | None]("locale", locale)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[CategoryObject],
            error_mapper=get_a_category_error_mapper,
            request_options=request_options,
        )

    async def get_categories(
        self,
        *,
        locale: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagedCategories, GetCategoriesErrorBody]:
        """Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

        Args:
            locale: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/browse/categories"),
            query_params=[
                param[str | None]("locale", locale),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagedCategories],
            error_mapper=get_categories_error_mapper,
            request_options=request_options,
        )
