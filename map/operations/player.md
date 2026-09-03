<!-- Generated file — do not edit; regenerated with the SDK. -->

# Player — operations

Accessor: `client.player` · Source: `spotify_web_api/apis/player.py` · 15 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.player.add_to_queue

- **Route**: `POST /me/player/queue`
- **Auth**: `oauth_2_0`
- **Signature**: `def add_to_queue(uri: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uri`
- **Params**: `uri` — query · `device_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddToQueueErrorBody]`
- **Error**: `AddToQueueErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddToQueueErrorBody` | `spotify_web_api/errors/add_to_queue_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.get_a_users_available_devices

- **Route**: `GET /me/player/devices`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_a_users_available_devices(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ManyDevices`
- **Returns (raw)**: `ApiResult[ManyDevices, GetAUsersAvailableDevicesErrorBody]`
- **Error**: `GetAUsersAvailableDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManyDevices` | `spotify_web_api/models/many_devices.py` |
| `GetAUsersAvailableDevicesErrorBody` | `spotify_web_api/errors/get_a_users_available_devices_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.get_information_about_the_users_current_playback

- **Route**: `GET /me/player`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_information_about_the_users_current_playback(*, market: str | None = None, additional_types: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `market` — query · `additional_types` — query
- **Returns (parsed)**: `CurrentlyPlayingContextObject`
- **Returns (raw)**: `ApiResult[CurrentlyPlayingContextObject, GetInformationAboutTheUsersCurrentPlaybackErrorBody]`
- **Error**: `GetInformationAboutTheUsersCurrentPlaybackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CurrentlyPlayingContextObject` | `spotify_web_api/models/currently_playing_context_object.py` |
| `GetInformationAboutTheUsersCurrentPlaybackErrorBody` | `spotify_web_api/errors/get_information_about_the_users_current_playback_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.get_queue

- **Route**: `GET /me/player/queue`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_queue(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `QueueObject`
- **Returns (raw)**: `ApiResult[QueueObject, GetQueueErrorBody]`
- **Error**: `GetQueueErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `QueueObject` | `spotify_web_api/models/queue_object.py` |
| `GetQueueErrorBody` | `spotify_web_api/errors/get_queue_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.get_recently_played

- **Route**: `GET /me/player/recently-played`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_recently_played(*, limit: int | None = 20, after: int | None = None, before: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `after` — query · `before` — query
- **Returns (parsed)**: `CursorPagingPlayHistoryObject`
- **Returns (raw)**: `ApiResult[CursorPagingPlayHistoryObject, GetRecentlyPlayedErrorBody]`
- **Error**: `GetRecentlyPlayedErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CursorPagingPlayHistoryObject` | `spotify_web_api/models/cursor_paging_play_history_object.py` |
| `GetRecentlyPlayedErrorBody` | `spotify_web_api/errors/get_recently_played_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.get_the_users_currently_playing_track

- **Route**: `GET /me/player/currently-playing`
- **Auth**: `oauth_2_0`
- **Signature**: `def get_the_users_currently_playing_track(*, market: str | None = None, additional_types: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `market` — query · `additional_types` — query
- **Returns (parsed)**: `CurrentlyPlayingObject`
- **Returns (raw)**: `ApiResult[CurrentlyPlayingObject, GetTheUsersCurrentlyPlayingTrackErrorBody]`
- **Error**: `GetTheUsersCurrentlyPlayingTrackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CurrentlyPlayingObject` | `spotify_web_api/models/currently_playing_object.py` |
| `GetTheUsersCurrentlyPlayingTrackErrorBody` | `spotify_web_api/errors/get_the_users_currently_playing_track_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.pause_a_users_playback

- **Route**: `PUT /me/player/pause`
- **Auth**: `oauth_2_0`
- **Signature**: `def pause_a_users_playback(*, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `device_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PauseAUsersPlaybackErrorBody]`
- **Error**: `PauseAUsersPlaybackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PauseAUsersPlaybackErrorBody` | `spotify_web_api/errors/pause_a_users_playback_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.seek_to_position_in_currently_playing_track

- **Route**: `PUT /me/player/seek`
- **Auth**: `oauth_2_0`
- **Signature**: `def seek_to_position_in_currently_playing_track(position_ms: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `position_ms`
- **Params**: `position_ms` — query · `device_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SeekToPositionInCurrentlyPlayingTrackErrorBody]`
- **Error**: `SeekToPositionInCurrentlyPlayingTrackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SeekToPositionInCurrentlyPlayingTrackErrorBody` | `spotify_web_api/errors/seek_to_position_in_currently_playing_track_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.set_repeat_mode_on_users_playback

- **Route**: `PUT /me/player/repeat`
- **Auth**: `oauth_2_0`
- **Signature**: `def set_repeat_mode_on_users_playback(state: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `state`
- **Params**: `state` — query · `device_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SetRepeatModeOnUsersPlaybackErrorBody]`
- **Error**: `SetRepeatModeOnUsersPlaybackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetRepeatModeOnUsersPlaybackErrorBody` | `spotify_web_api/errors/set_repeat_mode_on_users_playback_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.set_volume_for_users_playback

- **Route**: `PUT /me/player/volume`
- **Auth**: `oauth_2_0`
- **Signature**: `def set_volume_for_users_playback(volume_percent: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `volume_percent`
- **Params**: `volume_percent` — query · `device_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SetVolumeForUsersPlaybackErrorBody]`
- **Error**: `SetVolumeForUsersPlaybackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetVolumeForUsersPlaybackErrorBody` | `spotify_web_api/errors/set_volume_for_users_playback_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.skip_users_playback_to_next_track

- **Route**: `POST /me/player/next`
- **Auth**: `oauth_2_0`
- **Signature**: `def skip_users_playback_to_next_track(*, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `device_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SkipUsersPlaybackToNextTrackErrorBody]`
- **Error**: `SkipUsersPlaybackToNextTrackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SkipUsersPlaybackToNextTrackErrorBody` | `spotify_web_api/errors/skip_users_playback_to_next_track_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.skip_users_playback_to_previous_track

- **Route**: `POST /me/player/previous`
- **Auth**: `oauth_2_0`
- **Signature**: `def skip_users_playback_to_previous_track(*, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `device_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SkipUsersPlaybackToPreviousTrackErrorBody]`
- **Error**: `SkipUsersPlaybackToPreviousTrackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SkipUsersPlaybackToPreviousTrackErrorBody` | `spotify_web_api/errors/skip_users_playback_to_previous_track_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.start_a_users_playback

- **Route**: `PUT /me/player/play`
- **Auth**: `oauth_2_0`
- **Signature**: `def start_a_users_playback(*, device_id: str | None = None, body: StartOrResumePlaybackRequest | StartOrResumePlaybackRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `device_id` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, StartAUsersPlaybackErrorBody]`
- **Error**: `StartAUsersPlaybackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StartOrResumePlaybackRequest` | `spotify_web_api/models/start_or_resume_playback_request.py` |
| `StartOrResumePlaybackRequestDict` | `spotify_web_api/models/start_or_resume_playback_request.py` |
| `StartAUsersPlaybackErrorBody` | `spotify_web_api/errors/start_a_users_playback_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.toggle_shuffle_for_users_playback

- **Route**: `PUT /me/player/shuffle`
- **Auth**: `oauth_2_0`
- **Signature**: `def toggle_shuffle_for_users_playback(state: bool, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `state`
- **Params**: `state` — query · `device_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, ToggleShuffleForUsersPlaybackErrorBody]`
- **Error**: `ToggleShuffleForUsersPlaybackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ToggleShuffleForUsersPlaybackErrorBody` | `spotify_web_api/errors/toggle_shuffle_for_users_playback_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

### client.player.transfer_a_users_playback

- **Route**: `PUT /me/player`
- **Auth**: `oauth_2_0`
- **Signature**: `def transfer_a_users_playback(*, body: MePlayerRequest | MePlayerRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, TransferAUsersPlaybackErrorBody]`
- **Error**: `TransferAUsersPlaybackErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MePlayerRequest` | `spotify_web_api/models/me_player_request.py` |
| `MePlayerRequestDict` | `spotify_web_api/models/me_player_request.py` |
| `TransferAUsersPlaybackErrorBody` | `spotify_web_api/errors/transfer_a_users_playback_error.py` |
| `Unauthorized1` | `spotify_web_api/models/unauthorized1.py` |
| `Forbidden1` | `spotify_web_api/models/forbidden1.py` |
| `TooManyRequests1` | `spotify_web_api/models/too_many_requests1.py` |

