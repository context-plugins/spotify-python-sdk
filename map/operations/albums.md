<!-- Generated file — do not edit; regenerated with the SDK. -->

# Albums — operations

Accessor: `client.albums` · Source: `spotify_web_api/apis/albums.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.albums.check_users_saved_albums

- **Route**: `GET /me/albums/contains`
- **Auth**: `oauth_2_0`
- **Signature**: `def check_users_saved_albums(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `list[bool]`
- **Returns (raw)**: `ApiResult[list[bool], CheckUsersSavedAlbumsErrorBody]`
- **Error**: `CheckUsersSavedAlbumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckUsersSavedAlbumsErrorBody` | `spotify_web_api/errors/check_users_saved_albums_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.albums.get_an_album

- **Route**: `GET /albums/{id}`
- **Auth**: `oauth_2_0` OR `oauth_2_0_client_credentials`
- **Signature**: `def get_an_album(id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `market` — query
- **Returns (parsed)**: `AlbumObject`
- **Returns (raw)**: `ApiResult[AlbumObject, GetAnAlbumErrorBody]`
- **Error**: `GetAnAlbumErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AlbumObject` | `spotify_web_api/models/album_object.py` |
| `GetAnAlbumErrorBody` | `spotify_web_api/errors/get_an_album_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.albums.get_an_albums_tracks

- **Route**: `GET /albums/{id}/tracks`
- **Auth**: `oauth_2_0` OR `oauth_2_0_client_credentials`
- **Signature**: `def get_an_albums_tracks(id: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `market` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingSimplifiedTrackObject`
- **Returns (raw)**: `ApiResult[PagingSimplifiedTrackObject, GetAnAlbumsTracksErrorBody]`
- **Error**: `GetAnAlbumsTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingSimplifiedTrackObject` | `spotify_web_api/models/paging_simplified_track_object.py` |
| `GetAnAlbumsTracksErrorBody` | `spotify_web_api/errors/get_an_albums_tracks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.albums.get_an_artists_albums

- **Route**: `GET /artists/{id}/albums`
- **Auth**: `oauth_2_0` OR `oauth_2_0_client_credentials`
- **Signature**: `def get_an_artists_albums(id: str, *, include_groups: str | None = None, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `include_groups` — query · `market` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingArtistDiscographyAlbumObject`
- **Returns (raw)**: `ApiResult[PagingArtistDiscographyAlbumObject, GetAnArtistsAlbumsErrorBody]`
- **Error**: `GetAnArtistsAlbumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingArtistDiscographyAlbumObject` | `spotify_web_api/models/paging_artist_discography_album_object.py` |
| `GetAnArtistsAlbumsErrorBody` | `spotify_web_api/errors/get_an_artists_albums_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.albums.get_multiple_albums

- **Route**: `GET /albums`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_multiple_albums(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `market` — query
- **Returns (parsed)**: `ManyAlbums`
- **Returns (raw)**: `ApiResult[ManyAlbums, GetMultipleAlbumsErrorBody]`
- **Error**: `GetMultipleAlbumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyAlbums` | `spotify_web_api/models/many_albums.py` |
| `GetMultipleAlbumsErrorBody` | `spotify_web_api/errors/get_multiple_albums_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.albums.get_new_releases

- **Route**: `GET /browse/new-releases`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_new_releases(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `offset` — query
- **Returns (parsed)**: `PagedAlbums`
- **Returns (raw)**: `ApiResult[PagedAlbums, GetNewReleasesErrorBody]`
- **Error**: `GetNewReleasesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagedAlbums` | `spotify_web_api/models/paged_albums.py` |
| `GetNewReleasesErrorBody` | `spotify_web_api/errors/get_new_releases_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.albums.get_users_saved_albums

- **Route**: `GET /me/albums`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_users_saved_albums(*, limit: int | None = 20, offset: int | None = 0, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `offset` — query · `market` — query
- **Returns (parsed)**: `PagingSavedAlbumObject`
- **Returns (raw)**: `ApiResult[PagingSavedAlbumObject, GetUsersSavedAlbumsErrorBody]`
- **Error**: `GetUsersSavedAlbumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingSavedAlbumObject` | `spotify_web_api/models/paging_saved_album_object.py` |
| `GetUsersSavedAlbumsErrorBody` | `spotify_web_api/errors/get_users_saved_albums_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.albums.remove_albums_user

- **Route**: `DELETE /me/albums`
- **Auth**: `oauth_2_0`
- **Signature**: `def remove_albums_user(ids: str, *, body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveAlbumsUserErrorBody]`
- **Error**: `RemoveAlbumsUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveAlbumsRequest` | `spotify_web_api/models/remove_albums_request.py` |
| `RemoveAlbumsRequestDict` | `spotify_web_api/models/remove_albums_request.py` |
| `RemoveAlbumsUserErrorBody` | `spotify_web_api/errors/remove_albums_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.albums.save_albums_user

- **Route**: `PUT /me/albums`
- **Auth**: `oauth_2_0`
- **Signature**: `def save_albums_user(ids: str, *, body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SaveAlbumsUserErrorBody]`
- **Error**: `SaveAlbumsUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SaveAlbumsRequest` | `spotify_web_api/models/save_albums_request.py` |
| `SaveAlbumsRequestDict` | `spotify_web_api/models/save_albums_request.py` |
| `SaveAlbumsUserErrorBody` | `spotify_web_api/errors/save_albums_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

