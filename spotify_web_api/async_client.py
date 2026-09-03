from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.albums import AsyncAlbums
from .apis.artists import AsyncArtists
from .apis.audiobooks import AsyncAudiobooks
from .apis.categories_api import AsyncCategoriesApi
from .apis.chapters import AsyncChapters
from .apis.episodes import AsyncEpisodes
from .apis.genres import AsyncGenres
from .apis.library import AsyncLibrary
from .apis.markets_api import AsyncMarketsApi
from .apis.player import AsyncPlayer
from .apis.playlists import AsyncPlaylists
from .apis.search import AsyncSearch
from .apis.shows import AsyncShows
from .apis.tracks import AsyncTracks
from .apis.users import AsyncUsers
from .auth import AsyncAuthSchemes, Oauth20Scope
from .base_client import DEFAULT_TIMEOUT, BaseSpotifyWebApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AsyncAuthorizationCodeCredentials,
    AsyncAuthorizationCodeCredentialsOrDict,
    AsyncAuthorizationCodeTokenSource,
    AsyncClientCredentialsTokenSource,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncOAuth2RefreshableScheme,
    AsyncOAuth2Scheme,
    AsyncRawClient,
    AsyncRefreshableTokenSource,
    AsyncTokenSource,
    ClientCredentials,
    ClientCredentialsOrDict,
    client_secret_basic,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncSpotifyWebApiClient(BaseSpotifyWebApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        oauth_2_0: AsyncAuthorizationCodeCredentialsOrDict[Oauth20Scope] | None = None,
        oauth_2_0_token_source: (
            AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[Oauth20Scope]] | None
        ) = None,
        oauth_2_0_client_credentials: ClientCredentialsOrDict | None = None,
        oauth_2_0_client_credentials_token_source: AsyncTokenSource[ClientCredentials] | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "SpotifyWebApiClient/2024.3.3 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "2024.3.3"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            oauth_2_0=(
                AsyncOAuth2RefreshableScheme(
                    credentials=AsyncAuthorizationCodeCredentials[Oauth20Scope].coerce(oauth_2_0),
                    source=(
                        oauth_2_0_token_source
                        if oauth_2_0_token_source is not None
                        else AsyncAuthorizationCodeTokenSource[Oauth20Scope](
                            client=self._raw_client,
                            authorization_url=self._server.default("/authorize"),
                            token_url=self._server.default("/api/token"),
                            refresh_url=self._server.default("/api/token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if oauth_2_0 is not None
                else no_auth
            ),
            oauth_2_0_client_credentials=(
                AsyncOAuth2Scheme(
                    credentials=ClientCredentials.coerce(oauth_2_0_client_credentials),
                    source=(
                        oauth_2_0_client_credentials_token_source
                        if oauth_2_0_client_credentials_token_source is not None
                        else AsyncClientCredentialsTokenSource(
                            client=self._raw_client,
                            token_url=self._server.default("/api/token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if oauth_2_0_client_credentials is not None
                else no_auth
            ),
        )

    @cached_property
    def albums(self) -> AsyncAlbums:
        return AsyncAlbums(self._raw_client, self._server, self._auth)

    @cached_property
    def artists(self) -> AsyncArtists:
        return AsyncArtists(self._raw_client, self._server, self._auth)

    @cached_property
    def audiobooks(self) -> AsyncAudiobooks:
        return AsyncAudiobooks(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_api(self) -> AsyncCategoriesApi:
        return AsyncCategoriesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def chapters(self) -> AsyncChapters:
        return AsyncChapters(self._raw_client, self._server, self._auth)

    @cached_property
    def episodes(self) -> AsyncEpisodes:
        return AsyncEpisodes(self._raw_client, self._server, self._auth)

    @cached_property
    def genres(self) -> AsyncGenres:
        return AsyncGenres(self._raw_client, self._server, self._auth)

    @cached_property
    def library(self) -> AsyncLibrary:
        return AsyncLibrary(self._raw_client, self._server, self._auth)

    @cached_property
    def markets_api(self) -> AsyncMarketsApi:
        return AsyncMarketsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def player(self) -> AsyncPlayer:
        return AsyncPlayer(self._raw_client, self._server, self._auth)

    @cached_property
    def playlists(self) -> AsyncPlaylists:
        return AsyncPlaylists(self._raw_client, self._server, self._auth)

    @cached_property
    def search(self) -> AsyncSearch:
        return AsyncSearch(self._raw_client, self._server, self._auth)

    @cached_property
    def shows(self) -> AsyncShows:
        return AsyncShows(self._raw_client, self._server, self._auth)

    @cached_property
    def tracks(self) -> AsyncTracks:
        return AsyncTracks(self._raw_client, self._server, self._auth)

    @cached_property
    def users(self) -> AsyncUsers:
        return AsyncUsers(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncSpotifyWebApiClient
