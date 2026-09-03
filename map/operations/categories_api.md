<!-- Generated file — do not edit; regenerated with the SDK. -->

# CategoriesApi — operations

Accessor: `client.categories_api` · Source: `spotify_web_api/apis/categories_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.categories_api.get_a_categories_playlists

- **Route**: `GET /browse/categories/{category_id}/playlists`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_a_categories_playlists(category_id: str, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category_id`
- **Params**: `category_id` — path · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingFeaturedPlaylistObject`
- **Returns (raw)**: `ApiResult[PagingFeaturedPlaylistObject, GetACategoriesPlaylistsErrorBody]`
- **Error**: `GetACategoriesPlaylistsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingFeaturedPlaylistObject` | `spotify_web_api/models/paging_featured_playlist_object.py` |
| `GetACategoriesPlaylistsErrorBody` | `spotify_web_api/errors/get_a_categories_playlists_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.categories_api.get_a_category

- **Route**: `GET /browse/categories/{category_id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_a_category(category_id: str, *, locale: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category_id`
- **Params**: `category_id` — path · `locale` — query
- **Returns (parsed)**: `CategoryObject`
- **Returns (raw)**: `ApiResult[CategoryObject, GetACategoryErrorBody]`
- **Error**: `GetACategoryErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CategoryObject` | `spotify_web_api/models/category_object.py` |
| `GetACategoryErrorBody` | `spotify_web_api/errors/get_a_category_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.categories_api.get_categories

- **Route**: `GET /browse/categories`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_categories(*, locale: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `locale` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagedCategories`
- **Returns (raw)**: `ApiResult[PagedCategories, GetCategoriesErrorBody]`
- **Error**: `GetCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagedCategories` | `spotify_web_api/models/paged_categories.py` |
| `GetCategoriesErrorBody` | `spotify_web_api/errors/get_categories_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

