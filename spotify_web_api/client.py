from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.albums import Albums
from .apis.artists import Artists
from .apis.audiobooks import Audiobooks
from .apis.categories_api import CategoriesApi
from .apis.chapters import Chapters
from .apis.episodes import Episodes
from .apis.genres import Genres
from .apis.library import Library
from .apis.markets_api import MarketsApi
from .apis.player import Player
from .apis.playlists import Playlists
from .apis.search import Search
from .apis.shows import Shows
from .apis.tracks import Tracks
from .apis.users import Users
from .auth import AuthSchemes, Oauth20Scope
from .base_client import DEFAULT_TIMEOUT, BaseSpotifyWebApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AuthorizationCodeCredentials,
    AuthorizationCodeCredentialsOrDict,
    AuthorizationCodeTokenSource,
    ClientCredentials,
    ClientCredentialsOrDict,
    ClientCredentialsTokenSource,
    HttpClient,
    Httpx2Client,
    OAuth2RefreshableScheme,
    OAuth2Scheme,
    RawClient,
    RefreshableTokenSource,
    RetryOptionsOrDict,
    TokenSource,
    client_secret_basic,
    no_auth,
    param,
)
from .server.environment import Environment


class SpotifyWebApiClient(BaseSpotifyWebApiClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        oauth_2_0: AuthorizationCodeCredentialsOrDict[Oauth20Scope] | None = None,
        oauth_2_0_token_source: RefreshableTokenSource[AuthorizationCodeCredentials[Oauth20Scope]] | None = None,
        oauth_2_0_client_credentials: ClientCredentialsOrDict | None = None,
        oauth_2_0_client_credentials_token_source: TokenSource[ClientCredentials] | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
            retry_options=self._retry_options,
            global_headers=[
                param[str]("User-Agent", "SpotifyWebApiClient/2024.3.3 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "2024.3.3"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            oauth_2_0=(
                OAuth2RefreshableScheme(
                    credentials=AuthorizationCodeCredentials[Oauth20Scope].coerce(oauth_2_0),
                    source=(
                        oauth_2_0_token_source
                        if oauth_2_0_token_source is not None
                        else AuthorizationCodeTokenSource[Oauth20Scope](
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
                OAuth2Scheme(
                    credentials=ClientCredentials.coerce(oauth_2_0_client_credentials),
                    source=(
                        oauth_2_0_client_credentials_token_source
                        if oauth_2_0_client_credentials_token_source is not None
                        else ClientCredentialsTokenSource(
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
    def albums(self) -> Albums:
        return Albums(self._raw_client, self._server, self._auth)

    @cached_property
    def artists(self) -> Artists:
        return Artists(self._raw_client, self._server, self._auth)

    @cached_property
    def audiobooks(self) -> Audiobooks:
        return Audiobooks(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_api(self) -> CategoriesApi:
        return CategoriesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def chapters(self) -> Chapters:
        return Chapters(self._raw_client, self._server, self._auth)

    @cached_property
    def episodes(self) -> Episodes:
        return Episodes(self._raw_client, self._server, self._auth)

    @cached_property
    def genres(self) -> Genres:
        return Genres(self._raw_client, self._server, self._auth)

    @cached_property
    def library(self) -> Library:
        return Library(self._raw_client, self._server, self._auth)

    @cached_property
    def markets_api(self) -> MarketsApi:
        return MarketsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def player(self) -> Player:
        return Player(self._raw_client, self._server, self._auth)

    @cached_property
    def playlists(self) -> Playlists:
        return Playlists(self._raw_client, self._server, self._auth)

    @cached_property
    def search(self) -> Search:
        return Search(self._raw_client, self._server, self._auth)

    @cached_property
    def shows(self) -> Shows:
        return Shows(self._raw_client, self._server, self._auth)

    @cached_property
    def tracks(self) -> Tracks:
        return Tracks(self._raw_client, self._server, self._auth)

    @cached_property
    def users(self) -> Users:
        return Users(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = SpotifyWebApiClient
