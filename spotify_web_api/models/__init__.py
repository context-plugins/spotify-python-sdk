from . import enums, unions
from .album_base import AlbumBase, AlbumBaseDict
from .album_object import AlbumObject, AlbumObjectDict
from .album_restriction_object import AlbumRestrictionObject, AlbumRestrictionObjectDict
from .artist_discography_album_object import ArtistDiscographyAlbumObject, ArtistDiscographyAlbumObjectDict
from .artist_object import ArtistObject, ArtistObjectDict
from .audio_analysis_object import AudioAnalysisObject, AudioAnalysisObjectDict
from .audio_features_object import AudioFeaturesObject, AudioFeaturesObjectDict
from .audiobook_base import AudiobookBase, AudiobookBaseDict
from .audiobook_object import AudiobookObject, AudiobookObjectDict
from .author_object import AuthorObject, AuthorObjectDict
from .bad_request1 import BadRequest1, BadRequest1Dict
from .bad_request1_error import BadRequest1Error, BadRequest1ErrorDict
from .categories import Categories, CategoriesDict
from .category_object import CategoryObject, CategoryObjectDict
from .chapter_base import ChapterBase, ChapterBaseDict
from .chapter_object import ChapterObject, ChapterObjectDict
from .chapter_restriction_object import ChapterRestrictionObject, ChapterRestrictionObjectDict
from .context_object import ContextObject, ContextObjectDict
from .copyright_object import CopyrightObject, CopyrightObjectDict
from .currently_playing_context_object import CurrentlyPlayingContextObject, CurrentlyPlayingContextObjectDict
from .currently_playing_object import CurrentlyPlayingObject, CurrentlyPlayingObjectDict
from .cursor_object import CursorObject, CursorObjectDict
from .cursor_paged_artists import CursorPagedArtists, CursorPagedArtistsDict
from .cursor_paging_object import CursorPagingObject, CursorPagingObjectDict
from .cursor_paging_play_history_object import CursorPagingPlayHistoryObject, CursorPagingPlayHistoryObjectDict
from .cursor_paging_simplified_artist_object import (
    CursorPagingSimplifiedArtistObject,
    CursorPagingSimplifiedArtistObjectDict,
)
from .device_object import DeviceObject, DeviceObjectDict
from .disallows_object import DisallowsObject, DisallowsObjectDict
from .episode_base import EpisodeBase, EpisodeBaseDict
from .episode_object import EpisodeObject, EpisodeObjectDict
from .episode_restriction_object import EpisodeRestrictionObject, EpisodeRestrictionObjectDict
from .error_object import ErrorObject, ErrorObjectDict
from .explicit_content_settings_object import ExplicitContentSettingsObject, ExplicitContentSettingsObjectDict
from .external_id_object import ExternalIdObject, ExternalIdObjectDict
from .external_url_object import ExternalUrlObject, ExternalUrlObjectDict
from .follow_artists_or_users_request import FollowArtistsOrUsersRequest, FollowArtistsOrUsersRequestDict
from .followers_object import FollowersObject, FollowersObjectDict
from .forbidden1 import Forbidden1, Forbidden1Dict
from .forbidden1_error import Forbidden1Error, Forbidden1ErrorDict
from .image_object import ImageObject, ImageObjectDict
from .linked_track_object import LinkedTrackObject, LinkedTrackObjectDict
from .many_albums import ManyAlbums, ManyAlbumsDict
from .many_artists import ManyArtists, ManyArtistsDict
from .many_audio_features import ManyAudioFeatures, ManyAudioFeaturesDict
from .many_audiobooks import ManyAudiobooks, ManyAudiobooksDict
from .many_chapters import ManyChapters, ManyChaptersDict
from .many_devices import ManyDevices, ManyDevicesDict
from .many_episodes import ManyEpisodes, ManyEpisodesDict
from .many_genres import ManyGenres, ManyGenresDict
from .many_simplified_shows import ManySimplifiedShows, ManySimplifiedShowsDict
from .many_tracks import ManyTracks, ManyTracksDict
from .markets import Markets, MarketsDict
from .me_player_request import MePlayerRequest, MePlayerRequestDict
from .meta import Meta, MetaDict
from .narrator_object import NarratorObject, NarratorObjectDict
from .not_found1 import NotFound1, NotFound1Dict
from .not_found1_error import NotFound1Error, NotFound1ErrorDict
from .paged_albums import PagedAlbums, PagedAlbumsDict
from .paged_categories import PagedCategories, PagedCategoriesDict
from .paging_artist_discography_album_object import (
    PagingArtistDiscographyAlbumObject,
    PagingArtistDiscographyAlbumObjectDict,
)
from .paging_artist_object import PagingArtistObject, PagingArtistObjectDict
from .paging_featured_playlist_object import PagingFeaturedPlaylistObject, PagingFeaturedPlaylistObjectDict
from .paging_object import PagingObject, PagingObjectDict
from .paging_playlist_object import PagingPlaylistObject, PagingPlaylistObjectDict
from .paging_playlist_track_object import PagingPlaylistTrackObject, PagingPlaylistTrackObjectDict
from .paging_saved_album_object import PagingSavedAlbumObject, PagingSavedAlbumObjectDict
from .paging_saved_audiobook_object import PagingSavedAudiobookObject, PagingSavedAudiobookObjectDict
from .paging_saved_episode_object import PagingSavedEpisodeObject, PagingSavedEpisodeObjectDict
from .paging_saved_show_object import PagingSavedShowObject, PagingSavedShowObjectDict
from .paging_saved_track_object import PagingSavedTrackObject, PagingSavedTrackObjectDict
from .paging_simplified_album_object import PagingSimplifiedAlbumObject, PagingSimplifiedAlbumObjectDict
from .paging_simplified_audiobook_object import PagingSimplifiedAudiobookObject, PagingSimplifiedAudiobookObjectDict
from .paging_simplified_chapter_object import PagingSimplifiedChapterObject, PagingSimplifiedChapterObjectDict
from .paging_simplified_episode_object import PagingSimplifiedEpisodeObject, PagingSimplifiedEpisodeObjectDict
from .paging_simplified_show_object import PagingSimplifiedShowObject, PagingSimplifiedShowObjectDict
from .paging_simplified_track_object import PagingSimplifiedTrackObject, PagingSimplifiedTrackObjectDict
from .paging_track_object import PagingTrackObject, PagingTrackObjectDict
from .play_history_object import PlayHistoryObject, PlayHistoryObjectDict
from .playlist_object import PlaylistObject, PlaylistObjectDict
from .playlist_owner_object import PlaylistOwnerObject, PlaylistOwnerObjectDict
from .playlist_snapshot_id import PlaylistSnapshotId, PlaylistSnapshotIdDict
from .playlist_track_object import PlaylistTrackObject, PlaylistTrackObjectDict
from .playlist_tracks_ref_object import PlaylistTracksRefObject, PlaylistTracksRefObjectDict
from .playlist_user_object import PlaylistUserObject, PlaylistUserObjectDict
from .playlists_followers_request import PlaylistsFollowersRequest, PlaylistsFollowersRequestDict
from .playlists_request import PlaylistsRequest, PlaylistsRequestDict
from .playlists_tracks_request import PlaylistsTracksRequest, PlaylistsTracksRequestDict
from .playlists_tracks_request1 import PlaylistsTracksRequest1, PlaylistsTracksRequest1Dict
from .playlists_tracks_request2 import PlaylistsTracksRequest2, PlaylistsTracksRequest2Dict
from .private_user_object import PrivateUserObject, PrivateUserObjectDict
from .public_user_object import PublicUserObject, PublicUserObjectDict
from .queue_object import QueueObject, QueueObjectDict
from .recommendation_seed_object import RecommendationSeedObject, RecommendationSeedObjectDict
from .recommendations_object import RecommendationsObject, RecommendationsObjectDict
from .remove_albums_request import RemoveAlbumsRequest, RemoveAlbumsRequestDict
from .remove_episodes_request import RemoveEpisodesRequest, RemoveEpisodesRequestDict
from .remove_shows_request import RemoveShowsRequest, RemoveShowsRequestDict
from .remove_tracks_request import RemoveTracksRequest, RemoveTracksRequestDict
from .resume_point_object import ResumePointObject, ResumePointObjectDict
from .save_albums_request import SaveAlbumsRequest, SaveAlbumsRequestDict
from .save_episodes_request import SaveEpisodesRequest, SaveEpisodesRequestDict
from .save_shows_request import SaveShowsRequest, SaveShowsRequestDict
from .save_tracks_request import SaveTracksRequest, SaveTracksRequestDict
from .saved_album_object import SavedAlbumObject, SavedAlbumObjectDict
from .saved_audiobook_object import SavedAudiobookObject, SavedAudiobookObjectDict
from .saved_episode_object import SavedEpisodeObject, SavedEpisodeObjectDict
from .saved_show_object import SavedShowObject, SavedShowObjectDict
from .saved_track_object import SavedTrackObject, SavedTrackObjectDict
from .search_items import SearchItems, SearchItemsDict
from .section_object import SectionObject, SectionObjectDict
from .segment_object import SegmentObject, SegmentObjectDict
from .show_base import ShowBase, ShowBaseDict
from .show_object import ShowObject, ShowObjectDict
from .simplified_album_object import SimplifiedAlbumObject, SimplifiedAlbumObjectDict
from .simplified_artist_object import SimplifiedArtistObject, SimplifiedArtistObjectDict
from .simplified_playlist_object import SimplifiedPlaylistObject, SimplifiedPlaylistObjectDict
from .simplified_track_object import SimplifiedTrackObject, SimplifiedTrackObjectDict
from .start_or_resume_playback_request import StartOrResumePlaybackRequest, StartOrResumePlaybackRequestDict
from .time_interval_object import TimeIntervalObject, TimeIntervalObjectDict
from .too_many_requests1 import TooManyRequests1, TooManyRequests1Dict
from .too_many_requests1_error import TooManyRequests1Error, TooManyRequests1ErrorDict
from .track import Track, TrackDict
from .track1 import Track1, Track1Dict
from .track_object import TrackObject, TrackObjectDict
from .track_restriction_object import TrackRestrictionObject, TrackRestrictionObjectDict
from .unauthorized1 import Unauthorized1, Unauthorized1Dict
from .unauthorized1_error import Unauthorized1Error, Unauthorized1ErrorDict
from .unfollow_artists_or_users_request import UnfollowArtistsOrUsersRequest, UnfollowArtistsOrUsersRequestDict
from .unions import CurrentlyPlaying, CurrentlyPlayingDict, Item, ItemDict, Queue, QueueDict, Track11, Track11Dict
from .users_playlists_request import UsersPlaylistsRequest, UsersPlaylistsRequestDict

__all__ = [
    "enums",
    "unions",
    "AlbumBase",
    "AlbumBaseDict",
    "AlbumObject",
    "AlbumObjectDict",
    "AlbumRestrictionObject",
    "AlbumRestrictionObjectDict",
    "ArtistDiscographyAlbumObject",
    "ArtistDiscographyAlbumObjectDict",
    "ArtistObject",
    "ArtistObjectDict",
    "AudioAnalysisObject",
    "AudioAnalysisObjectDict",
    "AudioFeaturesObject",
    "AudioFeaturesObjectDict",
    "AudiobookBase",
    "AudiobookBaseDict",
    "AudiobookObject",
    "AudiobookObjectDict",
    "AuthorObject",
    "AuthorObjectDict",
    "BadRequest1",
    "BadRequest1Dict",
    "BadRequest1Error",
    "BadRequest1ErrorDict",
    "Categories",
    "CategoriesDict",
    "CategoryObject",
    "CategoryObjectDict",
    "ChapterBase",
    "ChapterBaseDict",
    "ChapterObject",
    "ChapterObjectDict",
    "ChapterRestrictionObject",
    "ChapterRestrictionObjectDict",
    "ContextObject",
    "ContextObjectDict",
    "CopyrightObject",
    "CopyrightObjectDict",
    "CurrentlyPlaying",
    "CurrentlyPlayingContextObject",
    "CurrentlyPlayingContextObjectDict",
    "CurrentlyPlayingDict",
    "CurrentlyPlayingObject",
    "CurrentlyPlayingObjectDict",
    "CursorObject",
    "CursorObjectDict",
    "CursorPagedArtists",
    "CursorPagedArtistsDict",
    "CursorPagingObject",
    "CursorPagingObjectDict",
    "CursorPagingPlayHistoryObject",
    "CursorPagingPlayHistoryObjectDict",
    "CursorPagingSimplifiedArtistObject",
    "CursorPagingSimplifiedArtistObjectDict",
    "DeviceObject",
    "DeviceObjectDict",
    "DisallowsObject",
    "DisallowsObjectDict",
    "EpisodeBase",
    "EpisodeBaseDict",
    "EpisodeObject",
    "EpisodeObjectDict",
    "EpisodeRestrictionObject",
    "EpisodeRestrictionObjectDict",
    "ErrorObject",
    "ErrorObjectDict",
    "ExplicitContentSettingsObject",
    "ExplicitContentSettingsObjectDict",
    "ExternalIdObject",
    "ExternalIdObjectDict",
    "ExternalUrlObject",
    "ExternalUrlObjectDict",
    "FollowArtistsOrUsersRequest",
    "FollowArtistsOrUsersRequestDict",
    "FollowersObject",
    "FollowersObjectDict",
    "Forbidden1",
    "Forbidden1Dict",
    "Forbidden1Error",
    "Forbidden1ErrorDict",
    "ImageObject",
    "ImageObjectDict",
    "Item",
    "ItemDict",
    "LinkedTrackObject",
    "LinkedTrackObjectDict",
    "ManyAlbums",
    "ManyAlbumsDict",
    "ManyArtists",
    "ManyArtistsDict",
    "ManyAudioFeatures",
    "ManyAudioFeaturesDict",
    "ManyAudiobooks",
    "ManyAudiobooksDict",
    "ManyChapters",
    "ManyChaptersDict",
    "ManyDevices",
    "ManyDevicesDict",
    "ManyEpisodes",
    "ManyEpisodesDict",
    "ManyGenres",
    "ManyGenresDict",
    "ManySimplifiedShows",
    "ManySimplifiedShowsDict",
    "ManyTracks",
    "ManyTracksDict",
    "Markets",
    "MarketsDict",
    "MePlayerRequest",
    "MePlayerRequestDict",
    "Meta",
    "MetaDict",
    "NarratorObject",
    "NarratorObjectDict",
    "NotFound1",
    "NotFound1Dict",
    "NotFound1Error",
    "NotFound1ErrorDict",
    "PagedAlbums",
    "PagedAlbumsDict",
    "PagedCategories",
    "PagedCategoriesDict",
    "PagingArtistDiscographyAlbumObject",
    "PagingArtistDiscographyAlbumObjectDict",
    "PagingArtistObject",
    "PagingArtistObjectDict",
    "PagingFeaturedPlaylistObject",
    "PagingFeaturedPlaylistObjectDict",
    "PagingObject",
    "PagingObjectDict",
    "PagingPlaylistObject",
    "PagingPlaylistObjectDict",
    "PagingPlaylistTrackObject",
    "PagingPlaylistTrackObjectDict",
    "PagingSavedAlbumObject",
    "PagingSavedAlbumObjectDict",
    "PagingSavedAudiobookObject",
    "PagingSavedAudiobookObjectDict",
    "PagingSavedEpisodeObject",
    "PagingSavedEpisodeObjectDict",
    "PagingSavedShowObject",
    "PagingSavedShowObjectDict",
    "PagingSavedTrackObject",
    "PagingSavedTrackObjectDict",
    "PagingSimplifiedAlbumObject",
    "PagingSimplifiedAlbumObjectDict",
    "PagingSimplifiedAudiobookObject",
    "PagingSimplifiedAudiobookObjectDict",
    "PagingSimplifiedChapterObject",
    "PagingSimplifiedChapterObjectDict",
    "PagingSimplifiedEpisodeObject",
    "PagingSimplifiedEpisodeObjectDict",
    "PagingSimplifiedShowObject",
    "PagingSimplifiedShowObjectDict",
    "PagingSimplifiedTrackObject",
    "PagingSimplifiedTrackObjectDict",
    "PagingTrackObject",
    "PagingTrackObjectDict",
    "PlayHistoryObject",
    "PlayHistoryObjectDict",
    "PlaylistObject",
    "PlaylistObjectDict",
    "PlaylistOwnerObject",
    "PlaylistOwnerObjectDict",
    "PlaylistSnapshotId",
    "PlaylistSnapshotIdDict",
    "PlaylistTrackObject",
    "PlaylistTrackObjectDict",
    "PlaylistTracksRefObject",
    "PlaylistTracksRefObjectDict",
    "PlaylistUserObject",
    "PlaylistUserObjectDict",
    "PlaylistsFollowersRequest",
    "PlaylistsFollowersRequestDict",
    "PlaylistsRequest",
    "PlaylistsRequestDict",
    "PlaylistsTracksRequest",
    "PlaylistsTracksRequest1",
    "PlaylistsTracksRequest1Dict",
    "PlaylistsTracksRequest2",
    "PlaylistsTracksRequest2Dict",
    "PlaylistsTracksRequestDict",
    "PrivateUserObject",
    "PrivateUserObjectDict",
    "PublicUserObject",
    "PublicUserObjectDict",
    "Queue",
    "QueueDict",
    "QueueObject",
    "QueueObjectDict",
    "RecommendationSeedObject",
    "RecommendationSeedObjectDict",
    "RecommendationsObject",
    "RecommendationsObjectDict",
    "RemoveAlbumsRequest",
    "RemoveAlbumsRequestDict",
    "RemoveEpisodesRequest",
    "RemoveEpisodesRequestDict",
    "RemoveShowsRequest",
    "RemoveShowsRequestDict",
    "RemoveTracksRequest",
    "RemoveTracksRequestDict",
    "ResumePointObject",
    "ResumePointObjectDict",
    "SaveAlbumsRequest",
    "SaveAlbumsRequestDict",
    "SaveEpisodesRequest",
    "SaveEpisodesRequestDict",
    "SaveShowsRequest",
    "SaveShowsRequestDict",
    "SaveTracksRequest",
    "SaveTracksRequestDict",
    "SavedAlbumObject",
    "SavedAlbumObjectDict",
    "SavedAudiobookObject",
    "SavedAudiobookObjectDict",
    "SavedEpisodeObject",
    "SavedEpisodeObjectDict",
    "SavedShowObject",
    "SavedShowObjectDict",
    "SavedTrackObject",
    "SavedTrackObjectDict",
    "SearchItems",
    "SearchItemsDict",
    "SectionObject",
    "SectionObjectDict",
    "SegmentObject",
    "SegmentObjectDict",
    "ShowBase",
    "ShowBaseDict",
    "ShowObject",
    "ShowObjectDict",
    "SimplifiedAlbumObject",
    "SimplifiedAlbumObjectDict",
    "SimplifiedArtistObject",
    "SimplifiedArtistObjectDict",
    "SimplifiedPlaylistObject",
    "SimplifiedPlaylistObjectDict",
    "SimplifiedTrackObject",
    "SimplifiedTrackObjectDict",
    "StartOrResumePlaybackRequest",
    "StartOrResumePlaybackRequestDict",
    "TimeIntervalObject",
    "TimeIntervalObjectDict",
    "TooManyRequests1",
    "TooManyRequests1Dict",
    "TooManyRequests1Error",
    "TooManyRequests1ErrorDict",
    "Track",
    "Track1",
    "Track11",
    "Track11Dict",
    "Track1Dict",
    "TrackDict",
    "TrackObject",
    "TrackObjectDict",
    "TrackRestrictionObject",
    "TrackRestrictionObjectDict",
    "Unauthorized1",
    "Unauthorized1Dict",
    "Unauthorized1Error",
    "Unauthorized1ErrorDict",
    "UnfollowArtistsOrUsersRequest",
    "UnfollowArtistsOrUsersRequestDict",
    "UsersPlaylistsRequest",
    "UsersPlaylistsRequestDict",
]
