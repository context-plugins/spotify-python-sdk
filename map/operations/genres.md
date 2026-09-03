<!-- Generated file — do not edit; regenerated with the SDK. -->

# Genres — operations

Accessor: `client.genres` · Source: `spotify_web_api/apis/genres.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.genres.get_recommendation_genres

- **Route**: `GET /recommendations/available-genre-seeds`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_recommendation_genres(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ManyGenres`
- **Returns (raw)**: `ApiResult[ManyGenres, GetRecommendationGenresErrorBody]`
- **Error**: `GetRecommendationGenresErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyGenres` | `spotify_web_api/models/many_genres.py` |
| `GetRecommendationGenresErrorBody` | `spotify_web_api/errors/get_recommendation_genres_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

