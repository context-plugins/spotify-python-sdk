from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.add_to_queue_error import AddToQueueErrorBody, add_to_queue_error_mapper
from ..errors.get_a_users_available_devices_error import (
    GetAUsersAvailableDevicesErrorBody,
    get_a_users_available_devices_error_mapper,
)
from ..errors.get_information_about_the_users_current_playback_error import (
    GetInformationAboutTheUsersCurrentPlaybackErrorBody,
    get_information_about_the_users_current_playback_error_mapper,
)
from ..errors.get_queue_error import GetQueueErrorBody, get_queue_error_mapper
from ..errors.get_recently_played_error import GetRecentlyPlayedErrorBody, get_recently_played_error_mapper
from ..errors.get_the_users_currently_playing_track_error import (
    GetTheUsersCurrentlyPlayingTrackErrorBody,
    get_the_users_currently_playing_track_error_mapper,
)
from ..errors.pause_a_users_playback_error import PauseAUsersPlaybackErrorBody, pause_a_users_playback_error_mapper
from ..errors.seek_to_position_in_currently_playing_track_error import (
    SeekToPositionInCurrentlyPlayingTrackErrorBody,
    seek_to_position_in_currently_playing_track_error_mapper,
)
from ..errors.set_repeat_mode_on_users_playback_error import (
    SetRepeatModeOnUsersPlaybackErrorBody,
    set_repeat_mode_on_users_playback_error_mapper,
)
from ..errors.set_volume_for_users_playback_error import (
    SetVolumeForUsersPlaybackErrorBody,
    set_volume_for_users_playback_error_mapper,
)
from ..errors.skip_users_playback_to_next_track_error import (
    SkipUsersPlaybackToNextTrackErrorBody,
    skip_users_playback_to_next_track_error_mapper,
)
from ..errors.skip_users_playback_to_previous_track_error import (
    SkipUsersPlaybackToPreviousTrackErrorBody,
    skip_users_playback_to_previous_track_error_mapper,
)
from ..errors.start_a_users_playback_error import StartAUsersPlaybackErrorBody, start_a_users_playback_error_mapper
from ..errors.toggle_shuffle_for_users_playback_error import (
    ToggleShuffleForUsersPlaybackErrorBody,
    toggle_shuffle_for_users_playback_error_mapper,
)
from ..errors.transfer_a_users_playback_error import (
    TransferAUsersPlaybackErrorBody,
    transfer_a_users_playback_error_mapper,
)
from ..models.currently_playing_context_object import CurrentlyPlayingContextObject
from ..models.currently_playing_object import CurrentlyPlayingObject
from ..models.cursor_paging_play_history_object import CursorPagingPlayHistoryObject
from ..models.many_devices import ManyDevices
from ..models.me_player_request import MePlayerRequest, MePlayerRequestDict
from ..models.queue_object import QueueObject
from ..models.start_or_resume_playback_request import StartOrResumePlaybackRequest, StartOrResumePlaybackRequestDict
from ..server.server import Server


class Player:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PlayerWithRawResponse(client, server, auth)

    def add_to_queue(
        self, uri: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Add an item to the end of the user's current playback queue. This API only works for users who have Spotify
        Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            uri: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command received

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.add_to_queue(uri, device_id=device_id, request_options=request_options))

    def get_a_users_available_devices(self, *, request_options: RequestOptionsOrDict | None = None) -> ManyDevices:
        """Get information about a user’s available Spotify Connect devices. Some device models are not supported and
        will not be listed in the API response.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of devices

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_a_users_available_devices(request_options=request_options))

    def get_information_about_the_users_current_playback(
        self,
        *,
        market: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CurrentlyPlayingContextObject:
        """Get information about the user’s current playback state, including track or episode, progress, and active
        device.

        Args:
            market: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Information about playback

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_information_about_the_users_current_playback(
                market=market, additional_types=additional_types, request_options=request_options
            ),
        )

    def get_queue(self, *, request_options: RequestOptionsOrDict | None = None) -> QueueObject:
        """Get the list of objects that make up the user's queue.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Information about the queue

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_queue(request_options=request_options))

    def get_recently_played(
        self,
        *,
        limit: int | None = 20,
        after: int | None = None,
        before: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CursorPagingPlayHistoryObject:
        """Get tracks from the current user's recently played tracks. _**Note**: Currently doesn't support podcast
        episodes._

        Args:
            limit: Value sent with the request.
            after: Value sent with the request.
            before: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A paged set of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_recently_played(
                limit=limit, after=after, before=before, request_options=request_options
            ),
        )

    def get_the_users_currently_playing_track(
        self,
        *,
        market: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CurrentlyPlayingObject:
        """Get the object currently being played on the user's Spotify account.

        Args:
            market: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Information about the currently playing track

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_the_users_currently_playing_track(
                market=market, additional_types=additional_types, request_options=request_options
            ),
        )

    def pause_a_users_playback(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Pause playback on the user's account. This API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playback paused

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.pause_a_users_playback(device_id=device_id, request_options=request_options)
        )

    def seek_to_position_in_currently_playing_track(
        self, position_ms: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Seeks to the given position in the user’s currently playing track. This API only works for users who have
        Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            position_ms: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.seek_to_position_in_currently_playing_track(
                position_ms, device_id=device_id, request_options=request_options
            ),
        )

    def set_repeat_mode_on_users_playback(
        self, state: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Set the repeat mode for the user's playback. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            state: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.set_repeat_mode_on_users_playback(
                state, device_id=device_id, request_options=request_options
            ),
        )

    def set_volume_for_users_playback(
        self, volume_percent: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Set the volume for the user’s current playback device. This API only works for users who have Spotify
        Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            volume_percent: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.set_volume_for_users_playback(
                volume_percent, device_id=device_id, request_options=request_options
            ),
        )

    def skip_users_playback_to_next_track(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Skips to next track in the user’s queue. This API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.skip_users_playback_to_next_track(
                device_id=device_id, request_options=request_options
            ),
        )

    def skip_users_playback_to_previous_track(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Skips to previous track in the user’s queue. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.skip_users_playback_to_previous_track(
                device_id=device_id, request_options=request_options
            ),
        )

    def start_a_users_playback(
        self,
        *,
        device_id: str | None = None,
        body: StartOrResumePlaybackRequest | StartOrResumePlaybackRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Start a new context or resume current playback on the user's active device. This API only works for users who
        have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API
        endpoints.

        Args:
            device_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playback started

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.start_a_users_playback(
                device_id=device_id, body=body, request_options=request_options
            ),
        )

    def toggle_shuffle_for_users_playback(
        self, state: bool, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Toggle shuffle on or off for user’s playback. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            state: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.toggle_shuffle_for_users_playback(
                state, device_id=device_id, request_options=request_options
            ),
        )

    def transfer_a_users_playback(
        self,
        *,
        body: MePlayerRequest | MePlayerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Transfer playback to a new device and optionally begin playback. This API only works for users who have
        Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playback transferred

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.transfer_a_users_playback(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> PlayerWithRawResponse:
        return self._with_raw_response


class AsyncPlayer:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPlayerWithRawResponse(client, server, auth)

    async def add_to_queue(
        self, uri: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Add an item to the end of the user's current playback queue. This API only works for users who have Spotify
        Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            uri: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command received

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.add_to_queue(uri, device_id=device_id, request_options=request_options)
        )

    async def get_a_users_available_devices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManyDevices:
        """Get information about a user’s available Spotify Connect devices. Some device models are not supported and
        will not be listed in the API response.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of devices

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_a_users_available_devices(request_options=request_options))

    async def get_information_about_the_users_current_playback(
        self,
        *,
        market: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CurrentlyPlayingContextObject:
        """Get information about the user’s current playback state, including track or episode, progress, and active
        device.

        Args:
            market: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Information about playback

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_information_about_the_users_current_playback(
                market=market, additional_types=additional_types, request_options=request_options
            ),
        )

    async def get_queue(self, *, request_options: RequestOptionsOrDict | None = None) -> QueueObject:
        """Get the list of objects that make up the user's queue.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Information about the queue

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_queue(request_options=request_options))

    async def get_recently_played(
        self,
        *,
        limit: int | None = 20,
        after: int | None = None,
        before: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CursorPagingPlayHistoryObject:
        """Get tracks from the current user's recently played tracks. _**Note**: Currently doesn't support podcast
        episodes._

        Args:
            limit: Value sent with the request.
            after: Value sent with the request.
            before: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A paged set of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_recently_played(
                limit=limit, after=after, before=before, request_options=request_options
            ),
        )

    async def get_the_users_currently_playing_track(
        self,
        *,
        market: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CurrentlyPlayingObject:
        """Get the object currently being played on the user's Spotify account.

        Args:
            market: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Information about the currently playing track

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_the_users_currently_playing_track(
                market=market, additional_types=additional_types, request_options=request_options
            ),
        )

    async def pause_a_users_playback(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Pause playback on the user's account. This API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playback paused

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.pause_a_users_playback(device_id=device_id, request_options=request_options)
        )

    async def seek_to_position_in_currently_playing_track(
        self, position_ms: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Seeks to the given position in the user’s currently playing track. This API only works for users who have
        Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            position_ms: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.seek_to_position_in_currently_playing_track(
                position_ms, device_id=device_id, request_options=request_options
            ),
        )

    async def set_repeat_mode_on_users_playback(
        self, state: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Set the repeat mode for the user's playback. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            state: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.set_repeat_mode_on_users_playback(
                state, device_id=device_id, request_options=request_options
            ),
        )

    async def set_volume_for_users_playback(
        self, volume_percent: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Set the volume for the user’s current playback device. This API only works for users who have Spotify
        Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            volume_percent: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.set_volume_for_users_playback(
                volume_percent, device_id=device_id, request_options=request_options
            ),
        )

    async def skip_users_playback_to_next_track(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Skips to next track in the user’s queue. This API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.skip_users_playback_to_next_track(
                device_id=device_id, request_options=request_options
            ),
        )

    async def skip_users_playback_to_previous_track(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Skips to previous track in the user’s queue. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.skip_users_playback_to_previous_track(
                device_id=device_id, request_options=request_options
            ),
        )

    async def start_a_users_playback(
        self,
        *,
        device_id: str | None = None,
        body: StartOrResumePlaybackRequest | StartOrResumePlaybackRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Start a new context or resume current playback on the user's active device. This API only works for users who
        have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API
        endpoints.

        Args:
            device_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playback started

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.start_a_users_playback(
                device_id=device_id, body=body, request_options=request_options
            ),
        )

    async def toggle_shuffle_for_users_playback(
        self, state: bool, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Toggle shuffle on or off for user’s playback. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            state: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Command sent

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.toggle_shuffle_for_users_playback(
                state, device_id=device_id, request_options=request_options
            ),
        )

    async def transfer_a_users_playback(
        self,
        *,
        body: MePlayerRequest | MePlayerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Transfer playback to a new device and optionally begin playback. This API only works for users who have
        Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Playback transferred

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.transfer_a_users_playback(body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncPlayerWithRawResponse:
        return self._with_raw_response


class PlayerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_to_queue(
        self, uri: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddToQueueErrorBody]:
        """Add an item to the end of the user's current playback queue. This API only works for users who have Spotify
        Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            uri: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/player/queue"),
            query_params=[param[str]("uri", uri), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=add_to_queue_error_mapper,
            request_options=request_options,
        )

    def get_a_users_available_devices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyDevices, GetAUsersAvailableDevicesErrorBody]:
        """Get information about a user’s available Spotify Connect devices. Some device models are not supported and
        will not be listed in the API response.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player/devices"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyDevices],
            error_mapper=get_a_users_available_devices_error_mapper,
            request_options=request_options,
        )

    def get_information_about_the_users_current_playback(
        self,
        *,
        market: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CurrentlyPlayingContextObject, GetInformationAboutTheUsersCurrentPlaybackErrorBody]:
        """Get information about the user’s current playback state, including track or episode, progress, and active
        device.

        Args:
            market: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player"),
            query_params=[param[str | None]("market", market), param[str | None]("additional_types", additional_types)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[CurrentlyPlayingContextObject],
            error_mapper=get_information_about_the_users_current_playback_error_mapper,
            request_options=request_options,
        )

    def get_queue(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[QueueObject, GetQueueErrorBody]:
        """Get the list of objects that make up the user's queue.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player/queue"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[QueueObject],
            error_mapper=get_queue_error_mapper,
            request_options=request_options,
        )

    def get_recently_played(
        self,
        *,
        limit: int | None = 20,
        after: int | None = None,
        before: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CursorPagingPlayHistoryObject, GetRecentlyPlayedErrorBody]:
        """Get tracks from the current user's recently played tracks. _**Note**: Currently doesn't support podcast
        episodes._

        Args:
            limit: Value sent with the request.
            after: Value sent with the request.
            before: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player/recently-played"),
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("after", after),
                param[int | None]("before", before),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[CursorPagingPlayHistoryObject],
            error_mapper=get_recently_played_error_mapper,
            request_options=request_options,
        )

    def get_the_users_currently_playing_track(
        self,
        *,
        market: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CurrentlyPlayingObject, GetTheUsersCurrentlyPlayingTrackErrorBody]:
        """Get the object currently being played on the user's Spotify account.

        Args:
            market: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player/currently-playing"),
            query_params=[param[str | None]("market", market), param[str | None]("additional_types", additional_types)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[CurrentlyPlayingObject],
            error_mapper=get_the_users_currently_playing_track_error_mapper,
            request_options=request_options,
        )

    def pause_a_users_playback(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, PauseAUsersPlaybackErrorBody]:
        """Pause playback on the user's account. This API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/pause"),
            query_params=[param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=pause_a_users_playback_error_mapper,
            request_options=request_options,
        )

    def seek_to_position_in_currently_playing_track(
        self, position_ms: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SeekToPositionInCurrentlyPlayingTrackErrorBody]:
        """Seeks to the given position in the user’s currently playing track. This API only works for users who have
        Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            position_ms: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/seek"),
            query_params=[param[int]("position_ms", position_ms), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=seek_to_position_in_currently_playing_track_error_mapper,
            request_options=request_options,
        )

    def set_repeat_mode_on_users_playback(
        self, state: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SetRepeatModeOnUsersPlaybackErrorBody]:
        """Set the repeat mode for the user's playback. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            state: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/repeat"),
            query_params=[param[str]("state", state), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=set_repeat_mode_on_users_playback_error_mapper,
            request_options=request_options,
        )

    def set_volume_for_users_playback(
        self, volume_percent: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SetVolumeForUsersPlaybackErrorBody]:
        """Set the volume for the user’s current playback device. This API only works for users who have Spotify
        Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            volume_percent: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/volume"),
            query_params=[param[int]("volume_percent", volume_percent), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=set_volume_for_users_playback_error_mapper,
            request_options=request_options,
        )

    def skip_users_playback_to_next_track(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SkipUsersPlaybackToNextTrackErrorBody]:
        """Skips to next track in the user’s queue. This API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/player/next"),
            query_params=[param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=skip_users_playback_to_next_track_error_mapper,
            request_options=request_options,
        )

    def skip_users_playback_to_previous_track(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SkipUsersPlaybackToPreviousTrackErrorBody]:
        """Skips to previous track in the user’s queue. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/player/previous"),
            query_params=[param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=skip_users_playback_to_previous_track_error_mapper,
            request_options=request_options,
        )

    def start_a_users_playback(
        self,
        *,
        device_id: str | None = None,
        body: StartOrResumePlaybackRequest | StartOrResumePlaybackRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, StartAUsersPlaybackErrorBody]:
        """Start a new context or resume current playback on the user's active device. This API only works for users who
        have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API
        endpoints.

        Args:
            device_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/play"),
            query_params=[param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StartOrResumePlaybackRequest | StartOrResumePlaybackRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=start_a_users_playback_error_mapper,
            request_options=request_options,
        )

    def toggle_shuffle_for_users_playback(
        self, state: bool, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ToggleShuffleForUsersPlaybackErrorBody]:
        """Toggle shuffle on or off for user’s playback. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            state: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/shuffle"),
            query_params=[param[bool]("state", state), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=toggle_shuffle_for_users_playback_error_mapper,
            request_options=request_options,
        )

    def transfer_a_users_playback(
        self,
        *,
        body: MePlayerRequest | MePlayerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, TransferAUsersPlaybackErrorBody]:
        """Transfer playback to a new device and optionally begin playback. This API only works for users who have
        Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MePlayerRequest | MePlayerRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=transfer_a_users_playback_error_mapper,
            request_options=request_options,
        )


class AsyncPlayerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_to_queue(
        self, uri: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddToQueueErrorBody]:
        """Add an item to the end of the user's current playback queue. This API only works for users who have Spotify
        Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            uri: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/player/queue"),
            query_params=[param[str]("uri", uri), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=add_to_queue_error_mapper,
            request_options=request_options,
        )

    async def get_a_users_available_devices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyDevices, GetAUsersAvailableDevicesErrorBody]:
        """Get information about a user’s available Spotify Connect devices. Some device models are not supported and
        will not be listed in the API response.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player/devices"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[ManyDevices],
            error_mapper=get_a_users_available_devices_error_mapper,
            request_options=request_options,
        )

    async def get_information_about_the_users_current_playback(
        self,
        *,
        market: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CurrentlyPlayingContextObject, GetInformationAboutTheUsersCurrentPlaybackErrorBody]:
        """Get information about the user’s current playback state, including track or episode, progress, and active
        device.

        Args:
            market: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player"),
            query_params=[param[str | None]("market", market), param[str | None]("additional_types", additional_types)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[CurrentlyPlayingContextObject],
            error_mapper=get_information_about_the_users_current_playback_error_mapper,
            request_options=request_options,
        )

    async def get_queue(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[QueueObject, GetQueueErrorBody]:
        """Get the list of objects that make up the user's queue.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player/queue"),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[QueueObject],
            error_mapper=get_queue_error_mapper,
            request_options=request_options,
        )

    async def get_recently_played(
        self,
        *,
        limit: int | None = 20,
        after: int | None = None,
        before: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CursorPagingPlayHistoryObject, GetRecentlyPlayedErrorBody]:
        """Get tracks from the current user's recently played tracks. _**Note**: Currently doesn't support podcast
        episodes._

        Args:
            limit: Value sent with the request.
            after: Value sent with the request.
            before: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player/recently-played"),
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("after", after),
                param[int | None]("before", before),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[CursorPagingPlayHistoryObject],
            error_mapper=get_recently_played_error_mapper,
            request_options=request_options,
        )

    async def get_the_users_currently_playing_track(
        self,
        *,
        market: str | None = None,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CurrentlyPlayingObject, GetTheUsersCurrentlyPlayingTrackErrorBody]:
        """Get the object currently being played on the user's Spotify account.

        Args:
            market: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/player/currently-playing"),
            query_params=[param[str | None]("market", market), param[str | None]("additional_types", additional_types)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[CurrentlyPlayingObject],
            error_mapper=get_the_users_currently_playing_track_error_mapper,
            request_options=request_options,
        )

    async def pause_a_users_playback(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, PauseAUsersPlaybackErrorBody]:
        """Pause playback on the user's account. This API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/pause"),
            query_params=[param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=pause_a_users_playback_error_mapper,
            request_options=request_options,
        )

    async def seek_to_position_in_currently_playing_track(
        self, position_ms: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SeekToPositionInCurrentlyPlayingTrackErrorBody]:
        """Seeks to the given position in the user’s currently playing track. This API only works for users who have
        Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            position_ms: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/seek"),
            query_params=[param[int]("position_ms", position_ms), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=seek_to_position_in_currently_playing_track_error_mapper,
            request_options=request_options,
        )

    async def set_repeat_mode_on_users_playback(
        self, state: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SetRepeatModeOnUsersPlaybackErrorBody]:
        """Set the repeat mode for the user's playback. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            state: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/repeat"),
            query_params=[param[str]("state", state), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=set_repeat_mode_on_users_playback_error_mapper,
            request_options=request_options,
        )

    async def set_volume_for_users_playback(
        self, volume_percent: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SetVolumeForUsersPlaybackErrorBody]:
        """Set the volume for the user’s current playback device. This API only works for users who have Spotify
        Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            volume_percent: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/volume"),
            query_params=[param[int]("volume_percent", volume_percent), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=set_volume_for_users_playback_error_mapper,
            request_options=request_options,
        )

    async def skip_users_playback_to_next_track(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SkipUsersPlaybackToNextTrackErrorBody]:
        """Skips to next track in the user’s queue. This API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/player/next"),
            query_params=[param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=skip_users_playback_to_next_track_error_mapper,
            request_options=request_options,
        )

    async def skip_users_playback_to_previous_track(
        self, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SkipUsersPlaybackToPreviousTrackErrorBody]:
        """Skips to previous track in the user’s queue. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/player/previous"),
            query_params=[param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=skip_users_playback_to_previous_track_error_mapper,
            request_options=request_options,
        )

    async def start_a_users_playback(
        self,
        *,
        device_id: str | None = None,
        body: StartOrResumePlaybackRequest | StartOrResumePlaybackRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, StartAUsersPlaybackErrorBody]:
        """Start a new context or resume current playback on the user's active device. This API only works for users who
        have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API
        endpoints.

        Args:
            device_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/play"),
            query_params=[param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StartOrResumePlaybackRequest | StartOrResumePlaybackRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=start_a_users_playback_error_mapper,
            request_options=request_options,
        )

    async def toggle_shuffle_for_users_playback(
        self, state: bool, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ToggleShuffleForUsersPlaybackErrorBody]:
        """Toggle shuffle on or off for user’s playback. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            state: Value sent with the request.
            device_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player/shuffle"),
            query_params=[param[bool]("state", state), param[str | None]("device_id", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=toggle_shuffle_for_users_playback_error_mapper,
            request_options=request_options,
        )

    async def transfer_a_users_playback(
        self,
        *,
        body: MePlayerRequest | MePlayerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, TransferAUsersPlaybackErrorBody]:
        """Transfer playback to a new device and optionally begin playback. This API only works for users who have
        Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/player"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MePlayerRequest | MePlayerRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=transfer_a_users_playback_error_mapper,
            request_options=request_options,
        )
