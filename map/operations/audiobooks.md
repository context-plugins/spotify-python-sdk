<!-- Generated file — do not edit; regenerated with the SDK. -->

# Audiobooks — operations

Accessor: `client.audiobooks` · Source: `spotify_web_api/apis/audiobooks.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.audiobooks.check_users_saved_audiobooks

- **Route**: `GET /me/audiobooks/contains`
- **Auth**: `oauth_2_0`
- **Signature**: `def check_users_saved_audiobooks(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `list[bool]`
- **Returns (raw)**: `ApiResult[list[bool], CheckUsersSavedAudiobooksErrorBody]`
- **Error**: `CheckUsersSavedAudiobooksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckUsersSavedAudiobooksErrorBody` | `spotify_web_api/errors/check_users_saved_audiobooks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.audiobooks.get_an_audiobook

- **Route**: `GET /audiobooks/{id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_an_audiobook(id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `market` — query
- **Returns (parsed)**: `AudiobookObject`
- **Returns (raw)**: `ApiResult[AudiobookObject, GetAnAudiobookErrorBody]`
- **Error**: `GetAnAudiobookErrorBody` — **Case A (typed)**
- **Error arms**: `BadRequest1` [400] · `Unauthorized1` [401] · `Forbidden1` [403] · `NotFound1` [404] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AudiobookObject` | `spotify_web_api/models/audiobook_object.py` |
| `GetAnAudiobookErrorBody` | `spotify_web_api/errors/get_an_audiobook_error.py` |
| `BadRequest1` | `spotify_web_api/models/bad_request1.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `NotFound1` | `spotify_web_api/models/not_found1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.audiobooks.get_audiobook_chapters

- **Route**: `GET /audiobooks/{id}/chapters`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_audiobook_chapters(id: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `market` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingSimplifiedChapterObject`
- **Returns (raw)**: `ApiResult[PagingSimplifiedChapterObject, GetAudiobookChaptersErrorBody]`
- **Error**: `GetAudiobookChaptersErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingSimplifiedChapterObject` | `spotify_web_api/models/paging_simplified_chapter_object.py` |
| `GetAudiobookChaptersErrorBody` | `spotify_web_api/errors/get_audiobook_chapters_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.audiobooks.get_multiple_audiobooks

- **Route**: `GET /audiobooks`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_multiple_audiobooks(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `market` — query
- **Returns (parsed)**: `ManyAudiobooks`
- **Returns (raw)**: `ApiResult[ManyAudiobooks, GetMultipleAudiobooksErrorBody]`
- **Error**: `GetMultipleAudiobooksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyAudiobooks` | `spotify_web_api/models/many_audiobooks.py` |
| `GetMultipleAudiobooksErrorBody` | `spotify_web_api/errors/get_multiple_audiobooks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.audiobooks.get_users_saved_audiobooks

- **Route**: `GET /me/audiobooks`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_users_saved_audiobooks(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingSavedAudiobookObject`
- **Returns (raw)**: `ApiResult[PagingSavedAudiobookObject, GetUsersSavedAudiobooksErrorBody]`
- **Error**: `GetUsersSavedAudiobooksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingSavedAudiobookObject` | `spotify_web_api/models/paging_saved_audiobook_object.py` |
| `GetUsersSavedAudiobooksErrorBody` | `spotify_web_api/errors/get_users_saved_audiobooks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.audiobooks.remove_audiobooks_user

- **Route**: `DELETE /me/audiobooks`
- **Auth**: `oauth_2_0`
- **Signature**: `def remove_audiobooks_user(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveAudiobooksUserErrorBody]`
- **Error**: `RemoveAudiobooksUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveAudiobooksUserErrorBody` | `spotify_web_api/errors/remove_audiobooks_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.audiobooks.save_audiobooks_user

- **Route**: `PUT /me/audiobooks`
- **Auth**: `oauth_2_0`
- **Signature**: `def save_audiobooks_user(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SaveAudiobooksUserErrorBody]`
- **Error**: `SaveAudiobooksUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SaveAudiobooksUserErrorBody` | `spotify_web_api/errors/save_audiobooks_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

