from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder
from ..errors.get_available_markets_error import GetAvailableMarketsErrorBody, get_available_markets_error_mapper
from ..models.markets import Markets
from ..server.server import Server


class MarketsApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MarketsApiWithRawResponse(client, server, auth)

    def get_available_markets(self, *, request_options: RequestOptionsOrDict | None = None) -> Markets:
        """Get the list of markets where Spotify is available.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A markets object with an array of country codes

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_available_markets(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MarketsApiWithRawResponse:
        return self._with_raw_response


class AsyncMarketsApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMarketsApiWithRawResponse(client, server, auth)

    async def get_available_markets(self, *, request_options: RequestOptionsOrDict | None = None) -> Markets:
        """Get the list of markets where Spotify is available.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A markets object with an array of country codes

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.get_available_markets(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncMarketsApiWithRawResponse:
        return self._with_raw_response


class MarketsApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_available_markets(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Markets, GetAvailableMarketsErrorBody]:
        """Get the list of markets where Spotify is available.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/markets"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[Markets],
            error_mapper=get_available_markets_error_mapper,
            request_options=request_options,
        )


class AsyncMarketsApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_available_markets(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Markets, GetAvailableMarketsErrorBody]:
        """Get the list of markets where Spotify is available.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/markets"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[Markets],
            error_mapper=get_available_markets_error_mapper,
            request_options=request_options,
        )
