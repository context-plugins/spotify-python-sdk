<!-- Generated file — do not edit; regenerated with the SDK. -->

# Search — operations

Accessor: `client.search` · Source: `spotify_web_api/apis/search.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.search.search

- **Route**: `GET /search`
- **Auth**: `oauth_2_0` OR `oauth_2_0_client_credentials`
- **Signature**: `def search(q: str, type_: list[ItemtypeOrStr], *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, include_external: IncludeExternalOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `q`, `type_`
- **Params**: `q` — query · `type_` — query `type` · `market` — query · `limit` — query · `offset` — query · `include_external` — query
- **Returns (parsed)**: `SearchItems`
- **Returns (raw)**: `ApiResult[SearchItems, SearchErrorBody]`
- **Error**: `SearchErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ItemtypeOrStr` | `spotify_web_api/models/enums/itemtype.py` |
| `IncludeExternalOrStr` | `spotify_web_api/models/enums/include_external.py` |
| `SearchItems` | `spotify_web_api/models/search_items.py` |
| `SearchErrorBody` | `spotify_web_api/errors/search_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

