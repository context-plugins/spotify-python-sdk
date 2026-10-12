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
    json_decoder,
    param,
    unwrap,
)
from ..errors.check_users_saved_audiobooks_error import (
    CheckUsersSavedAudiobooksErrorBody,
    check_users_saved_audiobooks_error_mapper,
)
from ..errors.get_an_audiobook_error import GetAnAudiobookErrorBody, get_an_audiobook_error_mapper
from ..errors.get_audiobook_chapters_error import GetAudiobookChaptersErrorBody, get_audiobook_chapters_error_mapper
from ..errors.get_multiple_audiobooks_error import GetMultipleAudiobooksErrorBody, get_multiple_audiobooks_error_mapper
from ..errors.get_users_saved_audiobooks_error import (
    GetUsersSavedAudiobooksErrorBody,
    get_users_saved_audiobooks_error_mapper,
)
from ..errors.remove_audiobooks_user_error import RemoveAudiobooksUserErrorBody, remove_audiobooks_user_error_mapper
from ..errors.save_audiobooks_user_error import SaveAudiobooksUserErrorBody, save_audiobooks_user_error_mapper
from ..models.audiobook_object import AudiobookObject
from ..models.many_audiobooks import ManyAudiobooks
from ..models.paging_saved_audiobook_object import PagingSavedAudiobookObject
from ..models.paging_simplified_chapter_object import PagingSimplifiedChapterObject
from ..server.server import Server


class Audiobooks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AudiobooksWithRawResponse(client, server, auth)

    def check_users_saved_audiobooks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more audiobooks are already saved in the current Spotify user's library.

        Args:
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
        return unwrap(self._with_raw_response.check_users_saved_audiobooks(ids, request_options=request_options))

    def get_an_audiobook(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> AudiobookObject:
        """Get Spotify catalog information for a single audiobook. Audiobooks are only available within the US, UK,
        Canada, Ireland, New Zealand and Australia markets.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An Audiobook

        Raises:
            ApiError: The request contains malformed data in path, query parameters, or body. Bad or expired token. This
                can happen if the user revoked a token or the access token has expired. You should re-authenticate the
                user. Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately,
                re-authenticating the user won't help here. The requested resource cannot be found. The app has exceeded
                its rate limits. ``error`` is ``BadRequest1 | Unauthorized1 | Forbidden1 | NotFound1 | TooManyRequests1
                | RawError``."""
        return unwrap(self._with_raw_response.get_an_audiobook(id_, market=market, request_options=request_options))

    def get_audiobook_chapters(
        self,
        id_: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedChapterObject:
        """Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of chapters

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_audiobook_chapters(
                id_, market=market, limit=limit, offset=offset, request_options=request_options
            ),
        )

    def get_multiple_audiobooks(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyAudiobooks:
        """Get Spotify catalog information for several audiobooks identified by their Spotify IDs. Audiobooks are only
        available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of audiobooks. If one of the requested audiobooks is unavailable then you'll find a ``null`` item in
            the ``audiobooks`` array where the audiobook object would otherwise be.

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_multiple_audiobooks(ids, market=market, request_options=request_options)
        )

    def get_users_saved_audiobooks(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingSavedAudiobookObject:
        """Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of saved audiobooks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_users_saved_audiobooks(
                limit=limit, offset=offset, request_options=request_options
            ),
        )

    def remove_audiobooks_user(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove one or more audiobooks from the Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Audiobook(s) have been removed from the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.remove_audiobooks_user(ids, request_options=request_options))

    def save_audiobooks_user(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Save one or more audiobooks to the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Audiobook(s) are saved to the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.save_audiobooks_user(ids, request_options=request_options))

    @property
    def with_raw_response(self) -> AudiobooksWithRawResponse:
        return self._with_raw_response


class AsyncAudiobooks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAudiobooksWithRawResponse(client, server, auth)

    async def check_users_saved_audiobooks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more audiobooks are already saved in the current Spotify user's library.

        Args:
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
        return unwrap(await self._with_raw_response.check_users_saved_audiobooks(ids, request_options=request_options))

    async def get_an_audiobook(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> AudiobookObject:
        """Get Spotify catalog information for a single audiobook. Audiobooks are only available within the US, UK,
        Canada, Ireland, New Zealand and Australia markets.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An Audiobook

        Raises:
            ApiError: The request contains malformed data in path, query parameters, or body. Bad or expired token. This
                can happen if the user revoked a token or the access token has expired. You should re-authenticate the
                user. Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately,
                re-authenticating the user won't help here. The requested resource cannot be found. The app has exceeded
                its rate limits. ``error`` is ``BadRequest1 | Unauthorized1 | Forbidden1 | NotFound1 | TooManyRequests1
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_an_audiobook(id_, market=market, request_options=request_options)
        )

    async def get_audiobook_chapters(
        self,
        id_: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedChapterObject:
        """Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of chapters

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_audiobook_chapters(
                id_, market=market, limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def get_multiple_audiobooks(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyAudiobooks:
        """Get Spotify catalog information for several audiobooks identified by their Spotify IDs. Audiobooks are only
        available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of audiobooks. If one of the requested audiobooks is unavailable then you'll find a ``null`` item in
            the ``audiobooks`` array where the audiobook object would otherwise be.

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_multiple_audiobooks(ids, market=market, request_options=request_options)
        )

    async def get_users_saved_audiobooks(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingSavedAudiobookObject:
        """Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of saved audiobooks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_users_saved_audiobooks(
                limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def remove_audiobooks_user(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove one or more audiobooks from the Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Audiobook(s) have been removed from the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.remove_audiobooks_user(ids, request_options=request_options))

    async def save_audiobooks_user(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Save one or more audiobooks to the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Audiobook(s) are saved to the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.save_audiobooks_user(ids, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncAudiobooksWithRawResponse:
        return self._with_raw_response


class AudiobooksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_users_saved_audiobooks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedAudiobooksErrorBody]:
        """Check if one or more audiobooks are already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/audiobooks/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_audiobooks_error_mapper,
            request_options=request_options,
        )

    def get_an_audiobook(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AudiobookObject, GetAnAudiobookErrorBody]:
        """Get Spotify catalog information for a single audiobook. Audiobooks are only available within the US, UK,
        Canada, Ireland, New Zealand and Australia markets.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audiobooks/{id}"),
            path_params=[param[str]("id", id_)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[AudiobookObject],
            error_mapper=get_an_audiobook_error_mapper,
            request_options=request_options,
        )

    def get_audiobook_chapters(
        self,
        id_: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedChapterObject, GetAudiobookChaptersErrorBody]:
        """Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audiobooks/{id}/chapters"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSimplifiedChapterObject],
            error_mapper=get_audiobook_chapters_error_mapper,
            request_options=request_options,
        )

    def get_multiple_audiobooks(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyAudiobooks, GetMultipleAudiobooksErrorBody]:
        """Get Spotify catalog information for several audiobooks identified by their Spotify IDs. Audiobooks are only
        available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audiobooks"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyAudiobooks],
            error_mapper=get_multiple_audiobooks_error_mapper,
            request_options=request_options,
        )

    def get_users_saved_audiobooks(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingSavedAudiobookObject, GetUsersSavedAudiobooksErrorBody]:
        """Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedAudiobookObject],
            error_mapper=get_users_saved_audiobooks_error_mapper,
            request_options=request_options,
        )

    def remove_audiobooks_user(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveAudiobooksUserErrorBody]:
        """Remove one or more audiobooks from the Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_audiobooks_user_error_mapper,
            request_options=request_options,
        )

    def save_audiobooks_user(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SaveAudiobooksUserErrorBody]:
        """Save one or more audiobooks to the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_audiobooks_user_error_mapper,
            request_options=request_options,
        )


class AsyncAudiobooksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_users_saved_audiobooks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedAudiobooksErrorBody]:
        """Check if one or more audiobooks are already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/audiobooks/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[list[bool]],
            error_mapper=check_users_saved_audiobooks_error_mapper,
            request_options=request_options,
        )

    async def get_an_audiobook(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AudiobookObject, GetAnAudiobookErrorBody]:
        """Get Spotify catalog information for a single audiobook. Audiobooks are only available within the US, UK,
        Canada, Ireland, New Zealand and Australia markets.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audiobooks/{id}"),
            path_params=[param[str]("id", id_)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[AudiobookObject],
            error_mapper=get_an_audiobook_error_mapper,
            request_options=request_options,
        )

    async def get_audiobook_chapters(
        self,
        id_: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedChapterObject, GetAudiobookChaptersErrorBody]:
        """Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audiobooks/{id}/chapters"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingSimplifiedChapterObject],
            error_mapper=get_audiobook_chapters_error_mapper,
            request_options=request_options,
        )

    async def get_multiple_audiobooks(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyAudiobooks, GetMultipleAudiobooksErrorBody]:
        """Get Spotify catalog information for several audiobooks identified by their Spotify IDs. Audiobooks are only
        available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audiobooks"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[ManyAudiobooks],
            error_mapper=get_multiple_audiobooks_error_mapper,
            request_options=request_options,
        )

    async def get_users_saved_audiobooks(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingSavedAudiobookObject, GetUsersSavedAudiobooksErrorBody]:
        """Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingSavedAudiobookObject],
            error_mapper=get_users_saved_audiobooks_error_mapper,
            request_options=request_options,
        )

    async def remove_audiobooks_user(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveAudiobooksUserErrorBody]:
        """Remove one or more audiobooks from the Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=remove_audiobooks_user_error_mapper,
            request_options=request_options,
        )

    async def save_audiobooks_user(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SaveAudiobooksUserErrorBody]:
        """Save one or more audiobooks to the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=save_audiobooks_user_error_mapper,
            request_options=request_options,
        )
