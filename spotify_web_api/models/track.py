from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Track(SdkBaseModel):
    num_samples: Optional[int] = UNSET
    """The exact number of audio samples analyzed from this track. See also ``analysis_sample_rate``."""

    duration: Optional[float] = UNSET
    """Length of the track in seconds."""

    sample_md5: Optional[str] = UNSET
    """This field will always contain the empty string."""

    offset_seconds: Optional[int] = UNSET
    """An offset to the start of the region of the track that was analyzed. (As the entire track is analyzed, this
    should always be 0.)"""

    window_seconds: Optional[int] = UNSET
    """The length of the region of the track was analyzed, if a subset of the track was analyzed. (As the entire track
    is analyzed, this should always be 0.)"""

    analysis_sample_rate: Optional[int] = UNSET
    """The sample rate used to decode and analyze this track. May differ from the actual sample rate of this track
    available on Spotify."""

    analysis_channels: Optional[int] = UNSET
    """The number of channels used for analysis. If 1, all channels are summed together to mono before analysis."""

    end_of_fade_in: Optional[float] = UNSET
    """The time, in seconds, at which the track's fade-in period ends. If the track has no fade-in, this will be 0.0."""

    start_of_fade_out: Optional[float] = UNSET
    """The time, in seconds, at which the track's fade-out period starts. If the track has no fade-out, this should
    match the track's length."""

    loudness: Optional[float] = UNSET
    """The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are
    useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary
    psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db."""

    tempo: Optional[float] = UNSET
    """The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or
    pace of a given piece and derives directly from the average beat duration."""

    tempo_confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the ``tempo``."""

    time_signature: Optional[int] = UNSET
    """An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are
    in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4"."""

    time_signature_confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the ``time_signature``."""

    key: Optional[int] = UNSET
    """The key the track is in. Integers map to pitches using standard `Pitch Class notation
    <https://en.wikipedia.org/wiki/Pitch_class>`__. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the
    value is -1."""

    key_confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the ``key``."""

    mode: Optional[int] = UNSET
    """Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is
    derived. Major is represented by 1 and minor is 0."""

    mode_confidence: Optional[float] = UNSET
    """The confidence, from 0.0 to 1.0, of the reliability of the ``mode``."""

    codestring: Optional[str] = UNSET
    """An `Echo Nest Musical Fingerprint (ENMFP) <https://academiccommons.columbia.edu/doi/10.7916/D8Q248M4>`__
    codestring for this track."""

    code_version: Optional[float] = UNSET
    """A version number for the Echo Nest Musical Fingerprint format used in the codestring field."""

    echoprintstring: Optional[str] = UNSET
    """An `EchoPrint <https://github.com/spotify/echoprint-codegen>`__ codestring for this track."""

    echoprint_version: Optional[float] = UNSET
    """A version number for the EchoPrint format used in the echoprintstring field."""

    synchstring: Optional[str] = UNSET
    """A `Synchstring <https://github.com/echonest/synchdata>`__ for this track."""

    synch_version: Optional[float] = UNSET
    """A version number for the Synchstring used in the synchstring field."""

    rhythmstring: Optional[str] = UNSET
    """A Rhythmstring for this track. The format of this string is similar to the Synchstring."""

    rhythm_version: Optional[float] = UNSET
    """A version number for the Rhythmstring used in the rhythmstring field."""


class TrackDict(TypedDict):
    num_samples: NotRequired[int]
    duration: NotRequired[float]
    sample_md5: NotRequired[str]
    offset_seconds: NotRequired[int]
    window_seconds: NotRequired[int]
    analysis_sample_rate: NotRequired[int]
    analysis_channels: NotRequired[int]
    end_of_fade_in: NotRequired[float]
    start_of_fade_out: NotRequired[float]
    loudness: NotRequired[float]
    tempo: NotRequired[float]
    tempo_confidence: NotRequired[float]
    time_signature: NotRequired[int]
    time_signature_confidence: NotRequired[float]
    key: NotRequired[int]
    key_confidence: NotRequired[float]
    mode: NotRequired[int]
    mode_confidence: NotRequired[float]
    codestring: NotRequired[str]
    code_version: NotRequired[float]
    echoprintstring: NotRequired[str]
    echoprint_version: NotRequired[float]
    synchstring: NotRequired[str]
    synch_version: NotRequired[float]
    rhythmstring: NotRequired[str]
    rhythm_version: NotRequired[float]
