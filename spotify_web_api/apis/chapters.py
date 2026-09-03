from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_a_chapter_error import GetAChapterErrorBody, get_a_chapter_error_mapper
from ..errors.get_audiobook_chapters_error import GetAudiobookChaptersErrorBody, get_audiobook_chapters_error_mapper
from ..errors.get_several_chapters_error import GetSeveralChaptersErrorBody, get_several_chapters_error_mapper
from ..models.chapter_object import ChapterObject
from ..models.many_chapters import ManyChapters
from ..models.paging_simplified_chapter_object import PagingSimplifiedChapterObject
from ..server.server import Server


class Chapters:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChaptersWithRawResponse(client, server, auth)

    def get_a_chapter(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ChapterObject:
        """Get Spotify catalog information for a single audiobook chapter. Chapters are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A Chapter

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_a_chapter(id, market=market, request_options=request_options).unwrap()

    def get_audiobook_chapters(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedChapterObject:
        """Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of chapters

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_audiobook_chapters(
            id, market=market, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_several_chapters(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyChapters:
        """Get Spotify catalog information for several audiobook chapters identified by their Spotify IDs. Chapters are
        only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of chapters

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_several_chapters(
            ids, market=market, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ChaptersWithRawResponse:
        return self._with_raw_response


class AsyncChapters:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChaptersWithRawResponse(client, server, auth)

    async def get_a_chapter(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ChapterObject:
        """Get Spotify catalog information for a single audiobook chapter. Chapters are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A Chapter

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_a_chapter(id, market=market, request_options=request_options)
        ).unwrap()

    async def get_audiobook_chapters(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedChapterObject:
        """Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of chapters

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_audiobook_chapters(
                id, market=market, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def get_several_chapters(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyChapters:
        """Get Spotify catalog information for several audiobook chapters identified by their Spotify IDs. Chapters are
        only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A set of chapters

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_several_chapters(ids, market=market, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncChaptersWithRawResponse:
        return self._with_raw_response


class ChaptersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_a_chapter(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChapterObject, GetAChapterErrorBody]:
        """Get Spotify catalog information for a single audiobook chapter. Chapters are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/chapters/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ChapterObject],
            error_mapper=get_a_chapter_error_mapper,
            request_options=request_options,
        )

    def get_audiobook_chapters(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedChapterObject, GetAudiobookChaptersErrorBody]:
        """Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

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
            url_template=self._server.default("/audiobooks/{id}/chapters"),
            path_params=[param[str]("id", id)],
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

    def get_several_chapters(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyChapters, GetSeveralChaptersErrorBody]:
        """Get Spotify catalog information for several audiobook chapters identified by their Spotify IDs. Chapters are
        only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/chapters"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyChapters],
            error_mapper=get_several_chapters_error_mapper,
            request_options=request_options,
        )


class AsyncChaptersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_a_chapter(
        self, id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChapterObject, GetAChapterErrorBody]:
        """Get Spotify catalog information for a single audiobook chapter. Chapters are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            id: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/chapters/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ChapterObject],
            error_mapper=get_a_chapter_error_mapper,
            request_options=request_options,
        )

    async def get_audiobook_chapters(
        self,
        id: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedChapterObject, GetAudiobookChaptersErrorBody]:
        """Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US,
        UK, Canada, Ireland, New Zealand and Australia markets.

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
            url_template=self._server.default("/audiobooks/{id}/chapters"),
            path_params=[param[str]("id", id)],
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

    async def get_several_chapters(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyChapters, GetSeveralChaptersErrorBody]:
        """Get Spotify catalog information for several audiobook chapters identified by their Spotify IDs. Chapters are
        only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/chapters"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyChapters],
            error_mapper=get_several_chapters_error_mapper,
            request_options=request_options,
        )
