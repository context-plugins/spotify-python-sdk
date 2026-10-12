from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
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
from ..errors.add_tracks_to_playlist_error import AddTracksToPlaylistErrorBody, add_tracks_to_playlist_error_mapper
from ..errors.check_users_saved_tracks_error import (
    CheckUsersSavedTracksErrorBody,
    check_users_saved_tracks_error_mapper,
)
from ..errors.get_an_albums_tracks_error import GetAnAlbumsTracksErrorBody, get_an_albums_tracks_error_mapper
from ..errors.get_an_artists_top_tracks_error import (
    GetAnArtistsTopTracksErrorBody,
    get_an_artists_top_tracks_error_mapper,
)
from ..errors.get_audio_analysis_error import GetAudioAnalysisErrorBody, get_audio_analysis_error_mapper
from ..errors.get_audio_features_error import GetAudioFeaturesErrorBody, get_audio_features_error_mapper
from ..errors.get_playlists_tracks_error import GetPlaylistsTracksErrorBody, get_playlists_tracks_error_mapper
from ..errors.get_recommendations_error import GetRecommendationsErrorBody, get_recommendations_error_mapper
from ..errors.get_several_audio_features_error import (
    GetSeveralAudioFeaturesErrorBody,
    get_several_audio_features_error_mapper,
)
from ..errors.get_several_tracks_error import GetSeveralTracksErrorBody, get_several_tracks_error_mapper
from ..errors.get_track_error import GetTrackErrorBody, get_track_error_mapper
from ..errors.get_users_saved_tracks_error import GetUsersSavedTracksErrorBody, get_users_saved_tracks_error_mapper
from ..errors.get_users_top_tracks_error import GetUsersTopTracksErrorBody, get_users_top_tracks_error_mapper
from ..errors.remove_tracks_playlist_error import RemoveTracksPlaylistErrorBody, remove_tracks_playlist_error_mapper
from ..errors.remove_tracks_user_error import RemoveTracksUserErrorBody, remove_tracks_user_error_mapper
from ..errors.reorder_or_replace_playlists_tracks_error import (
    ReorderOrReplacePlaylistsTracksErrorBody,
    reorder_or_replace_playlists_tracks_error_mapper,
)
from ..errors.save_tracks_user_error import SaveTracksUserErrorBody, save_tracks_user_error_mapper
from ..models.audio_analysis_object import AudioAnalysisObject
from ..models.audio_features_object import AudioFeaturesObject
from ..models.many_audio_features import ManyAudioFeatures
from ..models.many_tracks import ManyTracks
from ..models.paging_playlist_track_object import PagingPlaylistTrackObject
from ..models.paging_saved_track_object import PagingSavedTrackObject
from ..models.paging_simplified_track_object import PagingSimplifiedTrackObject
from ..models.paging_track_object import PagingTrackObject
from ..models.playlist_snapshot_id import PlaylistSnapshotId
from ..models.playlists_tracks_request import PlaylistsTracksRequest, PlaylistsTracksRequestDict
from ..models.playlists_tracks_request1 import PlaylistsTracksRequest1, PlaylistsTracksRequest1Dict
from ..models.playlists_tracks_request2 import PlaylistsTracksRequest2, PlaylistsTracksRequest2Dict
from ..models.recommendations_object import RecommendationsObject
from ..models.remove_tracks_request import RemoveTracksRequest, RemoveTracksRequestDict
from ..models.save_tracks_request import SaveTracksRequest, SaveTracksRequestDict
from ..models.track_object import TrackObject
from ..server.server import Server


class Tracks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TracksWithRawResponse(client, server, auth)

    def add_tracks_to_playlist(
        self,
        playlist_id: str,
        *,
        position: int | None = None,
        uris: str | None = None,
        body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Add one or more items to a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            position: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.add_tracks_to_playlist(
                playlist_id, position=position, uris=uris, body=body, request_options=request_options
            ),
        )

    def check_users_saved_tracks(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]:
        """Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.check_users_saved_tracks(ids, request_options=request_options))

    def get_an_albums_tracks(
        self,
        id_: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedTrackObject:
        """Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number
        of tracks returned.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_an_albums_tracks(
                id_, market=market, limit=limit, offset=offset, request_options=request_options
            ),
        )

    def get_an_artists_top_tracks(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyTracks:
        """Get Spotify catalog information about an artist's top tracks by country.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_an_artists_top_tracks(id_, market=market, request_options=request_options)
        )

    def get_audio_analysis(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AudioAnalysisObject:
        """Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s
        structure and musical content, including rhythm, pitch, and timbre.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Audio analysis for one track

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_audio_analysis(id_, request_options=request_options))

    def get_audio_features(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AudioFeaturesObject:
        """Get audio feature information for a single track identified by its unique Spotify ID.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Audio features for one track

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_audio_features(id_, request_options=request_options))

    def get_playlists_tracks(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingPlaylistTrackObject:
        """Get full details of the items of a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_playlists_tracks(
                playlist_id,
                market=market,
                fields=fields,
                limit=limit,
                offset=offset,
                additional_types=additional_types,
                request_options=request_options,
            ),
        )

    def get_recommendations(
        self,
        *,
        limit: int | None = 20,
        market: str | None = None,
        seed_artists: str | None = None,
        seed_genres: str | None = None,
        seed_tracks: str | None = None,
        min_acousticness: float | None = None,
        max_acousticness: float | None = None,
        target_acousticness: float | None = None,
        min_danceability: float | None = None,
        max_danceability: float | None = None,
        target_danceability: float | None = None,
        min_duration_ms: int | None = None,
        max_duration_ms: int | None = None,
        target_duration_ms: int | None = None,
        min_energy: float | None = None,
        max_energy: float | None = None,
        target_energy: float | None = None,
        min_instrumentalness: float | None = None,
        max_instrumentalness: float | None = None,
        target_instrumentalness: float | None = None,
        min_key: int | None = None,
        max_key: int | None = None,
        target_key: int | None = None,
        min_liveness: float | None = None,
        max_liveness: float | None = None,
        target_liveness: float | None = None,
        min_loudness: float | None = None,
        max_loudness: float | None = None,
        target_loudness: float | None = None,
        min_mode: int | None = None,
        max_mode: int | None = None,
        target_mode: int | None = None,
        min_popularity: int | None = None,
        max_popularity: int | None = None,
        target_popularity: int | None = None,
        min_speechiness: float | None = None,
        max_speechiness: float | None = None,
        target_speechiness: float | None = None,
        min_tempo: float | None = None,
        max_tempo: float | None = None,
        target_tempo: float | None = None,
        min_time_signature: int | None = None,
        max_time_signature: int | None = None,
        target_time_signature: int | None = None,
        min_valence: float | None = None,
        max_valence: float | None = None,
        target_valence: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecommendationsObject:
        """Recommendations are generated based on the available information for a given seed entity and matched against
        similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will
        be returned together with pool size details.

        For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.

        Args:
            limit: Value sent with the request.
            market: Value sent with the request.
            seed_artists: Value sent with the request.
            seed_genres: Value sent with the request.
            seed_tracks: Value sent with the request.
            min_acousticness: Value sent with the request.
            max_acousticness: Value sent with the request.
            target_acousticness: Value sent with the request.
            min_danceability: Value sent with the request.
            max_danceability: Value sent with the request.
            target_danceability: Value sent with the request.
            min_duration_ms: Value sent with the request.
            max_duration_ms: Value sent with the request.
            target_duration_ms: Value sent with the request.
            min_energy: Value sent with the request.
            max_energy: Value sent with the request.
            target_energy: Value sent with the request.
            min_instrumentalness: Value sent with the request.
            max_instrumentalness: Value sent with the request.
            target_instrumentalness: Value sent with the request.
            min_key: Value sent with the request.
            max_key: Value sent with the request.
            target_key: Value sent with the request.
            min_liveness: Value sent with the request.
            max_liveness: Value sent with the request.
            target_liveness: Value sent with the request.
            min_loudness: Value sent with the request.
            max_loudness: Value sent with the request.
            target_loudness: Value sent with the request.
            min_mode: Value sent with the request.
            max_mode: Value sent with the request.
            target_mode: Value sent with the request.
            min_popularity: Value sent with the request.
            max_popularity: Value sent with the request.
            target_popularity: Value sent with the request.
            min_speechiness: Value sent with the request.
            max_speechiness: Value sent with the request.
            target_speechiness: Value sent with the request.
            min_tempo: Value sent with the request.
            max_tempo: Value sent with the request.
            target_tempo: Value sent with the request.
            min_time_signature: Value sent with the request.
            max_time_signature: Value sent with the request.
            target_time_signature: Value sent with the request.
            min_valence: Value sent with the request.
            max_valence: Value sent with the request.
            target_valence: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of recommendations

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_recommendations(
                limit=limit,
                market=market,
                seed_artists=seed_artists,
                seed_genres=seed_genres,
                seed_tracks=seed_tracks,
                min_acousticness=min_acousticness,
                max_acousticness=max_acousticness,
                target_acousticness=target_acousticness,
                min_danceability=min_danceability,
                max_danceability=max_danceability,
                target_danceability=target_danceability,
                min_duration_ms=min_duration_ms,
                max_duration_ms=max_duration_ms,
                target_duration_ms=target_duration_ms,
                min_energy=min_energy,
                max_energy=max_energy,
                target_energy=target_energy,
                min_instrumentalness=min_instrumentalness,
                max_instrumentalness=max_instrumentalness,
                target_instrumentalness=target_instrumentalness,
                min_key=min_key,
                max_key=max_key,
                target_key=target_key,
                min_liveness=min_liveness,
                max_liveness=max_liveness,
                target_liveness=target_liveness,
                min_loudness=min_loudness,
                max_loudness=max_loudness,
                target_loudness=target_loudness,
                min_mode=min_mode,
                max_mode=max_mode,
                target_mode=target_mode,
                min_popularity=min_popularity,
                max_popularity=max_popularity,
                target_popularity=target_popularity,
                min_speechiness=min_speechiness,
                max_speechiness=max_speechiness,
                target_speechiness=target_speechiness,
                min_tempo=min_tempo,
                max_tempo=max_tempo,
                target_tempo=target_tempo,
                min_time_signature=min_time_signature,
                max_time_signature=max_time_signature,
                target_time_signature=target_time_signature,
                min_valence=min_valence,
                max_valence=max_valence,
                target_valence=target_valence,
                request_options=request_options,
            ),
        )

    def get_several_audio_features(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManyAudioFeatures:
        """Get audio features for multiple tracks based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of audio features

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_several_audio_features(ids, request_options=request_options))

    def get_several_tracks(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyTracks:
        """Get Spotify catalog information for multiple tracks based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_several_tracks(ids, market=market, request_options=request_options))

    def get_track(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> TrackObject:
        """Get Spotify catalog information for a single track identified by its unique Spotify ID.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A track

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.get_track(id_, market=market, request_options=request_options))

    def get_users_saved_tracks(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedTrackObject:
        """Get a list of the songs saved in the current Spotify user's 'Your Music' library.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_users_saved_tracks(
                market=market, limit=limit, offset=offset, request_options=request_options
            ),
        )

    def get_users_top_tracks(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingTrackObject:
        """Get the current user's top tracks based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_users_top_tracks(
                time_range=time_range, limit=limit, offset=offset, request_options=request_options
            ),
        )

    def remove_tracks_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Remove one or more items from a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.remove_tracks_playlist(playlist_id, body=body, request_options=request_options)
        )

    def remove_tracks_user(
        self,
        ids: str,
        *,
        body: RemoveTracksRequest | RemoveTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more tracks from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Track removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.remove_tracks_user(ids, body=body, request_options=request_options))

    def reorder_or_replace_playlists_tracks(
        self,
        playlist_id: str,
        *,
        uris: str | None = None,
        body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Either reorder or replace items in a playlist depending on the request's parameters. To reorder items,
        include ``range_start``, ``insert_before``, ``range_length`` and ``snapshot_id`` in the request's body. To
        replace items, include ``uris`` as either a query parameter or in the request's body. Replacing items in a
        playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a
        playlist. <br/> **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint,
        but have different parameters. These operations can't be applied together in a single request.

        Args:
            playlist_id: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            self._with_raw_response.reorder_or_replace_playlists_tracks(
                playlist_id, uris=uris, body=body, request_options=request_options
            ),
        )

    def save_tracks_user(
        self,
        ids: str,
        *,
        body: SaveTracksRequest | SaveTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more tracks to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Track saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(self._with_raw_response.save_tracks_user(ids, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> TracksWithRawResponse:
        return self._with_raw_response


class AsyncTracks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTracksWithRawResponse(client, server, auth)

    async def add_tracks_to_playlist(
        self,
        playlist_id: str,
        *,
        position: int | None = None,
        uris: str | None = None,
        body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Add one or more items to a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            position: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.add_tracks_to_playlist(
                playlist_id, position=position, uris=uris, body=body, request_options=request_options
            ),
        )

    async def check_users_saved_tracks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.check_users_saved_tracks(ids, request_options=request_options))

    async def get_an_albums_tracks(
        self,
        id_: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSimplifiedTrackObject:
        """Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number
        of tracks returned.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_an_albums_tracks(
                id_, market=market, limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def get_an_artists_top_tracks(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyTracks:
        """Get Spotify catalog information about an artist's top tracks by country.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_an_artists_top_tracks(id_, market=market, request_options=request_options)
        )

    async def get_audio_analysis(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AudioAnalysisObject:
        """Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s
        structure and musical content, including rhythm, pitch, and timbre.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Audio analysis for one track

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_audio_analysis(id_, request_options=request_options))

    async def get_audio_features(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AudioFeaturesObject:
        """Get audio feature information for a single track identified by its unique Spotify ID.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Audio features for one track

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_audio_features(id_, request_options=request_options))

    async def get_playlists_tracks(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingPlaylistTrackObject:
        """Get full details of the items of a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_playlists_tracks(
                playlist_id,
                market=market,
                fields=fields,
                limit=limit,
                offset=offset,
                additional_types=additional_types,
                request_options=request_options,
            ),
        )

    async def get_recommendations(
        self,
        *,
        limit: int | None = 20,
        market: str | None = None,
        seed_artists: str | None = None,
        seed_genres: str | None = None,
        seed_tracks: str | None = None,
        min_acousticness: float | None = None,
        max_acousticness: float | None = None,
        target_acousticness: float | None = None,
        min_danceability: float | None = None,
        max_danceability: float | None = None,
        target_danceability: float | None = None,
        min_duration_ms: int | None = None,
        max_duration_ms: int | None = None,
        target_duration_ms: int | None = None,
        min_energy: float | None = None,
        max_energy: float | None = None,
        target_energy: float | None = None,
        min_instrumentalness: float | None = None,
        max_instrumentalness: float | None = None,
        target_instrumentalness: float | None = None,
        min_key: int | None = None,
        max_key: int | None = None,
        target_key: int | None = None,
        min_liveness: float | None = None,
        max_liveness: float | None = None,
        target_liveness: float | None = None,
        min_loudness: float | None = None,
        max_loudness: float | None = None,
        target_loudness: float | None = None,
        min_mode: int | None = None,
        max_mode: int | None = None,
        target_mode: int | None = None,
        min_popularity: int | None = None,
        max_popularity: int | None = None,
        target_popularity: int | None = None,
        min_speechiness: float | None = None,
        max_speechiness: float | None = None,
        target_speechiness: float | None = None,
        min_tempo: float | None = None,
        max_tempo: float | None = None,
        target_tempo: float | None = None,
        min_time_signature: int | None = None,
        max_time_signature: int | None = None,
        target_time_signature: int | None = None,
        min_valence: float | None = None,
        max_valence: float | None = None,
        target_valence: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecommendationsObject:
        """Recommendations are generated based on the available information for a given seed entity and matched against
        similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will
        be returned together with pool size details.

        For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.

        Args:
            limit: Value sent with the request.
            market: Value sent with the request.
            seed_artists: Value sent with the request.
            seed_genres: Value sent with the request.
            seed_tracks: Value sent with the request.
            min_acousticness: Value sent with the request.
            max_acousticness: Value sent with the request.
            target_acousticness: Value sent with the request.
            min_danceability: Value sent with the request.
            max_danceability: Value sent with the request.
            target_danceability: Value sent with the request.
            min_duration_ms: Value sent with the request.
            max_duration_ms: Value sent with the request.
            target_duration_ms: Value sent with the request.
            min_energy: Value sent with the request.
            max_energy: Value sent with the request.
            target_energy: Value sent with the request.
            min_instrumentalness: Value sent with the request.
            max_instrumentalness: Value sent with the request.
            target_instrumentalness: Value sent with the request.
            min_key: Value sent with the request.
            max_key: Value sent with the request.
            target_key: Value sent with the request.
            min_liveness: Value sent with the request.
            max_liveness: Value sent with the request.
            target_liveness: Value sent with the request.
            min_loudness: Value sent with the request.
            max_loudness: Value sent with the request.
            target_loudness: Value sent with the request.
            min_mode: Value sent with the request.
            max_mode: Value sent with the request.
            target_mode: Value sent with the request.
            min_popularity: Value sent with the request.
            max_popularity: Value sent with the request.
            target_popularity: Value sent with the request.
            min_speechiness: Value sent with the request.
            max_speechiness: Value sent with the request.
            target_speechiness: Value sent with the request.
            min_tempo: Value sent with the request.
            max_tempo: Value sent with the request.
            target_tempo: Value sent with the request.
            min_time_signature: Value sent with the request.
            max_time_signature: Value sent with the request.
            target_time_signature: Value sent with the request.
            min_valence: Value sent with the request.
            max_valence: Value sent with the request.
            target_valence: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of recommendations

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_recommendations(
                limit=limit,
                market=market,
                seed_artists=seed_artists,
                seed_genres=seed_genres,
                seed_tracks=seed_tracks,
                min_acousticness=min_acousticness,
                max_acousticness=max_acousticness,
                target_acousticness=target_acousticness,
                min_danceability=min_danceability,
                max_danceability=max_danceability,
                target_danceability=target_danceability,
                min_duration_ms=min_duration_ms,
                max_duration_ms=max_duration_ms,
                target_duration_ms=target_duration_ms,
                min_energy=min_energy,
                max_energy=max_energy,
                target_energy=target_energy,
                min_instrumentalness=min_instrumentalness,
                max_instrumentalness=max_instrumentalness,
                target_instrumentalness=target_instrumentalness,
                min_key=min_key,
                max_key=max_key,
                target_key=target_key,
                min_liveness=min_liveness,
                max_liveness=max_liveness,
                target_liveness=target_liveness,
                min_loudness=min_loudness,
                max_loudness=max_loudness,
                target_loudness=target_loudness,
                min_mode=min_mode,
                max_mode=max_mode,
                target_mode=target_mode,
                min_popularity=min_popularity,
                max_popularity=max_popularity,
                target_popularity=target_popularity,
                min_speechiness=min_speechiness,
                max_speechiness=max_speechiness,
                target_speechiness=target_speechiness,
                min_tempo=min_tempo,
                max_tempo=max_tempo,
                target_tempo=target_tempo,
                min_time_signature=min_time_signature,
                max_time_signature=max_time_signature,
                target_time_signature=target_time_signature,
                min_valence=min_valence,
                max_valence=max_valence,
                target_valence=target_valence,
                request_options=request_options,
            ),
        )

    async def get_several_audio_features(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManyAudioFeatures:
        """Get audio features for multiple tracks based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of audio features

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_several_audio_features(ids, request_options=request_options))

    async def get_several_tracks(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ManyTracks:
        """Get Spotify catalog information for multiple tracks based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A set of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_several_tracks(ids, market=market, request_options=request_options)
        )

    async def get_track(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> TrackObject:
        """Get Spotify catalog information for a single track identified by its unique Spotify ID.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A track

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.get_track(id_, market=market, request_options=request_options))

    async def get_users_saved_tracks(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedTrackObject:
        """Get a list of the songs saved in the current Spotify user's 'Your Music' library.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_users_saved_tracks(
                market=market, limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def get_users_top_tracks(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingTrackObject:
        """Get the current user's top tracks based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_users_top_tracks(
                time_range=time_range, limit=limit, offset=offset, request_options=request_options
            ),
        )

    async def remove_tracks_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Remove one or more items from a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.remove_tracks_playlist(
                playlist_id, body=body, request_options=request_options
            ),
        )

    async def remove_tracks_user(
        self,
        ids: str,
        *,
        body: RemoveTracksRequest | RemoveTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more tracks from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Track removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.remove_tracks_user(ids, body=body, request_options=request_options))

    async def reorder_or_replace_playlists_tracks(
        self,
        playlist_id: str,
        *,
        uris: str | None = None,
        body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistSnapshotId:
        """Either reorder or replace items in a playlist depending on the request's parameters. To reorder items,
        include ``range_start``, ``insert_before``, ``range_length`` and ``snapshot_id`` in the request's body. To
        replace items, include ``uris`` as either a query parameter or in the request's body. Replacing items in a
        playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a
        playlist. <br/> **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint,
        but have different parameters. These operations can't be applied together in a single request.

        Args:
            playlist_id: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A snapshot ID for the playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(
            await self._with_raw_response.reorder_or_replace_playlists_tracks(
                playlist_id, uris=uris, body=body, request_options=request_options
            ),
        )

    async def save_tracks_user(
        self,
        ids: str,
        *,
        body: SaveTracksRequest | SaveTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more tracks to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Track saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return unwrap(await self._with_raw_response.save_tracks_user(ids, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncTracksWithRawResponse:
        return self._with_raw_response


class TracksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_tracks_to_playlist(
        self,
        playlist_id: str,
        *,
        position: int | None = None,
        uris: str | None = None,
        body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, AddTracksToPlaylistErrorBody]:
        """Add one or more items to a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            position: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[int | None]("position", position), param[str | None]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest | PlaylistsTracksRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistSnapshotId],
            error_mapper=add_tracks_to_playlist_error_mapper,
            request_options=request_options,
        )

    def check_users_saved_tracks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedTracksErrorBody]:
        """Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/tracks/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_tracks_error_mapper,
            request_options=request_options,
        )

    def get_an_albums_tracks(
        self,
        id_: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedTrackObject, GetAnAlbumsTracksErrorBody]:
        """Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number
        of tracks returned.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{id}/tracks"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=AnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[PagingSimplifiedTrackObject],
            error_mapper=get_an_albums_tracks_error_mapper,
            request_options=request_options,
        )

    def get_an_artists_top_tracks(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyTracks, GetAnArtistsTopTracksErrorBody]:
        """Get Spotify catalog information about an artist's top tracks by country.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/top-tracks"),
            path_params=[param[str]("id", id_)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyTracks],
            error_mapper=get_an_artists_top_tracks_error_mapper,
            request_options=request_options,
        )

    def get_audio_analysis(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AudioAnalysisObject, GetAudioAnalysisErrorBody]:
        """Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s
        structure and musical content, including rhythm, pitch, and timbre.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audio-analysis/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[AudioAnalysisObject],
            error_mapper=get_audio_analysis_error_mapper,
            request_options=request_options,
        )

    def get_audio_features(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AudioFeaturesObject, GetAudioFeaturesErrorBody]:
        """Get audio feature information for a single track identified by its unique Spotify ID.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audio-features/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[AudioFeaturesObject],
            error_mapper=get_audio_features_error_mapper,
            request_options=request_options,
        )

    def get_playlists_tracks(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingPlaylistTrackObject, GetPlaylistsTracksErrorBody]:
        """Get full details of the items of a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[
                param[str | None]("market", market),
                param[str | None]("fields", fields),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("additional_types", additional_types),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingPlaylistTrackObject],
            error_mapper=get_playlists_tracks_error_mapper,
            request_options=request_options,
        )

    def get_recommendations(
        self,
        *,
        limit: int | None = 20,
        market: str | None = None,
        seed_artists: str | None = None,
        seed_genres: str | None = None,
        seed_tracks: str | None = None,
        min_acousticness: float | None = None,
        max_acousticness: float | None = None,
        target_acousticness: float | None = None,
        min_danceability: float | None = None,
        max_danceability: float | None = None,
        target_danceability: float | None = None,
        min_duration_ms: int | None = None,
        max_duration_ms: int | None = None,
        target_duration_ms: int | None = None,
        min_energy: float | None = None,
        max_energy: float | None = None,
        target_energy: float | None = None,
        min_instrumentalness: float | None = None,
        max_instrumentalness: float | None = None,
        target_instrumentalness: float | None = None,
        min_key: int | None = None,
        max_key: int | None = None,
        target_key: int | None = None,
        min_liveness: float | None = None,
        max_liveness: float | None = None,
        target_liveness: float | None = None,
        min_loudness: float | None = None,
        max_loudness: float | None = None,
        target_loudness: float | None = None,
        min_mode: int | None = None,
        max_mode: int | None = None,
        target_mode: int | None = None,
        min_popularity: int | None = None,
        max_popularity: int | None = None,
        target_popularity: int | None = None,
        min_speechiness: float | None = None,
        max_speechiness: float | None = None,
        target_speechiness: float | None = None,
        min_tempo: float | None = None,
        max_tempo: float | None = None,
        target_tempo: float | None = None,
        min_time_signature: int | None = None,
        max_time_signature: int | None = None,
        target_time_signature: int | None = None,
        min_valence: float | None = None,
        max_valence: float | None = None,
        target_valence: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecommendationsObject, GetRecommendationsErrorBody]:
        """Recommendations are generated based on the available information for a given seed entity and matched against
        similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will
        be returned together with pool size details.

        For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.

        Args:
            limit: Value sent with the request.
            market: Value sent with the request.
            seed_artists: Value sent with the request.
            seed_genres: Value sent with the request.
            seed_tracks: Value sent with the request.
            min_acousticness: Value sent with the request.
            max_acousticness: Value sent with the request.
            target_acousticness: Value sent with the request.
            min_danceability: Value sent with the request.
            max_danceability: Value sent with the request.
            target_danceability: Value sent with the request.
            min_duration_ms: Value sent with the request.
            max_duration_ms: Value sent with the request.
            target_duration_ms: Value sent with the request.
            min_energy: Value sent with the request.
            max_energy: Value sent with the request.
            target_energy: Value sent with the request.
            min_instrumentalness: Value sent with the request.
            max_instrumentalness: Value sent with the request.
            target_instrumentalness: Value sent with the request.
            min_key: Value sent with the request.
            max_key: Value sent with the request.
            target_key: Value sent with the request.
            min_liveness: Value sent with the request.
            max_liveness: Value sent with the request.
            target_liveness: Value sent with the request.
            min_loudness: Value sent with the request.
            max_loudness: Value sent with the request.
            target_loudness: Value sent with the request.
            min_mode: Value sent with the request.
            max_mode: Value sent with the request.
            target_mode: Value sent with the request.
            min_popularity: Value sent with the request.
            max_popularity: Value sent with the request.
            target_popularity: Value sent with the request.
            min_speechiness: Value sent with the request.
            max_speechiness: Value sent with the request.
            target_speechiness: Value sent with the request.
            min_tempo: Value sent with the request.
            max_tempo: Value sent with the request.
            target_tempo: Value sent with the request.
            min_time_signature: Value sent with the request.
            max_time_signature: Value sent with the request.
            target_time_signature: Value sent with the request.
            min_valence: Value sent with the request.
            max_valence: Value sent with the request.
            target_valence: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/recommendations"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("market", market),
                param[str | None]("seed_artists", seed_artists),
                param[str | None]("seed_genres", seed_genres),
                param[str | None]("seed_tracks", seed_tracks),
                param[float | None]("min_acousticness", min_acousticness),
                param[float | None]("max_acousticness", max_acousticness),
                param[float | None]("target_acousticness", target_acousticness),
                param[float | None]("min_danceability", min_danceability),
                param[float | None]("max_danceability", max_danceability),
                param[float | None]("target_danceability", target_danceability),
                param[int | None]("min_duration_ms", min_duration_ms),
                param[int | None]("max_duration_ms", max_duration_ms),
                param[int | None]("target_duration_ms", target_duration_ms),
                param[float | None]("min_energy", min_energy),
                param[float | None]("max_energy", max_energy),
                param[float | None]("target_energy", target_energy),
                param[float | None]("min_instrumentalness", min_instrumentalness),
                param[float | None]("max_instrumentalness", max_instrumentalness),
                param[float | None]("target_instrumentalness", target_instrumentalness),
                param[int | None]("min_key", min_key),
                param[int | None]("max_key", max_key),
                param[int | None]("target_key", target_key),
                param[float | None]("min_liveness", min_liveness),
                param[float | None]("max_liveness", max_liveness),
                param[float | None]("target_liveness", target_liveness),
                param[float | None]("min_loudness", min_loudness),
                param[float | None]("max_loudness", max_loudness),
                param[float | None]("target_loudness", target_loudness),
                param[int | None]("min_mode", min_mode),
                param[int | None]("max_mode", max_mode),
                param[int | None]("target_mode", target_mode),
                param[int | None]("min_popularity", min_popularity),
                param[int | None]("max_popularity", max_popularity),
                param[int | None]("target_popularity", target_popularity),
                param[float | None]("min_speechiness", min_speechiness),
                param[float | None]("max_speechiness", max_speechiness),
                param[float | None]("target_speechiness", target_speechiness),
                param[float | None]("min_tempo", min_tempo),
                param[float | None]("max_tempo", max_tempo),
                param[float | None]("target_tempo", target_tempo),
                param[int | None]("min_time_signature", min_time_signature),
                param[int | None]("max_time_signature", max_time_signature),
                param[int | None]("target_time_signature", target_time_signature),
                param[float | None]("min_valence", min_valence),
                param[float | None]("max_valence", max_valence),
                param[float | None]("target_valence", target_valence),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[RecommendationsObject],
            error_mapper=get_recommendations_error_mapper,
            request_options=request_options,
        )

    def get_several_audio_features(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyAudioFeatures, GetSeveralAudioFeaturesErrorBody]:
        """Get audio features for multiple tracks based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audio-features"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyAudioFeatures],
            error_mapper=get_several_audio_features_error_mapper,
            request_options=request_options,
        )

    def get_several_tracks(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyTracks, GetSeveralTracksErrorBody]:
        """Get Spotify catalog information for multiple tracks based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tracks"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[ManyTracks],
            error_mapper=get_several_tracks_error_mapper,
            request_options=request_options,
        )

    def get_track(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrackObject, GetTrackErrorBody]:
        """Get Spotify catalog information for a single track identified by its unique Spotify ID.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tracks/{id}"),
            path_params=[param[str]("id", id_)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=AnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=json_decoder[TrackObject],
            error_mapper=get_track_error_mapper,
            request_options=request_options,
        )

    def get_users_saved_tracks(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedTrackObject, GetUsersSavedTracksErrorBody]:
        """Get a list of the songs saved in the current Spotify user's 'Your Music' library.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/tracks"),
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedTrackObject],
            error_mapper=get_users_saved_tracks_error_mapper,
            request_options=request_options,
        )

    def get_users_top_tracks(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingTrackObject, GetUsersTopTracksErrorBody]:
        """Get the current user's top tracks based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/top/tracks"),
            query_params=[
                param[str | None]("time_range", time_range),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingTrackObject],
            error_mapper=get_users_top_tracks_error_mapper,
            request_options=request_options,
        )

    def remove_tracks_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, RemoveTracksPlaylistErrorBody]:
        """Remove one or more items from a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistSnapshotId],
            error_mapper=remove_tracks_playlist_error_mapper,
            request_options=request_options,
        )

    def remove_tracks_user(
        self,
        ids: str,
        *,
        body: RemoveTracksRequest | RemoveTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveTracksUserErrorBody]:
        """Remove one or more tracks from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/tracks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveTracksRequest | RemoveTracksRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_tracks_user_error_mapper,
            request_options=request_options,
        )

    def reorder_or_replace_playlists_tracks(
        self,
        playlist_id: str,
        *,
        uris: str | None = None,
        body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, ReorderOrReplacePlaylistsTracksErrorBody]:
        """Either reorder or replace items in a playlist depending on the request's parameters. To reorder items,
        include ``range_start``, ``insert_before``, ``range_length`` and ``snapshot_id`` in the request's body. To
        replace items, include ``uris`` as either a query parameter or in the request's body. Replacing items in a
        playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a
        playlist. <br/> **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint,
        but have different parameters. These operations can't be applied together in a single request.

        Args:
            playlist_id: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[str | None]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistSnapshotId],
            error_mapper=reorder_or_replace_playlists_tracks_error_mapper,
            request_options=request_options,
        )

    def save_tracks_user(
        self,
        ids: str,
        *,
        body: SaveTracksRequest | SaveTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveTracksUserErrorBody]:
        """Save one or more tracks to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/tracks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveTracksRequest | SaveTracksRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_tracks_user_error_mapper,
            request_options=request_options,
        )


class AsyncTracksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_tracks_to_playlist(
        self,
        playlist_id: str,
        *,
        position: int | None = None,
        uris: str | None = None,
        body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, AddTracksToPlaylistErrorBody]:
        """Add one or more items to a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            position: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[int | None]("position", position), param[str | None]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest | PlaylistsTracksRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PlaylistSnapshotId],
            error_mapper=add_tracks_to_playlist_error_mapper,
            request_options=request_options,
        )

    async def check_users_saved_tracks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedTracksErrorBody]:
        """Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/tracks/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[list[bool]],
            error_mapper=check_users_saved_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_an_albums_tracks(
        self,
        id_: str,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSimplifiedTrackObject, GetAnAlbumsTracksErrorBody]:
        """Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number
        of tracks returned.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{id}/tracks"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=async_json_decoder[PagingSimplifiedTrackObject],
            error_mapper=get_an_albums_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_an_artists_top_tracks(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyTracks, GetAnArtistsTopTracksErrorBody]:
        """Get Spotify catalog information about an artist's top tracks by country.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/artists/{id}/top-tracks"),
            path_params=[param[str]("id", id_)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[ManyTracks],
            error_mapper=get_an_artists_top_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_audio_analysis(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AudioAnalysisObject, GetAudioAnalysisErrorBody]:
        """Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s
        structure and musical content, including rhythm, pitch, and timbre.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audio-analysis/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[AudioAnalysisObject],
            error_mapper=get_audio_analysis_error_mapper,
            request_options=request_options,
        )

    async def get_audio_features(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AudioFeaturesObject, GetAudioFeaturesErrorBody]:
        """Get audio feature information for a single track identified by its unique Spotify ID.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audio-features/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[AudioFeaturesObject],
            error_mapper=get_audio_features_error_mapper,
            request_options=request_options,
        )

    async def get_playlists_tracks(
        self,
        playlist_id: str,
        *,
        market: str | None = None,
        fields: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        additional_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingPlaylistTrackObject, GetPlaylistsTracksErrorBody]:
        """Get full details of the items of a playlist owned by a Spotify user.

        Args:
            playlist_id: Value sent with the request.
            market: Value sent with the request.
            fields: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            additional_types: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[
                param[str | None]("market", market),
                param[str | None]("fields", fields),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("additional_types", additional_types),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingPlaylistTrackObject],
            error_mapper=get_playlists_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_recommendations(
        self,
        *,
        limit: int | None = 20,
        market: str | None = None,
        seed_artists: str | None = None,
        seed_genres: str | None = None,
        seed_tracks: str | None = None,
        min_acousticness: float | None = None,
        max_acousticness: float | None = None,
        target_acousticness: float | None = None,
        min_danceability: float | None = None,
        max_danceability: float | None = None,
        target_danceability: float | None = None,
        min_duration_ms: int | None = None,
        max_duration_ms: int | None = None,
        target_duration_ms: int | None = None,
        min_energy: float | None = None,
        max_energy: float | None = None,
        target_energy: float | None = None,
        min_instrumentalness: float | None = None,
        max_instrumentalness: float | None = None,
        target_instrumentalness: float | None = None,
        min_key: int | None = None,
        max_key: int | None = None,
        target_key: int | None = None,
        min_liveness: float | None = None,
        max_liveness: float | None = None,
        target_liveness: float | None = None,
        min_loudness: float | None = None,
        max_loudness: float | None = None,
        target_loudness: float | None = None,
        min_mode: int | None = None,
        max_mode: int | None = None,
        target_mode: int | None = None,
        min_popularity: int | None = None,
        max_popularity: int | None = None,
        target_popularity: int | None = None,
        min_speechiness: float | None = None,
        max_speechiness: float | None = None,
        target_speechiness: float | None = None,
        min_tempo: float | None = None,
        max_tempo: float | None = None,
        target_tempo: float | None = None,
        min_time_signature: int | None = None,
        max_time_signature: int | None = None,
        target_time_signature: int | None = None,
        min_valence: float | None = None,
        max_valence: float | None = None,
        target_valence: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecommendationsObject, GetRecommendationsErrorBody]:
        """Recommendations are generated based on the available information for a given seed entity and matched against
        similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will
        be returned together with pool size details.

        For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.

        Args:
            limit: Value sent with the request.
            market: Value sent with the request.
            seed_artists: Value sent with the request.
            seed_genres: Value sent with the request.
            seed_tracks: Value sent with the request.
            min_acousticness: Value sent with the request.
            max_acousticness: Value sent with the request.
            target_acousticness: Value sent with the request.
            min_danceability: Value sent with the request.
            max_danceability: Value sent with the request.
            target_danceability: Value sent with the request.
            min_duration_ms: Value sent with the request.
            max_duration_ms: Value sent with the request.
            target_duration_ms: Value sent with the request.
            min_energy: Value sent with the request.
            max_energy: Value sent with the request.
            target_energy: Value sent with the request.
            min_instrumentalness: Value sent with the request.
            max_instrumentalness: Value sent with the request.
            target_instrumentalness: Value sent with the request.
            min_key: Value sent with the request.
            max_key: Value sent with the request.
            target_key: Value sent with the request.
            min_liveness: Value sent with the request.
            max_liveness: Value sent with the request.
            target_liveness: Value sent with the request.
            min_loudness: Value sent with the request.
            max_loudness: Value sent with the request.
            target_loudness: Value sent with the request.
            min_mode: Value sent with the request.
            max_mode: Value sent with the request.
            target_mode: Value sent with the request.
            min_popularity: Value sent with the request.
            max_popularity: Value sent with the request.
            target_popularity: Value sent with the request.
            min_speechiness: Value sent with the request.
            max_speechiness: Value sent with the request.
            target_speechiness: Value sent with the request.
            min_tempo: Value sent with the request.
            max_tempo: Value sent with the request.
            target_tempo: Value sent with the request.
            min_time_signature: Value sent with the request.
            max_time_signature: Value sent with the request.
            target_time_signature: Value sent with the request.
            min_valence: Value sent with the request.
            max_valence: Value sent with the request.
            target_valence: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/recommendations"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("market", market),
                param[str | None]("seed_artists", seed_artists),
                param[str | None]("seed_genres", seed_genres),
                param[str | None]("seed_tracks", seed_tracks),
                param[float | None]("min_acousticness", min_acousticness),
                param[float | None]("max_acousticness", max_acousticness),
                param[float | None]("target_acousticness", target_acousticness),
                param[float | None]("min_danceability", min_danceability),
                param[float | None]("max_danceability", max_danceability),
                param[float | None]("target_danceability", target_danceability),
                param[int | None]("min_duration_ms", min_duration_ms),
                param[int | None]("max_duration_ms", max_duration_ms),
                param[int | None]("target_duration_ms", target_duration_ms),
                param[float | None]("min_energy", min_energy),
                param[float | None]("max_energy", max_energy),
                param[float | None]("target_energy", target_energy),
                param[float | None]("min_instrumentalness", min_instrumentalness),
                param[float | None]("max_instrumentalness", max_instrumentalness),
                param[float | None]("target_instrumentalness", target_instrumentalness),
                param[int | None]("min_key", min_key),
                param[int | None]("max_key", max_key),
                param[int | None]("target_key", target_key),
                param[float | None]("min_liveness", min_liveness),
                param[float | None]("max_liveness", max_liveness),
                param[float | None]("target_liveness", target_liveness),
                param[float | None]("min_loudness", min_loudness),
                param[float | None]("max_loudness", max_loudness),
                param[float | None]("target_loudness", target_loudness),
                param[int | None]("min_mode", min_mode),
                param[int | None]("max_mode", max_mode),
                param[int | None]("target_mode", target_mode),
                param[int | None]("min_popularity", min_popularity),
                param[int | None]("max_popularity", max_popularity),
                param[int | None]("target_popularity", target_popularity),
                param[float | None]("min_speechiness", min_speechiness),
                param[float | None]("max_speechiness", max_speechiness),
                param[float | None]("target_speechiness", target_speechiness),
                param[float | None]("min_tempo", min_tempo),
                param[float | None]("max_tempo", max_tempo),
                param[float | None]("target_tempo", target_tempo),
                param[int | None]("min_time_signature", min_time_signature),
                param[int | None]("max_time_signature", max_time_signature),
                param[int | None]("target_time_signature", target_time_signature),
                param[float | None]("min_valence", min_valence),
                param[float | None]("max_valence", max_valence),
                param[float | None]("target_valence", target_valence),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[RecommendationsObject],
            error_mapper=get_recommendations_error_mapper,
            request_options=request_options,
        )

    async def get_several_audio_features(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyAudioFeatures, GetSeveralAudioFeaturesErrorBody]:
        """Get audio features for multiple tracks based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/audio-features"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[ManyAudioFeatures],
            error_mapper=get_several_audio_features_error_mapper,
            request_options=request_options,
        )

    async def get_several_tracks(
        self, ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManyTracks, GetSeveralTracksErrorBody]:
        """Get Spotify catalog information for multiple tracks based on their Spotify IDs.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tracks"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[ManyTracks],
            error_mapper=get_several_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_track(
        self, id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrackObject, GetTrackErrorBody]:
        """Get Spotify catalog information for a single track identified by its unique Spotify ID.

        Args:
            id_: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tracks/{id}"),
            path_params=[param[str]("id", id_)],
            query_params=[param[str | None]("market", market)],
            auth_scheme=AsyncAnySchemes(self._auth.oauth_2_0, self._auth.oauth_2_0_client_credentials),
            decoder=async_json_decoder[TrackObject],
            error_mapper=get_track_error_mapper,
            request_options=request_options,
        )

    async def get_users_saved_tracks(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedTrackObject, GetUsersSavedTracksErrorBody]:
        """Get a list of the songs saved in the current Spotify user's 'Your Music' library.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/tracks"),
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingSavedTrackObject],
            error_mapper=get_users_saved_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_users_top_tracks(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingTrackObject, GetUsersTopTracksErrorBody]:
        """Get the current user's top tracks based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/top/tracks"),
            query_params=[
                param[str | None]("time_range", time_range),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PagingTrackObject],
            error_mapper=get_users_top_tracks_error_mapper,
            request_options=request_options,
        )

    async def remove_tracks_playlist(
        self,
        playlist_id: str,
        *,
        body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, RemoveTracksPlaylistErrorBody]:
        """Remove one or more items from a user's playlist.

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PlaylistSnapshotId],
            error_mapper=remove_tracks_playlist_error_mapper,
            request_options=request_options,
        )

    async def remove_tracks_user(
        self,
        ids: str,
        *,
        body: RemoveTracksRequest | RemoveTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveTracksUserErrorBody]:
        """Remove one or more tracks from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/tracks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveTracksRequest | RemoveTracksRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=remove_tracks_user_error_mapper,
            request_options=request_options,
        )

    async def reorder_or_replace_playlists_tracks(
        self,
        playlist_id: str,
        *,
        uris: str | None = None,
        body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistSnapshotId, ReorderOrReplacePlaylistsTracksErrorBody]:
        """Either reorder or replace items in a playlist depending on the request's parameters. To reorder items,
        include ``range_start``, ``insert_before``, ``range_length`` and ``snapshot_id`` in the request's body. To
        replace items, include ``uris`` as either a query parameter or in the request's body. Replacing items in a
        playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a
        playlist. <br/> **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint,
        but have different parameters. These operations can't be applied together in a single request.

        Args:
            playlist_id: Value sent with the request.
            uris: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}/tracks"),
            path_params=[param[str]("playlist_id", playlist_id)],
            query_params=[param[str | None]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_json_decoder[PlaylistSnapshotId],
            error_mapper=reorder_or_replace_playlists_tracks_error_mapper,
            request_options=request_options,
        )

    async def save_tracks_user(
        self,
        ids: str,
        *,
        body: SaveTracksRequest | SaveTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveTracksUserErrorBody]:
        """Save one or more tracks to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/tracks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveTracksRequest | SaveTracksRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=async_empty_response,
            error_mapper=save_tracks_user_error_mapper,
            request_options=request_options,
        )
