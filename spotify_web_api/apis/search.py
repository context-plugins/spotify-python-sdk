from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.search_error import SearchErrorBody, search_error_mapper
from ..models.enums.include_external import IncludeExternalOrStr
from ..models.enums.itemtype import ItemtypeOrStr
from ..models.search_items import SearchItems
from ..server.server import Server


class Search:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SearchWithRawResponse(client, server, auth)

    def search(
        self,
        q: str,
        type_: list[ItemtypeOrStr],
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        include_external: IncludeExternalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchItems:
        """Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks that
        match a keyword string. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and
        Australia markets.

        Args:
            q: Value sent with the request.
            type_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            include_external: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Search response

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.search(
                q,
                type_,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SearchWithRawResponse:
        return self._with_raw_response


class AsyncSearch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSearchWithRawResponse(client, server, auth)

    async def search(
        self,
        q: str,
        type_: list[ItemtypeOrStr],
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        include_external: IncludeExternalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchItems:
        """Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks that
        match a keyword string. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and
        Australia markets.

        Args:
            q: Value sent with the request.
            type_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            include_external: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Search response

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.search(
                q,
                type_,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSearchWithRawResponse:
        return self._with_raw_response


class SearchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def search(
        self,
        q: str,
        type_: list[ItemtypeOrStr],
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        include_external: IncludeExternalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchItems, SearchErrorBody]:
        """Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks that
        match a keyword string. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and
        Australia markets.

        Args:
            q: Value sent with the request.
            type_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            include_external: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search"),
            query_params=[
                param[str]("q", q),
                param[list[ItemtypeOrStr]]("type", type_),
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[IncludeExternalOrStr | None]("include_external", include_external),
            ],
            auth_scheme=AnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[SearchItems],
            error_mapper=search_error_mapper,
            request_options=request_options,
        )


class AsyncSearchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def search(
        self,
        q: str,
        type_: list[ItemtypeOrStr],
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        include_external: IncludeExternalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchItems, SearchErrorBody]:
        """Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks that
        match a keyword string. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and
        Australia markets.

        Args:
            q: Value sent with the request.
            type_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            include_external: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search"),
            query_params=[
                param[str]("q", q),
                param[list[ItemtypeOrStr]]("type", type_),
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[IncludeExternalOrStr | None]("include_external", include_external),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=async_json_decoder[SearchItems],
            error_mapper=search_error_mapper,
            request_options=request_options,
        )
