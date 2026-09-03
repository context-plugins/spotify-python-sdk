from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder
from ..errors.get_recommendation_genres_error import (
    GetRecommendationGenresErrorBody,
    get_recommendation_genres_error_mapper,
)
from ..models.many_genres import ManyGenres
from ..server.server import Server


class Genres:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GenresWithRawResponse(client, server, auth)

    def get_recommendation_genres(self, *, request_options: RequestOptionsOrDict | None = None) -> ManyGenres:
        """Retrieve a list of available genres seed parameter values for `recommendations
        <https://developer.spotify.com/documentation/web-api/reference/get-recommendations>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of genres

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_recommendation_genres(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> GenresWithRawResponse:
        return self._with_raw_response


class AsyncGenres:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGenresWithRawResponse(client, server, auth)

    async def get_recommendation_genres(self, *, request_options: RequestOptionsOrDict | None = None) -> ManyGenres:
        """Retrieve a list of available genres seed parameter values for `recommendations
        <https://developer.spotify.com/documentation/web-api/reference/get-recommendations>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of genres

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.get_recommendation_genres(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncGenresWithRawResponse:
        return self._with_raw_response


class GenresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_recommendation_genres(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyGenres, GetRecommendationGenresErrorBody]:
        """Retrieve a list of available genres seed parameter values for `recommendations
        <https://developer.spotify.com/documentation/web-api/reference/get-recommendations>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/recommendations/available-genre-seeds"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyGenres],
            error_mapper=get_recommendation_genres_error_mapper,
            request_options=request_options,
        )


class AsyncGenresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_recommendation_genres(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyGenres, GetRecommendationGenresErrorBody]:
        """Retrieve a list of available genres seed parameter values for `recommendations
        <https://developer.spotify.com/documentation/web-api/reference/get-recommendations>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/recommendations/available-genre-seeds"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyGenres],
            error_mapper=get_recommendation_genres_error_mapper,
            request_options=request_options,
        )
