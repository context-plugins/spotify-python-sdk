<!-- Generated file — do not edit; regenerated with the SDK. -->

# Playlists — operations

Accessor: `client.playlists` · Source: `spotify_web_api/apis/playlists.py` · 16 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.playlists.add_tracks_to_playlist

- **Route**: `POST /playlists/{playlist_id}/tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def add_tracks_to_playlist(playlist_id: str, *, position: int | None = None, uris: str | None = None, body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`
- **Params**: `playlist_id` — path · `position` — query · `uris` — query · `body` — JSON body
- **Returns (parsed)**: `PlaylistSnapshotId`
- **Returns (raw)**: `ApiResult[PlaylistSnapshotId, AddTracksToPlaylistErrorBody]`
- **Error**: `AddTracksToPlaylistErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PlaylistsTracksRequest` | `spotify_web_api/models/playlists_tracks_request.py` |
| `PlaylistsTracksRequestDict` | `spotify_web_api/models/playlists_tracks_request.py` |
| `PlaylistSnapshotId` | `spotify_web_api/models/playlist_snapshot_id.py` |
| `AddTracksToPlaylistErrorBody` | `spotify_web_api/errors/add_tracks_to_playlist_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.change_playlist_details

- **Route**: `PUT /playlists/{playlist_id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def change_playlist_details(playlist_id: str, *, body: PlaylistsRequest | PlaylistsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`
- **Params**: `playlist_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, ChangePlaylistDetailsErrorBody]`
- **Error**: `ChangePlaylistDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PlaylistsRequest` | `spotify_web_api/models/playlists_request.py` |
| `PlaylistsRequestDict` | `spotify_web_api/models/playlists_request.py` |
| `ChangePlaylistDetailsErrorBody` | `spotify_web_api/errors/change_playlist_details_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.check_if_user_follows_playlist

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

### client.playlists.create_playlist

- **Route**: `POST /users/{user_id}/playlists`
- **Auth**: `oauth_2_0`
- **Signature**: `def create_playlist(user_id: str, *, body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `PlaylistObject`
- **Returns (raw)**: `ApiResult[PlaylistObject, CreatePlaylistErrorBody]`
- **Error**: `CreatePlaylistErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersPlaylistsRequest` | `spotify_web_api/models/users_playlists_request.py` |
| `UsersPlaylistsRequestDict` | `spotify_web_api/models/users_playlists_request.py` |
| `PlaylistObject` | `spotify_web_api/models/playlist_object.py` |
| `CreatePlaylistErrorBody` | `spotify_web_api/errors/create_playlist_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.follow_playlist

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

### client.playlists.get_a_categories_playlists

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

### client.playlists.get_a_list_of_current_users_playlists

- **Route**: `GET /me/playlists`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_a_list_of_current_users_playlists(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingPlaylistObject`
- **Returns (raw)**: `ApiResult[PagingPlaylistObject, GetAListOfCurrentUsersPlaylistsErrorBody]`
- **Error**: `GetAListOfCurrentUsersPlaylistsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingPlaylistObject` | `spotify_web_api/models/paging_playlist_object.py` |
| `GetAListOfCurrentUsersPlaylistsErrorBody` | `spotify_web_api/errors/get_a_list_of_current_users_playlists_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.get_featured_playlists

- **Route**: `GET /browse/featured-playlists`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_featured_playlists(*, locale: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `locale` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingFeaturedPlaylistObject`
- **Returns (raw)**: `ApiResult[PagingFeaturedPlaylistObject, GetFeaturedPlaylistsErrorBody]`
- **Error**: `GetFeaturedPlaylistsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingFeaturedPlaylistObject` | `spotify_web_api/models/paging_featured_playlist_object.py` |
| `GetFeaturedPlaylistsErrorBody` | `spotify_web_api/errors/get_featured_playlists_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.get_list_users_playlists

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

### client.playlists.get_playlist

- **Route**: `GET /playlists/{playlist_id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_playlist(playlist_id: str, *, market: str | None = None, fields: str | None = None, additional_types: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`
- **Params**: `playlist_id` — path · `market` — query · `fields` — query · `additional_types` — query
- **Returns (parsed)**: `PlaylistObject`
- **Returns (raw)**: `ApiResult[PlaylistObject, GetPlaylistErrorBody]`
- **Error**: `GetPlaylistErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PlaylistObject` | `spotify_web_api/models/playlist_object.py` |
| `GetPlaylistErrorBody` | `spotify_web_api/errors/get_playlist_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.get_playlist_cover

- **Route**: `GET /playlists/{playlist_id}/images`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_playlist_cover(playlist_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`
- **Params**: `playlist_id` — path
- **Returns (parsed)**: `list[ImageObject]`
- **Returns (raw)**: `ApiResult[list[ImageObject], GetPlaylistCoverErrorBody]`
- **Error**: `GetPlaylistCoverErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ImageObject` | `spotify_web_api/models/image_object.py` |
| `GetPlaylistCoverErrorBody` | `spotify_web_api/errors/get_playlist_cover_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.get_playlists_tracks

- **Route**: `GET /playlists/{playlist_id}/tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_playlists_tracks(playlist_id: str, *, market: str | None = None, fields: str | None = None, limit: int | None = 20, offset: int | None = 0, additional_types: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`
- **Params**: `playlist_id` — path · `market` — query · `fields` — query · `limit` — query · `offset` — query · `additional_types` — query
- **Returns (parsed)**: `PagingPlaylistTrackObject`
- **Returns (raw)**: `ApiResult[PagingPlaylistTrackObject, GetPlaylistsTracksErrorBody]`
- **Error**: `GetPlaylistsTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingPlaylistTrackObject` | `spotify_web_api/models/paging_playlist_track_object.py` |
| `GetPlaylistsTracksErrorBody` | `spotify_web_api/errors/get_playlists_tracks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.remove_tracks_playlist

- **Route**: `DELETE /playlists/{playlist_id}/tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def remove_tracks_playlist(playlist_id: str, *, body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`
- **Params**: `playlist_id` — path · `body` — JSON body
- **Returns (parsed)**: `PlaylistSnapshotId`
- **Returns (raw)**: `ApiResult[PlaylistSnapshotId, RemoveTracksPlaylistErrorBody]`
- **Error**: `RemoveTracksPlaylistErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PlaylistsTracksRequest2` | `spotify_web_api/models/playlists_tracks_request2.py` |
| `PlaylistsTracksRequest2Dict` | `spotify_web_api/models/playlists_tracks_request2.py` |
| `PlaylistSnapshotId` | `spotify_web_api/models/playlist_snapshot_id.py` |
| `RemoveTracksPlaylistErrorBody` | `spotify_web_api/errors/remove_tracks_playlist_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.reorder_or_replace_playlists_tracks

- **Route**: `PUT /playlists/{playlist_id}/tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def reorder_or_replace_playlists_tracks(playlist_id: str, *, uris: str | None = None, body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`
- **Params**: `playlist_id` — path · `uris` — query · `body` — JSON body
- **Returns (parsed)**: `PlaylistSnapshotId`
- **Returns (raw)**: `ApiResult[PlaylistSnapshotId, ReorderOrReplacePlaylistsTracksErrorBody]`
- **Error**: `ReorderOrReplacePlaylistsTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PlaylistsTracksRequest1` | `spotify_web_api/models/playlists_tracks_request1.py` |
| `PlaylistsTracksRequest1Dict` | `spotify_web_api/models/playlists_tracks_request1.py` |
| `PlaylistSnapshotId` | `spotify_web_api/models/playlist_snapshot_id.py` |
| `ReorderOrReplacePlaylistsTracksErrorBody` | `spotify_web_api/errors/reorder_or_replace_playlists_tracks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.playlists.unfollow_playlist

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

### client.playlists.upload_custom_playlist_cover

- **Route**: `PUT /playlists/{playlist_id}/images`
- **Auth**: `oauth_2_0`
- **Signature**: `def upload_custom_playlist_cover(playlist_id: str, body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `playlist_id`, `body`
- **Params**: `playlist_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UploadCustomPlaylistCoverErrorBody]`
- **Error**: `UploadCustomPlaylistCoverErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UploadCustomPlaylistCoverErrorBody` | `spotify_web_api/errors/upload_custom_playlist_cover_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

