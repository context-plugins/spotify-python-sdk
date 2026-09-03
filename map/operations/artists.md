<!-- Generated file — do not edit; regenerated with the SDK. -->

# Artists — operations

Accessor: `client.artists` · Source: `spotify_web_api/apis/artists.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.artists.check_current_user_follows

- **Route**: `GET /me/following/contains`
- **Auth**: `oauth_2_0`
- **Signature**: `def check_current_user_follows(type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `ids`
- **Params**: `type_` — query `type` · `ids` — query
- **Returns (parsed)**: `list[bool]`
- **Returns (raw)**: `ApiResult[list[bool], CheckCurrentUserFollowsErrorBody]`
- **Error**: `CheckCurrentUserFollowsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ItemType3OrStr` | `spotify_web_api/models/enums/item_type3.py` |
| `CheckCurrentUserFollowsErrorBody` | `spotify_web_api/errors/check_current_user_follows_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.artists.follow_artists_users

- **Route**: `PUT /me/following`
- **Auth**: `oauth_2_0`
- **Signature**: `def follow_artists_users(type_: ItemType2OrStr, ids: str, *, body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `ids`
- **Params**: `type_` — query `type` · `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, FollowArtistsUsersErrorBody]`
- **Error**: `FollowArtistsUsersErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ItemType2OrStr` | `spotify_web_api/models/enums/item_type2.py` |
| `FollowArtistsOrUsersRequest` | `spotify_web_api/models/follow_artists_or_users_request.py` |
| `FollowArtistsOrUsersRequestDict` | `spotify_web_api/models/follow_artists_or_users_request.py` |
| `FollowArtistsUsersErrorBody` | `spotify_web_api/errors/follow_artists_users_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.artists.get_an_artist

- **Route**: `GET /artists/{id}`
- **Auth**: `oauth_2_0` OR `oauth_2_0_client_credentials`
- **Signature**: `def get_an_artist(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `ArtistObject`
- **Returns (raw)**: `ApiResult[ArtistObject, GetAnArtistErrorBody]`
- **Error**: `GetAnArtistErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ArtistObject` | `spotify_web_api/models/artist_object.py` |
| `GetAnArtistErrorBody` | `spotify_web_api/errors/get_an_artist_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.artists.get_an_artists_albums

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

### client.artists.get_an_artists_related_artists

- **Route**: `GET /artists/{id}/related-artists`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_an_artists_related_artists(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `ManyArtists`
- **Returns (raw)**: `ApiResult[ManyArtists, GetAnArtistsRelatedArtistsErrorBody]`
- **Error**: `GetAnArtistsRelatedArtistsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyArtists` | `spotify_web_api/models/many_artists.py` |
| `GetAnArtistsRelatedArtistsErrorBody` | `spotify_web_api/errors/get_an_artists_related_artists_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.artists.get_an_artists_top_tracks

- **Route**: `GET /artists/{id}/top-tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_an_artists_top_tracks(id: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `market` — query
- **Returns (parsed)**: `ManyTracks`
- **Returns (raw)**: `ApiResult[ManyTracks, GetAnArtistsTopTracksErrorBody]`
- **Error**: `GetAnArtistsTopTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyTracks` | `spotify_web_api/models/many_tracks.py` |
| `GetAnArtistsTopTracksErrorBody` | `spotify_web_api/errors/get_an_artists_top_tracks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.artists.get_followed

- **Route**: `GET /me/following`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_followed(type_: ItemType1OrStr, *, after: str | None = None, limit: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`
- **Params**: `type_` — query `type` · `after` — query · `limit` — query
- **Returns (parsed)**: `CursorPagedArtists`
- **Returns (raw)**: `ApiResult[CursorPagedArtists, GetFollowedErrorBody]`
- **Error**: `GetFollowedErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ItemType1OrStr` | `spotify_web_api/models/enums/item_type1.py` |
| `CursorPagedArtists` | `spotify_web_api/models/cursor_paged_artists.py` |
| `GetFollowedErrorBody` | `spotify_web_api/errors/get_followed_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.artists.get_multiple_artists

- **Route**: `GET /artists`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_multiple_artists(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `ManyArtists`
- **Returns (raw)**: `ApiResult[ManyArtists, GetMultipleArtistsErrorBody]`
- **Error**: `GetMultipleArtistsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyArtists` | `spotify_web_api/models/many_artists.py` |
| `GetMultipleArtistsErrorBody` | `spotify_web_api/errors/get_multiple_artists_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.artists.get_users_top_artists

- **Route**: `GET /me/top/artists`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_users_top_artists(*, time_range: str | None = "medium_term", limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `time_range` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingArtistObject`
- **Returns (raw)**: `ApiResult[PagingArtistObject, GetUsersTopArtistsErrorBody]`
- **Error**: `GetUsersTopArtistsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingArtistObject` | `spotify_web_api/models/paging_artist_object.py` |
| `GetUsersTopArtistsErrorBody` | `spotify_web_api/errors/get_users_top_artists_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.artists.unfollow_artists_users

- **Route**: `DELETE /me/following`
- **Auth**: `oauth_2_0`
- **Signature**: `def unfollow_artists_users(type_: ItemType3OrStr, ids: str, *, body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `ids`
- **Params**: `type_` — query `type` · `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UnfollowArtistsUsersErrorBody]`
- **Error**: `UnfollowArtistsUsersErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ItemType3OrStr` | `spotify_web_api/models/enums/item_type3.py` |
| `UnfollowArtistsOrUsersRequest` | `spotify_web_api/models/unfollow_artists_or_users_request.py` |
| `UnfollowArtistsOrUsersRequestDict` | `spotify_web_api/models/unfollow_artists_or_users_request.py` |
| `UnfollowArtistsUsersErrorBody` | `spotify_web_api/errors/unfollow_artists_users_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

