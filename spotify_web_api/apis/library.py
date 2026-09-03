from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.change_playlist_details_error import ChangePlaylistDetailsErrorBody, change_playlist_details_error_mapper
from ..errors.check_current_user_follows_error import (
    CheckCurrentUserFollowsErrorBody,
    check_current_user_follows_error_mapper,
)
from ..errors.check_users_saved_albums_error import (
    CheckUsersSavedAlbumsErrorBody,
    check_users_saved_albums_error_mapper,
)
from ..errors.check_users_saved_audiobooks_error import (
    CheckUsersSavedAudiobooksErrorBody,
    check_users_saved_audiobooks_error_mapper,
)
from ..errors.check_users_saved_episodes_error import (
    CheckUsersSavedEpisodesErrorBody,
    check_users_saved_episodes_error_mapper,
)
from ..errors.check_users_saved_shows_error import CheckUsersSavedShowsErrorBody, check_users_saved_shows_error_mapper
from ..errors.check_users_saved_tracks_error import (
    CheckUsersSavedTracksErrorBody,
    check_users_saved_tracks_error_mapper,
)
from ..errors.create_playlist_error import CreatePlaylistErrorBody, create_playlist_error_mapper
from ..errors.follow_artists_users_error import FollowArtistsUsersErrorBody, follow_artists_users_error_mapper
from ..errors.get_a_list_of_current_users_playlists_error import (
    GetAListOfCurrentUsersPlaylistsErrorBody,
    get_a_list_of_current_users_playlists_error_mapper,
)
from ..errors.get_followed_error import GetFollowedErrorBody, get_followed_error_mapper
from ..errors.get_users_saved_albums_error import GetUsersSavedAlbumsErrorBody, get_users_saved_albums_error_mapper
from ..errors.get_users_saved_audiobooks_error import (
    GetUsersSavedAudiobooksErrorBody,
    get_users_saved_audiobooks_error_mapper,
)
from ..errors.get_users_saved_episodes_error import (
    GetUsersSavedEpisodesErrorBody,
    get_users_saved_episodes_error_mapper,
)
from ..errors.get_users_saved_shows_error import GetUsersSavedShowsErrorBody, get_users_saved_shows_error_mapper
from ..errors.get_users_saved_tracks_error import GetUsersSavedTracksErrorBody, get_users_saved_tracks_error_mapper
from ..errors.get_users_top_artists_error import GetUsersTopArtistsErrorBody, get_users_top_artists_error_mapper
from ..errors.get_users_top_tracks_error import GetUsersTopTracksErrorBody, get_users_top_tracks_error_mapper
from ..errors.remove_albums_user_error import RemoveAlbumsUserErrorBody, remove_albums_user_error_mapper
from ..errors.remove_audiobooks_user_error import RemoveAudiobooksUserErrorBody, remove_audiobooks_user_error_mapper
from ..errors.remove_episodes_user_error import RemoveEpisodesUserErrorBody, remove_episodes_user_error_mapper
from ..errors.remove_shows_user_error import RemoveShowsUserErrorBody, remove_shows_user_error_mapper
from ..errors.remove_tracks_user_error import RemoveTracksUserErrorBody, remove_tracks_user_error_mapper
from ..errors.save_albums_user_error import SaveAlbumsUserErrorBody, save_albums_user_error_mapper
from ..errors.save_audiobooks_user_error import SaveAudiobooksUserErrorBody, save_audiobooks_user_error_mapper
from ..errors.save_episodes_user_error import SaveEpisodesUserErrorBody, save_episodes_user_error_mapper
from ..errors.save_shows_user_error import SaveShowsUserErrorBody, save_shows_user_error_mapper
from ..errors.save_tracks_user_error import SaveTracksUserErrorBody, save_tracks_user_error_mapper
from ..errors.unfollow_artists_users_error import UnfollowArtistsUsersErrorBody, unfollow_artists_users_error_mapper
from ..models.cursor_paged_artists import CursorPagedArtists
from ..models.enums.item_type1 import ItemType1OrStr
from ..models.enums.item_type2 import ItemType2OrStr
from ..models.enums.item_type3 import ItemType3OrStr
from ..models.follow_artists_or_users_request import FollowArtistsOrUsersRequest, FollowArtistsOrUsersRequestDict
from ..models.paging_artist_object import PagingArtistObject
from ..models.paging_playlist_object import PagingPlaylistObject
from ..models.paging_saved_album_object import PagingSavedAlbumObject
from ..models.paging_saved_audiobook_object import PagingSavedAudiobookObject
from ..models.paging_saved_episode_object import PagingSavedEpisodeObject
from ..models.paging_saved_show_object import PagingSavedShowObject
from ..models.paging_saved_track_object import PagingSavedTrackObject
from ..models.paging_track_object import PagingTrackObject
from ..models.playlist_object import PlaylistObject
from ..models.playlists_request import PlaylistsRequest, PlaylistsRequestDict
from ..models.remove_albums_request import RemoveAlbumsRequest, RemoveAlbumsRequestDict
from ..models.remove_episodes_request import RemoveEpisodesRequest, RemoveEpisodesRequestDict
from ..models.remove_shows_request import RemoveShowsRequest, RemoveShowsRequestDict
from ..models.remove_tracks_request import RemoveTracksRequest, RemoveTracksRequestDict
from ..models.save_albums_request import SaveAlbumsRequest, SaveAlbumsRequestDict
from ..models.save_episodes_request import SaveEpisodesRequest, SaveEpisodesRequestDict
from ..models.save_shows_request import SaveShowsRequest, SaveShowsRequestDict
from ..models.save_tracks_request import SaveTracksRequest, SaveTracksRequestDict
from ..models.unfollow_artists_or_users_request import UnfollowArtistsOrUsersRequest, UnfollowArtistsOrUsersRequestDict
from ..models.users_playlists_request import UsersPlaylistsRequest, UsersPlaylistsRequestDict
from ..server.server import Server


class Library:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LibraryWithRawResponse(client, server, auth)

    def change_playlist_details(
        self,
        playlist_id: str,
        *,
        body: PlaylistsRequest | PlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Change a playlist's name and public/private state. (The user must, of course, own the playlist.)

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Playlist updated

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.change_playlist_details(
            playlist_id, body=body, request_options=request_options
        ).unwrap()

    def check_current_user_follows(
        self, type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check to see if the current user is following one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.check_current_user_follows(type_, ids, request_options=request_options).unwrap()

    def check_users_saved_albums(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]:
        """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.check_users_saved_albums(ids, request_options=request_options).unwrap()

    def check_users_saved_audiobooks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more audiobooks are already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.check_users_saved_audiobooks(ids, request_options=request_options).unwrap()

    def check_users_saved_episodes(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
        This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or
        issues that you discover, in our `developer community forum
        <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__..

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.check_users_saved_episodes(ids, request_options=request_options).unwrap()

    def check_users_saved_shows(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]:
        """Check if one or more shows is already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.check_users_saved_shows(ids, request_options=request_options).unwrap()

    def check_users_saved_tracks(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]:
        """Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.check_users_saved_tracks(ids, request_options=request_options).unwrap()

    def create_playlist(
        self,
        user_id: str,
        *,
        body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistObject:
        """Create a playlist for a Spotify user. (The playlist will be empty until you `add tracks
        <https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist>`__.) Each user is
        generally limited to a maximum of 11000 playlists.

        Args:
            user_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.create_playlist(user_id, body=body, request_options=request_options).unwrap()

    def follow_artists_users(
        self,
        type_: ItemType2OrStr,
        ids: str,
        *,
        body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Add the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Artist or user followed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.follow_artists_users(
            type_, ids, body=body, request_options=request_options
        ).unwrap()

    def get_a_list_of_current_users_playlists(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingPlaylistObject:
        """Get a list of the playlists owned or followed by the current Spotify user.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of playlists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_a_list_of_current_users_playlists(
            limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_followed(
        self,
        type_: ItemType1OrStr,
        *,
        after: str | None = None,
        limit: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CursorPagedArtists:
        """Get the current user's followed artists.

        Args:
            type_: Value sent with the request.
            after: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_followed(
            type_, after=after, limit=limit, request_options=request_options
        ).unwrap()

    def get_users_saved_albums(
        self,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        market: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedAlbumObject:
        """Get a list of the albums saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_users_saved_albums(
            limit=limit, offset=offset, market=market, request_options=request_options
        ).unwrap()

    def get_users_saved_audiobooks(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingSavedAudiobookObject:
        """Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of saved audiobooks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_users_saved_audiobooks(
            limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_users_saved_episodes(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedEpisodeObject:
        """Get a list of the episodes saved in the current Spotify user's library.<br/> This API endpoint is in __beta__
        and could change without warning. Please share any feedback that you have, or issues that you discover, in our
        `developer community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of episodes

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_users_saved_episodes(
            market=market, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_users_saved_shows(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingSavedShowObject:
        """Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the
        number of shows returned.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of shows

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_users_saved_shows(
            limit=limit, offset=offset, request_options=request_options
        ).unwrap()

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_users_saved_tracks(
            market=market, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_users_top_artists(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingArtistObject:
        """Get the current user's top artists based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_users_top_artists(
            time_range=time_range, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.get_users_top_tracks(
            time_range=time_range, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def remove_albums_user(
        self,
        ids: str,
        *,
        body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more albums from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Album(s) have been removed from the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.remove_albums_user(ids, body=body, request_options=request_options).unwrap()

    def remove_audiobooks_user(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove one or more audiobooks from the Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Audiobook(s) have been removed from the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.remove_audiobooks_user(ids, request_options=request_options).unwrap()

    def remove_episodes_user(
        self,
        ids: str,
        *,
        body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more episodes from the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Episode removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.remove_episodes_user(ids, body=body, request_options=request_options).unwrap()

    def remove_shows_user(
        self,
        ids: str,
        *,
        market: str | None = None,
        body: RemoveShowsRequest | RemoveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete one or more shows from current Spotify user's library.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Show removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.remove_shows_user(
            ids, market=market, body=body, request_options=request_options
        ).unwrap()

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Track removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.remove_tracks_user(ids, body=body, request_options=request_options).unwrap()

    def save_albums_user(
        self,
        ids: str,
        *,
        body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more albums to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The album is saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.save_albums_user(ids, body=body, request_options=request_options).unwrap()

    def save_audiobooks_user(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Save one or more audiobooks to the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Audiobook(s) are saved to the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.save_audiobooks_user(ids, request_options=request_options).unwrap()

    def save_episodes_user(
        self,
        ids: str,
        *,
        body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more episodes to the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Episode saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.save_episodes_user(ids, body=body, request_options=request_options).unwrap()

    def save_shows_user(
        self,
        ids: str,
        *,
        body: SaveShowsRequest | SaveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more shows to current Spotify user's library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Show saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.save_shows_user(ids, body=body, request_options=request_options).unwrap()

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Track saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.save_tracks_user(ids, body=body, request_options=request_options).unwrap()

    def unfollow_artists_users(
        self,
        type_: ItemType3OrStr,
        ids: str,
        *,
        body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Artist or user unfollowed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return self._with_raw_response.unfollow_artists_users(
            type_, ids, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LibraryWithRawResponse:
        return self._with_raw_response


class AsyncLibrary:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLibraryWithRawResponse(client, server, auth)

    async def change_playlist_details(
        self,
        playlist_id: str,
        *,
        body: PlaylistsRequest | PlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Change a playlist's name and public/private state. (The user must, of course, own the playlist.)

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Playlist updated

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.change_playlist_details(
                playlist_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def check_current_user_follows(
        self, type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check to see if the current user is following one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.check_current_user_follows(type_, ids, request_options=request_options)
        ).unwrap()

    async def check_users_saved_albums(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.check_users_saved_albums(ids, request_options=request_options)).unwrap()

    async def check_users_saved_audiobooks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more audiobooks are already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.check_users_saved_audiobooks(ids, request_options=request_options)
        ).unwrap()

    async def check_users_saved_episodes(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
        This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or
        issues that you discover, in our `developer community forum
        <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__..

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.check_users_saved_episodes(ids, request_options=request_options)).unwrap()

    async def check_users_saved_shows(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more shows is already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.check_users_saved_shows(ids, request_options=request_options)).unwrap()

    async def check_users_saved_tracks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[bool]:
        """Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Array of booleans

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.check_users_saved_tracks(ids, request_options=request_options)).unwrap()

    async def create_playlist(
        self,
        user_id: str,
        *,
        body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlaylistObject:
        """Create a playlist for a Spotify user. (The playlist will be empty until you `add tracks
        <https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist>`__.) Each user is
        generally limited to a maximum of 11000 playlists.

        Args:
            user_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A playlist

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.create_playlist(user_id, body=body, request_options=request_options)
        ).unwrap()

    async def follow_artists_users(
        self,
        type_: ItemType2OrStr,
        ids: str,
        *,
        body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Add the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Artist or user followed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.follow_artists_users(type_, ids, body=body, request_options=request_options)
        ).unwrap()

    async def get_a_list_of_current_users_playlists(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingPlaylistObject:
        """Get a list of the playlists owned or followed by the current Spotify user.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of playlists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_a_list_of_current_users_playlists(
                limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def get_followed(
        self,
        type_: ItemType1OrStr,
        *,
        after: str | None = None,
        limit: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CursorPagedArtists:
        """Get the current user's followed artists.

        Args:
            type_: Value sent with the request.
            after: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A paged set of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_followed(type_, after=after, limit=limit, request_options=request_options)
        ).unwrap()

    async def get_users_saved_albums(
        self,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        market: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedAlbumObject:
        """Get a list of the albums saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of albums

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_users_saved_albums(
                limit=limit, offset=offset, market=market, request_options=request_options
            )
        ).unwrap()

    async def get_users_saved_audiobooks(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingSavedAudiobookObject:
        """Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of saved audiobooks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_users_saved_audiobooks(
                limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def get_users_saved_episodes(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingSavedEpisodeObject:
        """Get a list of the episodes saved in the current Spotify user's library.<br/> This API endpoint is in __beta__
        and could change without warning. Please share any feedback that you have, or issues that you discover, in our
        `developer community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of episodes

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_users_saved_episodes(
                market=market, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def get_users_saved_shows(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> PagingSavedShowObject:
        """Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the
        number of shows returned.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of shows

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_users_saved_shows(
                limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_users_saved_tracks(
                market=market, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def get_users_top_artists(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PagingArtistObject:
        """Get the current user's top artists based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of artists

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_users_top_artists(
                time_range=time_range, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pages of tracks

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.get_users_top_tracks(
                time_range=time_range, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def remove_albums_user(
        self,
        ids: str,
        *,
        body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more albums from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Album(s) have been removed from the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.remove_albums_user(ids, body=body, request_options=request_options)
        ).unwrap()

    async def remove_audiobooks_user(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove one or more audiobooks from the Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Audiobook(s) have been removed from the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.remove_audiobooks_user(ids, request_options=request_options)).unwrap()

    async def remove_episodes_user(
        self,
        ids: str,
        *,
        body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove one or more episodes from the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Episode removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.remove_episodes_user(ids, body=body, request_options=request_options)
        ).unwrap()

    async def remove_shows_user(
        self,
        ids: str,
        *,
        market: str | None = None,
        body: RemoveShowsRequest | RemoveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete one or more shows from current Spotify user's library.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Show removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.remove_shows_user(
                ids, market=market, body=body, request_options=request_options
            )
        ).unwrap()

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Track removed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.remove_tracks_user(ids, body=body, request_options=request_options)
        ).unwrap()

    async def save_albums_user(
        self,
        ids: str,
        *,
        body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more albums to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The album is saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.save_albums_user(ids, body=body, request_options=request_options)
        ).unwrap()

    async def save_audiobooks_user(self, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Save one or more audiobooks to the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Audiobook(s) are saved to the library

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.save_audiobooks_user(ids, request_options=request_options)).unwrap()

    async def save_episodes_user(
        self,
        ids: str,
        *,
        body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more episodes to the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Episode saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.save_episodes_user(ids, body=body, request_options=request_options)
        ).unwrap()

    async def save_shows_user(
        self,
        ids: str,
        *,
        body: SaveShowsRequest | SaveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Save one or more shows to current Spotify user's library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Show saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (await self._with_raw_response.save_shows_user(ids, body=body, request_options=request_options)).unwrap()

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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Track saved

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.save_tracks_user(ids, body=body, request_options=request_options)
        ).unwrap()

    async def unfollow_artists_users(
        self,
        type_: ItemType3OrStr,
        ids: str,
        *,
        body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Artist or user unfollowed

        Raises:
            ApiError: Bad or expired token. This can happen if the user revoked a token or the access token has expired.
                You should re-authenticate the user. Bad OAuth request (wrong consumer key, bad nonce, expired
                timestamp...). Unfortunately, re-authenticating the user won't help here. The app has exceeded its rate
                limits. ``error`` is ``Unauthorized1 | Forbidden1 | TooManyRequests1 | RawError``."""
        return (
            await self._with_raw_response.unfollow_artists_users(type_, ids, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLibraryWithRawResponse:
        return self._with_raw_response


class LibraryWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def change_playlist_details(
        self,
        playlist_id: str,
        *,
        body: PlaylistsRequest | PlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ChangePlaylistDetailsErrorBody]:
        """Change a playlist's name and public/private state. (The user must, of course, own the playlist.)

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsRequest | PlaylistsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=change_playlist_details_error_mapper,
            request_options=request_options,
        )

    def check_current_user_follows(
        self, type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckCurrentUserFollowsErrorBody]:
        """Check to see if the current user is following one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following/contains"),
            query_params=[param[ItemType3OrStr]("type", type_), param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_current_user_follows_error_mapper,
            request_options=request_options,
        )

    def check_users_saved_albums(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedAlbumsErrorBody]:
        """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_albums_error_mapper,
            request_options=request_options,
        )

    def check_users_saved_audiobooks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedAudiobooksErrorBody]:
        """Check if one or more audiobooks are already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/audiobooks/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_audiobooks_error_mapper,
            request_options=request_options,
        )

    def check_users_saved_episodes(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedEpisodesErrorBody]:
        """Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
        This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or
        issues that you discover, in our `developer community forum
        <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__..

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/episodes/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_episodes_error_mapper,
            request_options=request_options,
        )

    def check_users_saved_shows(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedShowsErrorBody]:
        """Check if one or more shows is already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/shows/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_shows_error_mapper,
            request_options=request_options,
        )

    def check_users_saved_tracks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedTracksErrorBody]:
        """Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

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

    def create_playlist(
        self,
        user_id: str,
        *,
        body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistObject, CreatePlaylistErrorBody]:
        """Create a playlist for a Spotify user. (The playlist will be empty until you `add tracks
        <https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist>`__.) Each user is
        generally limited to a maximum of 11000 playlists.

        Args:
            user_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/playlists"),
            path_params=[param[str]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPlaylistsRequest | UsersPlaylistsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistObject],
            error_mapper=create_playlist_error_mapper,
            request_options=request_options,
        )

    def follow_artists_users(
        self,
        type_: ItemType2OrStr,
        ids: str,
        *,
        body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, FollowArtistsUsersErrorBody]:
        """Add the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/following"),
            query_params=[param[ItemType2OrStr]("type", type_), param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=follow_artists_users_error_mapper,
            request_options=request_options,
        )

    def get_a_list_of_current_users_playlists(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingPlaylistObject, GetAListOfCurrentUsersPlaylistsErrorBody]:
        """Get a list of the playlists owned or followed by the current Spotify user.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/playlists"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingPlaylistObject],
            error_mapper=get_a_list_of_current_users_playlists_error_mapper,
            request_options=request_options,
        )

    def get_followed(
        self,
        type_: ItemType1OrStr,
        *,
        after: str | None = None,
        limit: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CursorPagedArtists, GetFollowedErrorBody]:
        """Get the current user's followed artists.

        Args:
            type_: Value sent with the request.
            after: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following"),
            query_params=[
                param[ItemType1OrStr]("type", type_),
                param[str | None]("after", after),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[CursorPagedArtists],
            error_mapper=get_followed_error_mapper,
            request_options=request_options,
        )

    def get_users_saved_albums(
        self,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        market: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedAlbumObject, GetUsersSavedAlbumsErrorBody]:
        """Get a list of the albums saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums"),
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("market", market),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedAlbumObject],
            error_mapper=get_users_saved_albums_error_mapper,
            request_options=request_options,
        )

    def get_users_saved_audiobooks(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingSavedAudiobookObject, GetUsersSavedAudiobooksErrorBody]:
        """Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedAudiobookObject],
            error_mapper=get_users_saved_audiobooks_error_mapper,
            request_options=request_options,
        )

    def get_users_saved_episodes(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedEpisodeObject, GetUsersSavedEpisodesErrorBody]:
        """Get a list of the episodes saved in the current Spotify user's library.<br/> This API endpoint is in __beta__
        and could change without warning. Please share any feedback that you have, or issues that you discover, in our
        `developer community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/episodes"),
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedEpisodeObject],
            error_mapper=get_users_saved_episodes_error_mapper,
            request_options=request_options,
        )

    def get_users_saved_shows(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingSavedShowObject, GetUsersSavedShowsErrorBody]:
        """Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the
        number of shows returned.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/shows"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedShowObject],
            error_mapper=get_users_saved_shows_error_mapper,
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

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

    def get_users_top_artists(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingArtistObject, GetUsersTopArtistsErrorBody]:
        """Get the current user's top artists based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/top/artists"),
            query_params=[
                param[str | None]("time_range", time_range),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingArtistObject],
            error_mapper=get_users_top_artists_error_mapper,
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

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

    def remove_albums_user(
        self,
        ids: str,
        *,
        body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveAlbumsUserErrorBody]:
        """Remove one or more albums from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/albums"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveAlbumsRequest | RemoveAlbumsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_albums_user_error_mapper,
            request_options=request_options,
        )

    def remove_audiobooks_user(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveAudiobooksUserErrorBody]:
        """Remove one or more audiobooks from the Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_audiobooks_user_error_mapper,
            request_options=request_options,
        )

    def remove_episodes_user(
        self,
        ids: str,
        *,
        body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveEpisodesUserErrorBody]:
        """Remove one or more episodes from the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/episodes"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveEpisodesRequest | RemoveEpisodesRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_episodes_user_error_mapper,
            request_options=request_options,
        )

    def remove_shows_user(
        self,
        ids: str,
        *,
        market: str | None = None,
        body: RemoveShowsRequest | RemoveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveShowsUserErrorBody]:
        """Delete one or more shows from current Spotify user's library.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/shows"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveShowsRequest | RemoveShowsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_shows_user_error_mapper,
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

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

    def save_albums_user(
        self,
        ids: str,
        *,
        body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveAlbumsUserErrorBody]:
        """Save one or more albums to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/albums"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveAlbumsRequest | SaveAlbumsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_albums_user_error_mapper,
            request_options=request_options,
        )

    def save_audiobooks_user(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SaveAudiobooksUserErrorBody]:
        """Save one or more audiobooks to the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_audiobooks_user_error_mapper,
            request_options=request_options,
        )

    def save_episodes_user(
        self,
        ids: str,
        *,
        body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveEpisodesUserErrorBody]:
        """Save one or more episodes to the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/episodes"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveEpisodesRequest | SaveEpisodesRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_episodes_user_error_mapper,
            request_options=request_options,
        )

    def save_shows_user(
        self,
        ids: str,
        *,
        body: SaveShowsRequest | SaveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveShowsUserErrorBody]:
        """Save one or more shows to current Spotify user's library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/shows"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveShowsRequest | SaveShowsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_shows_user_error_mapper,
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

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

    def unfollow_artists_users(
        self,
        type_: ItemType3OrStr,
        ids: str,
        *,
        body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UnfollowArtistsUsersErrorBody]:
        """Remove the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/following"),
            query_params=[param[ItemType3OrStr]("type", type_), param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=unfollow_artists_users_error_mapper,
            request_options=request_options,
        )


class AsyncLibraryWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def change_playlist_details(
        self,
        playlist_id: str,
        *,
        body: PlaylistsRequest | PlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ChangePlaylistDetailsErrorBody]:
        """Change a playlist's name and public/private state. (The user must, of course, own the playlist.)

        Args:
            playlist_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/playlists/{playlist_id}"),
            path_params=[param[str]("playlist_id", playlist_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PlaylistsRequest | PlaylistsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=change_playlist_details_error_mapper,
            request_options=request_options,
        )

    async def check_current_user_follows(
        self, type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckCurrentUserFollowsErrorBody]:
        """Check to see if the current user is following one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following/contains"),
            query_params=[param[ItemType3OrStr]("type", type_), param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_current_user_follows_error_mapper,
            request_options=request_options,
        )

    async def check_users_saved_albums(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedAlbumsErrorBody]:
        """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_albums_error_mapper,
            request_options=request_options,
        )

    async def check_users_saved_audiobooks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedAudiobooksErrorBody]:
        """Check if one or more audiobooks are already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/audiobooks/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_audiobooks_error_mapper,
            request_options=request_options,
        )

    async def check_users_saved_episodes(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedEpisodesErrorBody]:
        """Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
        This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or
        issues that you discover, in our `developer community forum
        <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__..

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/episodes/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_episodes_error_mapper,
            request_options=request_options,
        )

    async def check_users_saved_shows(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedShowsErrorBody]:
        """Check if one or more shows is already saved in the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/shows/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_shows_error_mapper,
            request_options=request_options,
        )

    async def check_users_saved_tracks(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[bool], CheckUsersSavedTracksErrorBody]:
        """Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/tracks/contains"),
            query_params=[param[str]("ids", ids)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[list[bool]],
            error_mapper=check_users_saved_tracks_error_mapper,
            request_options=request_options,
        )

    async def create_playlist(
        self,
        user_id: str,
        *,
        body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlaylistObject, CreatePlaylistErrorBody]:
        """Create a playlist for a Spotify user. (The playlist will be empty until you `add tracks
        <https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist>`__.) Each user is
        generally limited to a maximum of 11000 playlists.

        Args:
            user_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/playlists"),
            path_params=[param[str]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPlaylistsRequest | UsersPlaylistsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PlaylistObject],
            error_mapper=create_playlist_error_mapper,
            request_options=request_options,
        )

    async def follow_artists_users(
        self,
        type_: ItemType2OrStr,
        ids: str,
        *,
        body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, FollowArtistsUsersErrorBody]:
        """Add the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/following"),
            query_params=[param[ItemType2OrStr]("type", type_), param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=follow_artists_users_error_mapper,
            request_options=request_options,
        )

    async def get_a_list_of_current_users_playlists(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingPlaylistObject, GetAListOfCurrentUsersPlaylistsErrorBody]:
        """Get a list of the playlists owned or followed by the current Spotify user.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/playlists"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingPlaylistObject],
            error_mapper=get_a_list_of_current_users_playlists_error_mapper,
            request_options=request_options,
        )

    async def get_followed(
        self,
        type_: ItemType1OrStr,
        *,
        after: str | None = None,
        limit: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CursorPagedArtists, GetFollowedErrorBody]:
        """Get the current user's followed artists.

        Args:
            type_: Value sent with the request.
            after: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following"),
            query_params=[
                param[ItemType1OrStr]("type", type_),
                param[str | None]("after", after),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[CursorPagedArtists],
            error_mapper=get_followed_error_mapper,
            request_options=request_options,
        )

    async def get_users_saved_albums(
        self,
        *,
        limit: int | None = 20,
        offset: int | None = 0,
        market: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedAlbumObject, GetUsersSavedAlbumsErrorBody]:
        """Get a list of the albums saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            market: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums"),
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("market", market),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedAlbumObject],
            error_mapper=get_users_saved_albums_error_mapper,
            request_options=request_options,
        )

    async def get_users_saved_audiobooks(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingSavedAudiobookObject, GetUsersSavedAudiobooksErrorBody]:
        """Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedAudiobookObject],
            error_mapper=get_users_saved_audiobooks_error_mapper,
            request_options=request_options,
        )

    async def get_users_saved_episodes(
        self,
        *,
        market: str | None = None,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingSavedEpisodeObject, GetUsersSavedEpisodesErrorBody]:
        """Get a list of the episodes saved in the current Spotify user's library.<br/> This API endpoint is in __beta__
        and could change without warning. Please share any feedback that you have, or issues that you discover, in our
        `developer community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            market: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/episodes"),
            query_params=[
                param[str | None]("market", market),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedEpisodeObject],
            error_mapper=get_users_saved_episodes_error_mapper,
            request_options=request_options,
        )

    async def get_users_saved_shows(
        self, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PagingSavedShowObject, GetUsersSavedShowsErrorBody]:
        """Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the
        number of shows returned.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/shows"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingSavedShowObject],
            error_mapper=get_users_saved_shows_error_mapper,
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

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
            decoder=json_decoder[PagingSavedTrackObject],
            error_mapper=get_users_saved_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_users_top_artists(
        self,
        *,
        time_range: str | None = "medium_term",
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PagingArtistObject, GetUsersTopArtistsErrorBody]:
        """Get the current user's top artists based on calculated affinity.

        Args:
            time_range: Value sent with the request.
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/top/artists"),
            query_params=[
                param[str | None]("time_range", time_range),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.oauth_2_0,
            decoder=json_decoder[PagingArtistObject],
            error_mapper=get_users_top_artists_error_mapper,
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

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
            decoder=json_decoder[PagingTrackObject],
            error_mapper=get_users_top_tracks_error_mapper,
            request_options=request_options,
        )

    async def remove_albums_user(
        self,
        ids: str,
        *,
        body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveAlbumsUserErrorBody]:
        """Remove one or more albums from the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/albums"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveAlbumsRequest | RemoveAlbumsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_albums_user_error_mapper,
            request_options=request_options,
        )

    async def remove_audiobooks_user(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveAudiobooksUserErrorBody]:
        """Remove one or more audiobooks from the Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_audiobooks_user_error_mapper,
            request_options=request_options,
        )

    async def remove_episodes_user(
        self,
        ids: str,
        *,
        body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveEpisodesUserErrorBody]:
        """Remove one or more episodes from the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/episodes"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveEpisodesRequest | RemoveEpisodesRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_episodes_user_error_mapper,
            request_options=request_options,
        )

    async def remove_shows_user(
        self,
        ids: str,
        *,
        market: str | None = None,
        body: RemoveShowsRequest | RemoveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveShowsUserErrorBody]:
        """Delete one or more shows from current Spotify user's library.

        Args:
            ids: Value sent with the request.
            market: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/shows"),
            query_params=[param[str]("ids", ids), param[str | None]("market", market)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveShowsRequest | RemoveShowsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=remove_shows_user_error_mapper,
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
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

    async def save_albums_user(
        self,
        ids: str,
        *,
        body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveAlbumsUserErrorBody]:
        """Save one or more albums to the current user's 'Your Music' library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/albums"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveAlbumsRequest | SaveAlbumsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_albums_user_error_mapper,
            request_options=request_options,
        )

    async def save_audiobooks_user(
        self, ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SaveAudiobooksUserErrorBody]:
        """Save one or more audiobooks to the current Spotify user's library.

        Args:
            ids: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/audiobooks"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_audiobooks_user_error_mapper,
            request_options=request_options,
        )

    async def save_episodes_user(
        self,
        ids: str,
        *,
        body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveEpisodesUserErrorBody]:
        """Save one or more episodes to the current user's library.<br/> This API endpoint is in __beta__ and could
        change without warning. Please share any feedback that you have, or issues that you discover, in our `developer
        community forum <https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer>`__.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/episodes"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveEpisodesRequest | SaveEpisodesRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_episodes_user_error_mapper,
            request_options=request_options,
        )

    async def save_shows_user(
        self,
        ids: str,
        *,
        body: SaveShowsRequest | SaveShowsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SaveShowsUserErrorBody]:
        """Save one or more shows to current Spotify user's library.

        Args:
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/shows"),
            query_params=[param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SaveShowsRequest | SaveShowsRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=save_shows_user_error_mapper,
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
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

    async def unfollow_artists_users(
        self,
        type_: ItemType3OrStr,
        ids: str,
        *,
        body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UnfollowArtistsUsersErrorBody]:
        """Remove the current user as a follower of one or more artists or other Spotify users.

        Args:
            type_: Value sent with the request.
            ids: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/following"),
            query_params=[param[ItemType3OrStr]("type", type_), param[str]("ids", ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None](body),
            auth_scheme=self._auth.oauth_2_0,
            decoder=empty_response,
            error_mapper=unfollow_artists_users_error_mapper,
            request_options=request_options,
        )
