<!-- Generated file — do not edit; regenerated with the SDK. -->

# Tracks — operations

Accessor: `client.tracks` · Source: `spotify_web_api/apis/tracks.py` · 17 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.tracks.add_tracks_to_playlist

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

### client.tracks.check_users_saved_tracks

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

### client.tracks.get_an_albums_tracks

- **Route**: `GET /albums/{id}/tracks`
- **Auth**: `oauth_2_0` OR `oauth_2_0_client_credentials`
- **Signature**: `def get_an_albums_tracks(id_: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `market` — query · `limit` — query · `offset` — query
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

### client.tracks.get_an_artists_top_tracks

- **Route**: `GET /artists/{id}/top-tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_an_artists_top_tracks(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `market` — query
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

### client.tracks.get_audio_analysis

- **Route**: `GET /audio-analysis/{id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_audio_analysis(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `AudioAnalysisObject`
- **Returns (raw)**: `ApiResult[AudioAnalysisObject, GetAudioAnalysisErrorBody]`
- **Error**: `GetAudioAnalysisErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AudioAnalysisObject` | `spotify_web_api/models/audio_analysis_object.py` |
| `GetAudioAnalysisErrorBody` | `spotify_web_api/errors/get_audio_analysis_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.tracks.get_audio_features

- **Route**: `GET /audio-features/{id}`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_audio_features(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `AudioFeaturesObject`
- **Returns (raw)**: `ApiResult[AudioFeaturesObject, GetAudioFeaturesErrorBody]`
- **Error**: `GetAudioFeaturesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AudioFeaturesObject` | `spotify_web_api/models/audio_features_object.py` |
| `GetAudioFeaturesErrorBody` | `spotify_web_api/errors/get_audio_features_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.tracks.get_playlists_tracks

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

### client.tracks.get_recommendations

- **Route**: `GET /recommendations`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_recommendations(*, limit: int | None = 20, market: str | None = None, seed_artists: str | None = None, seed_genres: str | None = None, seed_tracks: str | None = None, min_acousticness: float | None = None, max_acousticness: float | None = None, target_acousticness: float | None = None, min_danceability: float | None = None, max_danceability: float | None = None, target_danceability: float | None = None, min_duration_ms: int | None = None, max_duration_ms: int | None = None, target_duration_ms: int | None = None, min_energy: float | None = None, max_energy: float | None = None, target_energy: float | None = None, min_instrumentalness: float | None = None, max_instrumentalness: float | None = None, target_instrumentalness: float | None = None, min_key: int | None = None, max_key: int | None = None, target_key: int | None = None, min_liveness: float | None = None, max_liveness: float | None = None, target_liveness: float | None = None, min_loudness: float | None = None, max_loudness: float | None = None, target_loudness: float | None = None, min_mode: int | None = None, max_mode: int | None = None, target_mode: int | None = None, min_popularity: int | None = None, max_popularity: int | None = None, target_popularity: int | None = None, min_speechiness: float | None = None, max_speechiness: float | None = None, target_speechiness: float | None = None, min_tempo: float | None = None, max_tempo: float | None = None, target_tempo: float | None = None, min_time_signature: int | None = None, max_time_signature: int | None = None, target_time_signature: int | None = None, min_valence: float | None = None, max_valence: float | None = None, target_valence: float | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `market` — query · `seed_artists` — query · `seed_genres` — query · `seed_tracks` — query · `min_acousticness` — query · `max_acousticness` — query · `target_acousticness` — query · `min_danceability` — query · `max_danceability` — query · `target_danceability` — query · `min_duration_ms` — query · `max_duration_ms` — query · `target_duration_ms` — query · `min_energy` — query · `max_energy` — query · `target_energy` — query · `min_instrumentalness` — query · `max_instrumentalness` — query · `target_instrumentalness` — query · `min_key` — query · `max_key` — query · `target_key` — query · `min_liveness` — query · `max_liveness` — query · `target_liveness` — query · `min_loudness` — query · `max_loudness` — query · `target_loudness` — query · `min_mode` — query · `max_mode` — query · `target_mode` — query · `min_popularity` — query · `max_popularity` — query · `target_popularity` — query · `min_speechiness` — query · `max_speechiness` — query · `target_speechiness` — query · `min_tempo` — query · `max_tempo` — query · `target_tempo` — query · `min_time_signature` — query · `max_time_signature` — query · `target_time_signature` — query · `min_valence` — query · `max_valence` — query · `target_valence` — query
- **Returns (parsed)**: `RecommendationsObject`
- **Returns (raw)**: `ApiResult[RecommendationsObject, GetRecommendationsErrorBody]`
- **Error**: `GetRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RecommendationsObject` | `spotify_web_api/models/recommendations_object.py` |
| `GetRecommendationsErrorBody` | `spotify_web_api/errors/get_recommendations_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.tracks.get_several_audio_features

- **Route**: `GET /audio-features`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_several_audio_features(ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query
- **Returns (parsed)**: `ManyAudioFeatures`
- **Returns (raw)**: `ApiResult[ManyAudioFeatures, GetSeveralAudioFeaturesErrorBody]`
- **Error**: `GetSeveralAudioFeaturesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyAudioFeatures` | `spotify_web_api/models/many_audio_features.py` |
| `GetSeveralAudioFeaturesErrorBody` | `spotify_web_api/errors/get_several_audio_features_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.tracks.get_several_tracks

- **Route**: `GET /tracks`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_several_tracks(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ids`
- **Params**: `ids` — query · `market` — query
- **Returns (parsed)**: `ManyTracks`
- **Returns (raw)**: `ApiResult[ManyTracks, GetSeveralTracksErrorBody]`
- **Error**: `GetSeveralTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyTracks` | `spotify_web_api/models/many_tracks.py` |
| `GetSeveralTracksErrorBody` | `spotify_web_api/errors/get_several_tracks_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.tracks.get_track

- **Route**: `GET /tracks/{id}`
- **Auth**: `oauth_2_0` OR `oauth_2_0_client_credentials`
- **Signature**: `def get_track(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `market` — query
- **Returns (parsed)**: `TrackObject`
- **Returns (raw)**: `ApiResult[TrackObject, GetTrackErrorBody]`
- **Error**: `GetTrackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TrackObject` | `spotify_web_api/models/track_object.py` |
| `GetTrackErrorBody` | `spotify_web_api/errors/get_track_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.tracks.get_users_saved_tracks

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

### client.tracks.get_users_top_tracks

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

### client.tracks.remove_tracks_playlist

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

### client.tracks.remove_tracks_user

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

### client.tracks.reorder_or_replace_playlists_tracks

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

### client.tracks.save_tracks_user

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

