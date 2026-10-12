<!-- Generated file — do not edit; regenerated with the SDK. -->

# Shows — operations

Accessor: `client.shows` · Source: `spotify_web_api/apis/shows.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.shows.check_users_saved_shows

- **Route**: `GET /me/shows/contains`
- **Auth**: `oauth_2_0`
- **Signature**: `def check_users_saved_shows(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `list[bool]`
- **Returns (raw)**: `ApiResult[list[bool], CheckUsersSavedShowsErrorBody]`
- **Error**: `CheckUsersSavedShowsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckUsersSavedShowsErrorBody` | `spotify_web_api/errors/check_users_saved_shows_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.shows.get_a_show

- **Route**: `GET /shows/{id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_a_show(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `market` — query
- **Returns (parsed)**: `ShowObject`
- **Returns (raw)**: `ApiResult[ShowObject, GetAShowErrorBody]`
- **Error**: `GetAShowErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ShowObject` | `spotify_web_api/models/show_object.py` |
| `GetAShowErrorBody` | `spotify_web_api/errors/get_a_show_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.shows.get_a_shows_episodes

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

### client.shows.get_multiple_shows

- **Route**: `GET /shows`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_multiple_shows(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `market` — query
- **Returns (parsed)**: `ManySimplifiedShows`
- **Returns (raw)**: `ApiResult[ManySimplifiedShows, GetMultipleShowsErrorBody]`
- **Error**: `GetMultipleShowsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManySimplifiedShows` | `spotify_web_api/models/many_simplified_shows.py` |
| `GetMultipleShowsErrorBody` | `spotify_web_api/errors/get_multiple_shows_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.shows.get_users_saved_shows

- **Route**: `GET /me/shows`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_users_saved_shows(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingSavedShowObject`
- **Returns (raw)**: `ApiResult[PagingSavedShowObject, GetUsersSavedShowsErrorBody]`
- **Error**: `GetUsersSavedShowsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingSavedShowObject` | `spotify_web_api/models/paging_saved_show_object.py` |
| `GetUsersSavedShowsErrorBody` | `spotify_web_api/errors/get_users_saved_shows_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.shows.remove_shows_user

- **Route**: `DELETE /me/shows`
- **Auth**: `oauth_2_0`
- **Signature**: `def remove_shows_user(ids: str, *, market: str | None = None, body: RemoveShowsRequest | RemoveShowsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `market` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveShowsUserErrorBody]`
- **Error**: `RemoveShowsUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveShowsRequest` | `spotify_web_api/models/remove_shows_request.py` |
| `RemoveShowsRequestDict` | `spotify_web_api/models/remove_shows_request.py` |
| `RemoveShowsUserErrorBody` | `spotify_web_api/errors/remove_shows_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.shows.save_shows_user

- **Route**: `PUT /me/shows`
- **Auth**: `oauth_2_0`
- **Signature**: `def save_shows_user(ids: str, *, body: SaveShowsRequest | SaveShowsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SaveShowsUserErrorBody]`
- **Error**: `SaveShowsUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SaveShowsRequest` | `spotify_web_api/models/save_shows_request.py` |
| `SaveShowsRequestDict` | `spotify_web_api/models/save_shows_request.py` |
| `SaveShowsUserErrorBody` | `spotify_web_api/errors/save_shows_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

