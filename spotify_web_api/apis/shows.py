from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.check_users_saved_shows_error import CheckUsersSavedShowsErrorBody, check_users_saved_shows_error_mapper
from ..errors.get_a_show_error import GetAShowErrorBody, get_a_show_error_mapper
from ..errors.get_a_shows_episodes_error import GetAShowsEpisodesErrorBody, get_a_shows_episodes_error_mapper
from ..errors.get_multiple_shows_error import GetMultipleShowsErrorBody, get_multiple_shows_error_mapper
from ..errors.get_users_saved_shows_error import GetUsersSavedShowsErrorBody, get_users_saved_shows_error_mapper
from ..errors.remove_shows_user_error import RemoveShowsUserErrorBody, remove_shows_user_error_mapper
from ..errors.save_shows_user_error import SaveShowsUserErrorBody, save_shows_user_error_mapper
from ..models.many_simplified_shows import ManySimplifiedShows
from ..models.paging_saved_show_object import PagingSavedShowObject
from ..models.paging_simplified_episode_object import PagingSimplifiedEpisodeObject
from ..models.remove_shows_request import RemoveShowsRequest, RemoveShowsRequestDict
from ..models.save_shows_request import SaveShowsRequest, SaveShowsRequestDict
from ..models.show_object import ShowObject
from ..server.server import Server


class Shows:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ShowsWithRawResponse(client, server, auth)

    def check_users_saved_shows(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]:
        """Check if one or more shows is already saved in the current Spotify user's library.

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
        return self._with_raw_response.check_users_saved_shows(ids, request_options=request_options).unwrap()

    def get_a_show(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ShowObject:
        """Get Spotify catalog information for a single show identified by its unique Spotify ID.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A show

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_a_show(id, market=market, request_options=request_options).unwrap()

    def get_a_shows_episodes(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedEpisodeObject:
        """Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number
        of episodes returned.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of episodes

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_a_shows_episodes(
            id, market=market, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_multiple_shows(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManySimplifiedShows:
        """Get Spotify catalog information for several shows based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of shows

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_multiple_shows(ids, market=market, request_options=request_options).unwrap()

    def get_users_saved_shows(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingSavedShowObject:
        """Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the
        number of shows returned.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of shows

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_users_saved_shows(
            limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def remove_shows_user(
        self,
        ids: str,
        *,
        market: str | None = None,
        body: RemoveShowsRequest | RemoveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete one or more shows from current Spotify user's library.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Show removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.remove_shows_user(
            ids, market=market, body=body, request_options=request_options
        ).unwrap()

    def save_shows_user(
        self,
        ids: str,
        *,
        body: SaveShowsRequest | SaveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more shows to current Spotify user's library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Show saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.save_shows_user(ids, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ShowsWithRawResponse:
        return self._with_raw_response


class AsyncShows:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncShowsWithRawResponse(client, server, auth)

    async def check_users_saved_shows(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more shows is already saved in the current Spotify user's library.

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
        return (await self._with_raw_response.check_users_saved_shows(ids, request_options=request_options)).unwrap()

    async def get_a_show(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ShowObject:
        """Get Spotify catalog information for a single show identified by its unique Spotify ID.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A show

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.get_a_show(id, market=market, request_options=request_options)).unwrap()

    async def get_a_shows_episodes(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedEpisodeObject:
        """Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number
        of episodes returned.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of episodes

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_a_shows_episodes(
                id, market=market, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def get_multiple_shows(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManySimplifiedShows:
        """Get Spotify catalog information for several shows based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of shows

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_multiple_shows(ids, market=market, request_options=request_options)
        ).unwrap()

    async def get_users_saved_shows(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingSavedShowObject:
        """Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the
        number of shows returned.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of shows

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_users_saved_shows(
                limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def remove_shows_user(
        self,
        ids: str,
        *,
        market: str | None = None,
        body: RemoveShowsRequest | RemoveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete one or more shows from current Spotify user's library.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Show removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.remove_shows_user(
                ids, market=market, body=body, request_options=request_options
            )
        ).unwrap()

    async def save_shows_user(
        self,
        ids: str,
        *,
        body: SaveShowsRequest | SaveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more shows to current Spotify user's library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Show saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.save_shows_user(ids, body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncShowsWithRawResponse:
        return self._with_raw_response


class ShowsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_users_saved_shows(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedShowsErrorBody]:
        """Check if one or more shows is already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/shows/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_shows_error_mapper,
            request_options=request_options,
        )

    def get_a_show(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ShowObject, GetAShowErrorBody]:
        """Get Spotify catalog information for a single show identified by its unique Spotify ID.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/shows/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ShowObject],
            error_mapper=get_a_show_error_mapper,
            request_options=request_options,
        )

    def get_a_shows_episodes(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedEpisodeObject, GetAShowsEpisodesErrorBody]:
        """Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number
        of episodes returned.

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
            url_template=self._server.default("/shows/{id}/episodes"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSimplifiedEpisodeObject],
            error_mapper=get_a_shows_episodes_error_mapper,
            request_options=request_options,
        )

    def get_multiple_shows(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManySimplifiedShows, GetMultipleShowsErrorBody]:
        """Get Spotify catalog information for several shows based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/shows"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManySimplifiedShows],
            error_mapper=get_multiple_shows_error_mapper,
            request_options=request_options,
        )

    def get_users_saved_shows(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingSavedShowObject, GetUsersSavedShowsErrorBody]:
        """Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the
        number of shows returned.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/shows"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedShowObject],
            error_mapper=get_users_saved_shows_error_mapper,
            request_options=request_options,
        )

    def remove_shows_user(
        self,
        ids: str,
        *,
        market: str | None = None,
        body: RemoveShowsRequest | RemoveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveShowsUserErrorBody]:
        """Delete one or more shows from current Spotify user's library.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/shows"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveShowsRequest | RemoveShowsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_shows_user_error_mapper,
            request_options=request_options,
        )

    def save_shows_user(
        self,
        ids: str,
        *,
        body: SaveShowsRequest | SaveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveShowsUserErrorBody]:
        """Save one or more shows to current Spotify user's library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/shows"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveShowsRequest | SaveShowsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_shows_user_error_mapper,
            request_options=request_options,
        )


class AsyncShowsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_users_saved_shows(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedShowsErrorBody]:
        """Check if one or more shows is already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/shows/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_shows_error_mapper,
            request_options=request_options,
        )

    async def get_a_show(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ShowObject, GetAShowErrorBody]:
        """Get Spotify catalog information for a single show identified by its unique Spotify ID.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/shows/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ShowObject],
            error_mapper=get_a_show_error_mapper,
            request_options=request_options,
        )

    async def get_a_shows_episodes(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedEpisodeObject, GetAShowsEpisodesErrorBody]:
        """Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number
        of episodes returned.

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
            url_template=self._server.default("/shows/{id}/episodes"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSimplifiedEpisodeObject],
            error_mapper=get_a_shows_episodes_error_mapper,
            request_options=request_options,
        )

    async def get_multiple_shows(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManySimplifiedShows, GetMultipleShowsErrorBody]:
        """Get Spotify catalog information for several shows based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/shows"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManySimplifiedShows],
            error_mapper=get_multiple_shows_error_mapper,
            request_options=request_options,
        )

    async def get_users_saved_shows(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingSavedShowObject, GetUsersSavedShowsErrorBody]:
        """Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the
        number of shows returned.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/shows"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedShowObject],
            error_mapper=get_users_saved_shows_error_mapper,
            request_options=request_options,
        )

    async def remove_shows_user(
        self,
        ids: str,
        *,
        market: str | None = None,
        body: RemoveShowsRequest | RemoveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveShowsUserErrorBody]:
        """Delete one or more shows from current Spotify user's library.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/shows"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveShowsRequest | RemoveShowsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_shows_user_error_mapper,
            request_options=request_options,
        )

    async def save_shows_user(
        self,
        ids: str,
        *,
        body: SaveShowsRequest | SaveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveShowsUserErrorBody]:
        """Save one or more shows to current Spotify user's library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/shows"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveShowsRequest | SaveShowsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_shows_user_error_mapper,
            request_options=request_options,
        )
