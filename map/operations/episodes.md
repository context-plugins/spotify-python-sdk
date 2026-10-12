<!-- Generated file — do not edit; regenerated with the SDK. -->

# Episodes — operations

Accessor: `client.episodes` · Source: `spotify_web_api/apis/episodes.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.episodes.check_users_saved_episodes

- **Route**: `GET /me/episodes/contains`
- **Auth**: `oauth_2_0`
- **Signature**: `def check_users_saved_episodes(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `list[bool]`
- **Returns (raw)**: `ApiResult[list[bool], CheckUsersSavedEpisodesErrorBody]`
- **Error**: `CheckUsersSavedEpisodesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckUsersSavedEpisodesErrorBody` | `spotify_web_api/errors/check_users_saved_episodes_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.episodes.get_a_shows_episodes

- **Route**: `GET /shows/{id}/episodes`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_a_shows_episodes(id_: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `market` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingSimplifiedEpisodeObject`
- **Returns (raw)**: `ApiResult[PagingSimplifiedEpisodeObject, GetAShowsEpisodesErrorBody]`
- **Error**: `GetAShowsEpisodesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingSimplifiedEpisodeObject` | `spotify_web_api/models/paging_simplified_episode_object.py` |
| `GetAShowsEpisodesErrorBody` | `spotify_web_api/errors/get_a_shows_episodes_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.episodes.get_an_episode

- **Route**: `GET /episodes/{id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_an_episode(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `market` — query
- **Returns (parsed)**: `EpisodeObject`
- **Returns (raw)**: `ApiResult[EpisodeObject, GetAnEpisodeErrorBody]`
- **Error**: `GetAnEpisodeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EpisodeObject` | `spotify_web_api/models/episode_object.py` |
| `GetAnEpisodeErrorBody` | `spotify_web_api/errors/get_an_episode_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.episodes.get_multiple_episodes

- **Route**: `GET /episodes`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_multiple_episodes(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `market` — query
- **Returns (parsed)**: `ManyEpisodes`
- **Returns (raw)**: `ApiResult[ManyEpisodes, GetMultipleEpisodesErrorBody]`
- **Error**: `GetMultipleEpisodesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyEpisodes` | `spotify_web_api/models/many_episodes.py` |
| `GetMultipleEpisodesErrorBody` | `spotify_web_api/errors/get_multiple_episodes_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.episodes.get_users_saved_episodes

- **Route**: `GET /me/episodes`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_users_saved_episodes(*, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `market` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingSavedEpisodeObject`
- **Returns (raw)**: `ApiResult[PagingSavedEpisodeObject, GetUsersSavedEpisodesErrorBody]`
- **Error**: `GetUsersSavedEpisodesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingSavedEpisodeObject` | `spotify_web_api/models/paging_saved_episode_object.py` |
| `GetUsersSavedEpisodesErrorBody` | `spotify_web_api/errors/get_users_saved_episodes_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.episodes.remove_episodes_user

- **Route**: `DELETE /me/episodes`
- **Auth**: `oauth_2_0`
- **Signature**: `def remove_episodes_user(ids: str, *, body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveEpisodesUserErrorBody]`
- **Error**: `RemoveEpisodesUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveEpisodesRequest` | `spotify_web_api/models/remove_episodes_request.py` |
| `RemoveEpisodesRequestDict` | `spotify_web_api/models/remove_episodes_request.py` |
| `RemoveEpisodesUserErrorBody` | `spotify_web_api/errors/remove_episodes_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.episodes.save_episodes_user

- **Route**: `PUT /me/episodes`
- **Auth**: `oauth_2_0`
- **Signature**: `def save_episodes_user(ids: str, *, body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SaveEpisodesUserErrorBody]`
- **Error**: `SaveEpisodesUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SaveEpisodesRequest` | `spotify_web_api/models/save_episodes_request.py` |
| `SaveEpisodesRequestDict` | `spotify_web_api/models/save_episodes_request.py` |
| `SaveEpisodesUserErrorBody` | `spotify_web_api/errors/save_episodes_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

