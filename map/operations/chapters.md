<!-- Generated file — do not edit; regenerated with the SDK. -->

# Chapters — operations

Accessor: `client.chapters` · Source: `spotify_web_api/apis/chapters.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.chapters.get_a_chapter

- **Route**: `GET /chapters/{id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_a_chapter(id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `market` — query
- **Returns (parsed)**: `ChapterObject`
- **Returns (raw)**: `ApiResult[ChapterObject, GetAChapterErrorBody]`
- **Error**: `GetAChapterErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChapterObject` | `spotify_web_api/models/chapter_object.py` |
| `GetAChapterErrorBody` | `spotify_web_api/errors/get_a_chapter_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.chapters.get_audiobook_chapters

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

### client.chapters.get_several_chapters

- **Route**: `GET /chapters`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_several_chapters(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `market` — query
- **Returns (parsed)**: `ManyChapters`
- **Returns (raw)**: `ApiResult[ManyChapters, GetSeveralChaptersErrorBody]`
- **Error**: `GetSeveralChaptersErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyChapters` | `spotify_web_api/models/many_chapters.py` |
| `GetSeveralChaptersErrorBody` | `spotify_web_api/errors/get_several_chapters_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

