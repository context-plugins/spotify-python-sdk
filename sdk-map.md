<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Spotify Web API (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Spotify Web API |
| Root package | `spotify_web_api` |
| Distribution name | `spotify-web-api` |
| Requires | Python 3.10 or later |
| API spec version | `2024.3.3` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from spotify_web_api import SpotifyWebApiClient
from spotify_web_api.auth import Oauth20Scope
from spotify_web_api.core import AuthorizationCodeCredentials, ClientCredentials


def prompt(url: str) -> str:
    return input(f"Open {url}, then paste the code: ")


client = SpotifyWebApiClient(
    oauth_2_0=AuthorizationCodeCredentials[Oauth20Scope](
        client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
    ),
    oauth_2_0_client_credentials=ClientCredentials(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
    environment="production",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with SpotifyWebApiClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run, to_thread

from spotify_web_api import AsyncSpotifyWebApiClient
from spotify_web_api.auth import Oauth20Scope
from spotify_web_api.core import AsyncAuthorizationCodeCredentials, ClientCredentials


async def prompt(url: str) -> str:
    print(f"Open {url}")
    return await to_thread(input, "Paste the code: ")


async def main() -> None:
    client = AsyncSpotifyWebApiClient(
        oauth_2_0=AsyncAuthorizationCodeCredentials[Oauth20Scope](
            client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
        ),
        oauth_2_0_client_credentials=ClientCredentials(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
        environment="production",
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncSpotifyWebApiClient(...) as client:` closes the pool on exit.

`AsyncClient` (`spotify_web_api/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `SpotifyWebApiClient` and `AsyncSpotifyWebApiClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.albums`). Every constructor argument is optional and keyword-only. Sources: `spotify_web_api/client.py`, `spotify_web_api/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `environment` | `Environment` | `Environment` | `"production"` |
| `base_url` | `str \| None` | `str \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `retry_options` | `int \| RetryOptionsOrDict \| None` | `int \| RetryOptionsOrDict \| None` | `None` |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `oauth_2_0` | `AuthorizationCodeCredentialsOrDict[Oauth20Scope] \| None` | `AsyncAuthorizationCodeCredentialsOrDict[Oauth20Scope] \| None` | `None` |
| `oauth_2_0_token_source` | `RefreshableTokenSource[AuthorizationCodeCredentials[Oauth20Scope]] \| None` | `AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[Oauth20Scope]] \| None` | `None` |
| `oauth_2_0_client_credentials` | `ClientCredentialsOrDict \| None` | `ClientCredentialsOrDict \| None` | `None` |
| `oauth_2_0_client_credentials_token_source` | `TokenSource[ClientCredentials] \| None` | `AsyncTokenSource[ClientCredentials] \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `Environment` | `spotify_web_api.server` | `Literal` of the Environments table's names |
| `RetryOptionsOrDict` | `spotify_web_api.core` | a retry count, `RetryOptions`, or a dict: `max_retries: int` · `initial_delay: float` · `backoff_factor: float` · `max_delay: float` · `max_jitter: float` · `status_codes_to_retry: frozenset[int]` · `http_methods_to_retry: frozenset[HttpMethod]` |
| `HttpClient` | `spotify_web_api.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()`; `send` returns once the head has arrived and never reads the body, and raises `TransportError` (from `core`) when no response arrives — anything else it raises is never retried |
| `AuthorizationCodeCredentialsOrDict` | `spotify_web_api.core` | `AuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `Oauth20Scope` | `spotify_web_api.auth` | `Enum` of the declared scopes |
| `RefreshableTokenSource` | `spotify_web_api.core` | protocol — `fetch(credentials) -> OAuthTokenRefreshable` · `refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AuthorizationCodeCredentials` | `spotify_web_api.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `ClientCredentialsOrDict` | `spotify_web_api.core` | `ClientCredentials` or a dict: `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `TokenSource` | `spotify_web_api.core` | protocol — `fetch(credentials) -> OAuthToken` |
| `ClientCredentials` | `spotify_web_api.core` | `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `AsyncHttpClient` | `spotify_web_api.core` | protocol — `async send(request: HttpRequest) -> AsyncHttpResponse` · `async aclose()`; the same obligation, awaited |
| `AsyncAuthorizationCodeCredentialsOrDict` | `spotify_web_api.core` | `AsyncAuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncRefreshableTokenSource` | `spotify_web_api.core` | protocol — `async fetch(credentials) -> OAuthTokenRefreshable` · `async refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AsyncAuthorizationCodeCredentials` | `spotify_web_api.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncTokenSource` | `spotify_web_api.core` | protocol — `async fetch(credentials) -> OAuthToken` |

### Retries — on by default

`retry_options` left at `None` applies the default `RetryOptions` policy below, so an unconfigured client **retries**: a request whose method is in `http_methods_to_retry` is sent again when it gets a status in `status_codes_to_retry`, or no response at all, and the last outcome reaches you only once its retries are spent. A body that cannot be re-sent byte for byte — a streamed file upload — is never retried. `retry_options=0` (or `{"max_retries": 0}`) turns retrying off; a bare count sets `max_retries` and leaves every other field at its default.

`RetryOptions` fields (source: `spotify_web_api/core/retries.py`). Pass only the fields you change; each one left out takes its default:

| Field | Type | Default |
| --- | --- | --- |
| `max_retries` | `int` | `3` |
| `initial_delay` | `float` (seconds) | `1.0` |
| `backoff_factor` | `float` | `2.0` |
| `max_delay` | `float` (seconds) | `60.0` |
| `max_jitter` | `float` (seconds) | `0.5` |
| `status_codes_to_retry` | `frozenset[int]` | `frozenset({408, 429, 500, 502, 503, 504})` |
| `http_methods_to_retry` | `frozenset[HttpMethod]` | `frozenset({"GET", "HEAD", "PUT", "OPTIONS"})` |

The wait before retry *n* is `initial_delay × backoff_factor^(n−1)` plus up to `max_jitter` of random delay, the sum capped at `max_delay`; a `Retry-After` header replaces it, trimmed to `max_delay`.

A single call overrides two of these through `request_options` (`spotify_web_api/core/request_options.py`): `max_retries` and `status_codes_to_retry`, each merged over the client's policy field by field — `request_options={"max_retries": 0}` turns retrying off for that one call and leaves every other call alone.

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.status_code` and `.headers`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `spotify_web_api/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`spotify_web_api/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any`.

Core runtime types (`spotify_web_api/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `spotify_web_api/errors/` or `RawError` | `error: E` · `status_code: int` · `headers: Mapping[str, str]` | `spotify_web_api/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `status_code: int` · `headers: Mapping[str, str]` (both on either) | `spotify_web_api/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` | `spotify_web_api/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
try:
    response = client.albums.check_users_saved_albums(
        "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"
    )
except ApiError as e:
    # Case A — typed error: e.error is CheckUsersSavedAlbumsErrorBody
    if isinstance(e.error, Unauthorized1):
        # Handle 401
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **138 operations**, **138 are Case A (typed)** and **0 are Case B (raw)**.

---

## Operations — by controller (15 pages, 138 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every *generated* type it names, with the module that declares it. A runtime type — a file alias, a date/time or byte converter — is not listed there.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout, extra headers, `max_retries` or `status_codes_to_retry`; every signature ends with it | here (`spotify_web_api/core/request_options.py`), Retries |
| **Base URL is the selected environment's** — this SDK's only server, one URL per `environment=`; override it with `base_url="https://…"` | Servers & auth |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.albums` | 9 | [map/operations/albums.md](map/operations/albums.md) |
| `client.artists` | 10 | [map/operations/artists.md](map/operations/artists.md) |
| `client.audiobooks` | 7 | [map/operations/audiobooks.md](map/operations/audiobooks.md) |
| `client.categories_api` | 3 | [map/operations/categories_api.md](map/operations/categories_api.md) |
| `client.chapters` | 3 | [map/operations/chapters.md](map/operations/chapters.md) |
| `client.episodes` | 7 | [map/operations/episodes.md](map/operations/episodes.md) |
| `client.genres` | 1 | [map/operations/genres.md](map/operations/genres.md) |
| `client.library` | 29 | [map/operations/library.md](map/operations/library.md) |
| `client.markets_api` | 1 | [map/operations/markets_api.md](map/operations/markets_api.md) |
| `client.player` | 15 | [map/operations/player.md](map/operations/player.md) |
| `client.playlists` | 16 | [map/operations/playlists.md](map/operations/playlists.md) |
| `client.search` | 1 | [map/operations/search.md](map/operations/search.md) |
| `client.shows` | 7 | [map/operations/shows.md](map/operations/shows.md) |
| `client.tracks` | 17 | [map/operations/tracks.md](map/operations/tracks.md) |
| `client.users` | 12 | [map/operations/users.md](map/operations/users.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `spotify_web_api/models/` declares one type plus its input companion, and every module under `spotify_web_api/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`AlbumBase` ↔ `album_base.py`; an error alias drops its `Body` suffix: `AddToQueueErrorBody` ↔ `add_to_queue_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 129 | `spotify_web_api/models/` |
| Enums (`Enum` over `str` / `int`) — Python member names + wire values | 18 | `spotify_web_api/models/enums/` |
| Unions (plain) — `TypeAlias` over the arms | 4 | `spotify_web_api/models/unions/` |
| Error aliases (one per Case A operation) | 89 | `spotify_web_api/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`type_` ↔ `"type"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model, enum and union also has an **input companion**, exported beside it from the same package (`AlbumBase` ↔ `AlbumBaseDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str` / `int`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AlbumGroup` ↔ `AlbumGroupOrStr`) and additionally accepts a wire value this SDK version does not know. A union is a `TypeAlias` over its arms.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `spotify_web_api` |
| Operation controllers | `spotify_web_api.apis` |
| Models | `spotify_web_api.models` |
| Enums | `spotify_web_api.models.enums` |
| Unions | `spotify_web_api.models.unions`, `spotify_web_api.models` |
| Error aliases | `spotify_web_api.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `spotify_web_api.core` |

---

## Servers & auth

**OAuth2 (authorization code).** Pass `oauth_2_0` your client id, redirect URI and authorization code; authorization is at `/authorize` and tokens come from `/api/token`, both on the base URL — so `base_url="https://…"` moves token traffic too. Scopes are the `Oauth20Scope` alias.

**OAuth2 (client credentials).** Pass `oauth_2_0_client_credentials` your client id and secret; tokens come from `/api/token` on the base URL — so `base_url="https://…"` moves token traffic too.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**Environments.** `environment=` selects the target environment (`spotify_web_api/server/environment.py`); this SDK's one server (`spotify_web_api/server/server_config.py`) has a base URL per environment:

| Environment | Base URL | Hosting | Override point |
| --- | --- | --- | --- |
| `"production"` *(default)* | `https://api.spotify.com/v1` | — | `base_url="https://…"` |
| `"environment2"` | `https://accounts.spotify.com` | — | `base_url="https://…"` |

Pick a row with `environment=`.

