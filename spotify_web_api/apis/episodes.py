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
from ..errors.check_users_saved_episodes_error import (
    CheckUsersSavedEpisodesErrorBody,
    check_users_saved_episodes_error_mapper,
)
from ..errors.get_a_shows_episodes_error import GetAShowsEpisodesErrorBody, get_a_shows_episodes_error_mapper
from ..errors.get_an_episode_error import GetAnEpisodeErrorBody, get_an_episode_error_mapper
from ..errors.get_multiple_episodes_error import GetMultipleEpisodesErrorBody, get_multiple_episodes_error_mapper
from ..errors.get_users_saved_episodes_error import (
    GetUsersSavedEpisodesErrorBody,
    get_users_saved_episodes_error_mapper,
)
from ..errors.remove_episodes_user_error import RemoveEpisodesUserErrorBody, remove_episodes_user_error_mapper
from ..errors.save_episodes_user_error import SaveEpisodesUserErrorBody, save_episodes_user_error_mapper
from ..models.episode_object import EpisodeObject
from ..models.many_episodes import ManyEpisodes
from ..models.paging_saved_episode_object import PagingSavedEpisodeObject
from ..models.paging_simplified_episode_object import PagingSimplifiedEpisodeObject
from ..models.remove_episodes_request import RemoveEpisodesRequest, RemoveEpisodesRequestDict
from ..models.save_episodes_request import SaveEpisodesRequest, SaveEpisodesRequestDict
from ..server.server import Server


class Episodes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EpisodesWithRawResponse(client, server, auth)

    def check_users_saved_episodes(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
        This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or
        issues that you discover, in our `developer community forum
        <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__..

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
        return self._with_raw_response.check_users_saved_episodes(ids, request_options=request_options).unwrap()

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

    def get_an_episode(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EpisodeObject:
        """Get Spotify catalog information for a single episode identified by its unique Spotify ID.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An episode

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_an_episode(id, market=market, request_options=request_options).unwrap()

    def get_multiple_episodes(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyEpisodes:
        """Get Spotify catalog information for several episodes based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of episodes

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_multiple_episodes(
            ids, market=market, request_options=request_options
        ).unwrap()

    def get_users_saved_episodes(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedEpisodeObject:
        """Get a list of the episodes saved in the current Spotify user's library.<br/> This API endpoint is in __beta__
        and could change without warning. Please share any feedback that you have, or issues that you discover, in our
        `developer community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
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
        return self._with_raw_response.get_users_saved_episodes(
            market=market, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def remove_episodes_user(
        self,
        ids: str,
        *,
        body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more episodes from the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Episode removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.remove_episodes_user(ids, body=body, request_options=request_options).unwrap()

    def save_episodes_user(
        self,
        ids: str,
        *,
        body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more episodes to the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Episode saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.save_episodes_user(ids, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> EpisodesWithRawResponse:
        return self._with_raw_response


class AsyncEpisodes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEpisodesWithRawResponse(client, server, auth)

    async def check_users_saved_episodes(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
        This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or
        issues that you discover, in our `developer community forum
        <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__..

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
        return (await self._with_raw_response.check_users_saved_episodes(ids, request_options=request_options)).unwrap()

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

    async def get_an_episode(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EpisodeObject:
        """Get Spotify catalog information for a single episode identified by its unique Spotify ID.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An episode

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_an_episode(id, market=market, request_options=request_options)
        ).unwrap()

    async def get_multiple_episodes(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyEpisodes:
        """Get Spotify catalog information for several episodes based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of episodes

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_multiple_episodes(ids, market=market, request_options=request_options)
        ).unwrap()

    async def get_users_saved_episodes(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedEpisodeObject:
        """Get a list of the episodes saved in the current Spotify user's library.<br/> This API endpoint is in __beta__
        and could change without warning. Please share any feedback that you have, or issues that you discover, in our
        `developer community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
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
            await self._with_raw_response.get_users_saved_episodes(
                market=market, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def remove_episodes_user(
        self,
        ids: str,
        *,
        body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more episodes from the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Episode removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.remove_episodes_user(ids, body=body, request_options=request_options)
        ).unwrap()

    async def save_episodes_user(
        self,
        ids: str,
        *,
        body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more episodes to the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Episode saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.save_episodes_user(ids, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEpisodesWithRawResponse:
        return self._with_raw_response


class EpisodesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_users_saved_episodes(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedEpisodesErrorBody]:
        """Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
        This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or
        issues that you discover, in our `developer community forum
        <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__..

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/episodes/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_episodes_error_mapper,
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

    def get_an_episode(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EpisodeObject, GetAnEpisodeErrorBody]:
        """Get Spotify catalog information for a single episode identified by its unique Spotify ID.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/episodes/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[EpisodeObject],
            error_mapper=get_an_episode_error_mapper,
            request_options=request_options,
        )

    def get_multiple_episodes(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyEpisodes, GetMultipleEpisodesErrorBody]:
        """Get Spotify catalog information for several episodes based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/episodes"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyEpisodes],
            error_mapper=get_multiple_episodes_error_mapper,
            request_options=request_options,
        )

    def get_users_saved_episodes(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedEpisodeObject, GetUsersSavedEpisodesErrorBody]:
        """Get a list of the episodes saved in the current Spotify user's library.<br/> This API endpoint is in __beta__
        and could change without warning. Please share any feedback that you have, or issues that you discover, in our
        `developer community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/episodes"),
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedEpisodeObject],
            error_mapper=get_users_saved_episodes_error_mapper,
            request_options=request_options,
        )

    def remove_episodes_user(
        self,
        ids: str,
        *,
        body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveEpisodesUserErrorBody]:
        """Remove one or more episodes from the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/episodes"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveEpisodesRequest | RemoveEpisodesRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_episodes_user_error_mapper,
            request_options=request_options,
        )

    def save_episodes_user(
        self,
        ids: str,
        *,
        body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveEpisodesUserErrorBody]:
        """Save one or more episodes to the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/episodes"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveEpisodesRequest | SaveEpisodesRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_episodes_user_error_mapper,
            request_options=request_options,
        )


class AsyncEpisodesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_users_saved_episodes(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedEpisodesErrorBody]:
        """Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
        This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or
        issues that you discover, in our `developer community forum
        <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__..

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/episodes/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_episodes_error_mapper,
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

    async def get_an_episode(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EpisodeObject, GetAnEpisodeErrorBody]:
        """Get Spotify catalog information for a single episode identified by its unique Spotify ID.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/episodes/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[EpisodeObject],
            error_mapper=get_an_episode_error_mapper,
            request_options=request_options,
        )

    async def get_multiple_episodes(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyEpisodes, GetMultipleEpisodesErrorBody]:
        """Get Spotify catalog information for several episodes based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/episodes"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyEpisodes],
            error_mapper=get_multiple_episodes_error_mapper,
            request_options=request_options,
        )

    async def get_users_saved_episodes(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedEpisodeObject, GetUsersSavedEpisodesErrorBody]:
        """Get a list of the episodes saved in the current Spotify user's library.<br/> This API endpoint is in __beta__
        and could change without warning. Please share any feedback that you have, or issues that you discover, in our
        `developer community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/episodes"),
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedEpisodeObject],
            error_mapper=get_users_saved_episodes_error_mapper,
            request_options=request_options,
        )

    async def remove_episodes_user(
        self,
        ids: str,
        *,
        body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveEpisodesUserErrorBody]:
        """Remove one or more episodes from the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/episodes"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveEpisodesRequest | RemoveEpisodesRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_episodes_user_error_mapper,
            request_options=request_options,
        )

    async def save_episodes_user(
        self,
        ids: str,
        *,
        body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveEpisodesUserErrorBody]:
        """Save one or more episodes to the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/episodes"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveEpisodesRequest | SaveEpisodesRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_episodes_user_error_mapper,
            request_options=request_options,
        )
