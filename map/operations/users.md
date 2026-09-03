<!-- Generated file — do not edit; regenerated with the SDK. -->

# Users — operations

Accessor: `client.users` · Source: `spotify_web_api/apis/users.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users.check_current_user_follows

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

### client.users.check_if_user_follows_playlist

- **Route**: `GET /playlists/{playlist_id}/followers/contains`
- **Auth**: `oauth_2_0`
- **Signature**: `def check_if_user_follows_playlist(playlist_id: str, ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`, `ids`
- **Params**: `playlist_id` — path · `ids` — query
- **Returns (parsed)**: `list[bool]`
- **Returns (raw)**: `ApiResult[list[bool], CheckIfUserFollowsPlaylistErrorBody]`
- **Error**: `CheckIfUserFollowsPlaylistErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfUserFollowsPlaylistErrorBody` | `spotify_web_api/errors/check_if_user_follows_playlist_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.users.follow_artists_users

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

### client.users.follow_playlist

- **Route**: `PUT /playlists/{playlist_id}/followers`
- **Auth**: `oauth_2_0`
- **Signature**: `def follow_playlist(playlist_id: str, *, body: PlaylistsFollowersRequest | PlaylistsFollowersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`
- **Params**: `playlist_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, FollowPlaylistErrorBody]`
- **Error**: `FollowPlaylistErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PlaylistsFollowersRequest` | `spotify_web_api/models/playlists_followers_request.py` |
| `PlaylistsFollowersRequestDict` | `spotify_web_api/models/playlists_followers_request.py` |
| `FollowPlaylistErrorBody` | `spotify_web_api/errors/follow_playlist_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.users.get_current_users_profile

- **Route**: `GET /me`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_current_users_profile(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `PrivateUserObject`
- **Returns (raw)**: `ApiResult[PrivateUserObject, GetCurrentUsersProfileErrorBody]`
- **Error**: `GetCurrentUsersProfileErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PrivateUserObject` | `spotify_web_api/models/private_user_object.py` |
| `GetCurrentUsersProfileErrorBody` | `spotify_web_api/errors/get_current_users_profile_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.users.get_followed

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

### client.users.get_list_users_playlists

- **Route**: `GET /users/{user_id}/playlists`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_list_users_playlists(user_id: str, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingPlaylistObject`
- **Returns (raw)**: `ApiResult[PagingPlaylistObject, GetListUsersPlaylistsErrorBody]`
- **Error**: `GetListUsersPlaylistsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingPlaylistObject` | `spotify_web_api/models/paging_playlist_object.py` |
| `GetListUsersPlaylistsErrorBody` | `spotify_web_api/errors/get_list_users_playlists_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.users.get_users_profile

- **Route**: `GET /users/{user_id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_users_profile(user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path
- **Returns (parsed)**: `PublicUserObject`
- **Returns (raw)**: `ApiResult[PublicUserObject, GetUsersProfileErrorBody]`
- **Error**: `GetUsersProfileErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PublicUserObject` | `spotify_web_api/models/public_user_object.py` |
| `GetUsersProfileErrorBody` | `spotify_web_api/errors/get_users_profile_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.users.get_users_top_artists

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

### client.users.get_users_top_tracks

- **Route**: `GET /me/top/tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_users_top_tracks(*, time_range: str | None = "medium_term", limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `time_range` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingTrackObject`
- **Returns (raw)**: `ApiResult[PagingTrackObject, GetUsersTopTracksErrorBody]`
- **Error**: `GetUsersTopTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingTrackObject` | `spotify_web_api/models/paging_track_object.py` |
| `GetUsersTopTracksErrorBody` | `spotify_web_api/errors/get_users_top_tracks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.users.unfollow_artists_users

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

### client.users.unfollow_playlist

- **Route**: `DELETE /playlists/{playlist_id}/followers`
- **Auth**: `oauth_2_0`
- **Signature**: `def unfollow_playlist(playlist_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`
- **Params**: `playlist_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UnfollowPlaylistErrorBody]`
- **Error**: `UnfollowPlaylistErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UnfollowPlaylistErrorBody` | `spotify_web_api/errors/unfollow_playlist_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

