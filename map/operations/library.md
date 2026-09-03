<!-- Generated file — do not edit; regenerated with the SDK. -->

# Library — operations

Accessor: `client.library` · Source: `spotify_web_api/apis/library.py` · 29 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.library.change_playlist_details

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

### client.library.check_current_user_follows

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

### client.library.check_users_saved_albums

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

### client.library.check_users_saved_audiobooks

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

### client.library.check_users_saved_episodes

- **Route**: `GET /me/episodes/contains`
- **Auth**: `oauth_2_0`
- **Signature**: `def check_users_saved_episodes(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `list[bool]`
- **Returns (raw)**: `ApiResult[list[bool], CheckUsersSavedEpisodesErrorBody]`
- **Error**: `CheckUsersSavedEpisodesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckUsersSavedEpisodesErrorBody` | `spotify_web_api/errors/check_users_saved_episodes_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.library.check_users_saved_shows

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

### client.library.check_users_saved_tracks

- **Route**: `GET /me/tracks/contains`
- **Auth**: `oauth_2_0`
- **Signature**: `def check_users_saved_tracks(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `list[bool]`
- **Returns (raw)**: `ApiResult[list[bool], CheckUsersSavedTracksErrorBody]`
- **Error**: `CheckUsersSavedTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckUsersSavedTracksErrorBody` | `spotify_web_api/errors/check_users_saved_tracks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.library.create_playlist

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

### client.library.follow_artists_users

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

### client.library.get_a_list_of_current_users_playlists

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

### client.library.get_followed

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

### client.library.get_users_saved_albums

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

### client.library.get_users_saved_audiobooks

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

### client.library.get_users_saved_episodes

- **Route**: `GET /me/episodes`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_users_saved_episodes(*, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `market` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingSavedEpisodeObject`
- **Returns (raw)**: `ApiResult[PagingSavedEpisodeObject, GetUsersSavedEpisodesErrorBody]`
- **Error**: `GetUsersSavedEpisodesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingSavedEpisodeObject` | `spotify_web_api/models/paging_saved_episode_object.py` |
| `GetUsersSavedEpisodesErrorBody` | `spotify_web_api/errors/get_users_saved_episodes_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.library.get_users_saved_shows

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

### client.library.get_users_saved_tracks

- **Route**: `GET /me/tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_users_saved_tracks(*, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `market` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PagingSavedTrackObject`
- **Returns (raw)**: `ApiResult[PagingSavedTrackObject, GetUsersSavedTracksErrorBody]`
- **Error**: `GetUsersSavedTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PagingSavedTrackObject` | `spotify_web_api/models/paging_saved_track_object.py` |
| `GetUsersSavedTracksErrorBody` | `spotify_web_api/errors/get_users_saved_tracks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.library.get_users_top_artists

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

### client.library.get_users_top_tracks

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

### client.library.remove_albums_user

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

### client.library.remove_audiobooks_user

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

### client.library.remove_episodes_user

- **Route**: `DELETE /me/episodes`
- **Auth**: `oauth_2_0`
- **Signature**: `def remove_episodes_user(ids: str, *, body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveEpisodesUserErrorBody]`
- **Error**: `RemoveEpisodesUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveEpisodesRequest` | `spotify_web_api/models/remove_episodes_request.py` |
| `RemoveEpisodesRequestDict` | `spotify_web_api/models/remove_episodes_request.py` |
| `RemoveEpisodesUserErrorBody` | `spotify_web_api/errors/remove_episodes_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.library.remove_shows_user

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

### client.library.remove_tracks_user

- **Route**: `DELETE /me/tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def remove_tracks_user(ids: str, *, body: RemoveTracksRequest | RemoveTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveTracksUserErrorBody]`
- **Error**: `RemoveTracksUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveTracksRequest` | `spotify_web_api/models/remove_tracks_request.py` |
| `RemoveTracksRequestDict` | `spotify_web_api/models/remove_tracks_request.py` |
| `RemoveTracksUserErrorBody` | `spotify_web_api/errors/remove_tracks_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.library.save_albums_user

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

### client.library.save_audiobooks_user

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

### client.library.save_episodes_user

- **Route**: `PUT /me/episodes`
- **Auth**: `oauth_2_0`
- **Signature**: `def save_episodes_user(ids: str, *, body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SaveEpisodesUserErrorBody]`
- **Error**: `SaveEpisodesUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SaveEpisodesRequest` | `spotify_web_api/models/save_episodes_request.py` |
| `SaveEpisodesRequestDict` | `spotify_web_api/models/save_episodes_request.py` |
| `SaveEpisodesUserErrorBody` | `spotify_web_api/errors/save_episodes_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.library.save_shows_user

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

### client.library.save_tracks_user

- **Route**: `PUT /me/tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def save_tracks_user(ids: str, *, body: SaveTracksRequest | SaveTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SaveTracksUserErrorBody]`
- **Error**: `SaveTracksUserErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SaveTracksRequest` | `spotify_web_api/models/save_tracks_request.py` |
| `SaveTracksRequestDict` | `spotify_web_api/models/save_tracks_request.py` |
| `SaveTracksUserErrorBody` | `spotify_web_api/errors/save_tracks_user_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.library.unfollow_artists_users

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

