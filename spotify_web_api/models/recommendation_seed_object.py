from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RecommendationSeedObject(SdkBaseModel):
    after_filtering_size: Optional[int] = Field(default=UNSET, alias="afterFilteringSize")
    r"""The number of tracks available after min\_\* and max\_\* filters have been applied."""

    after_relinking_size: Optional[int] = Field(default=UNSET, alias="afterRelinkingSize")
    """The number of tracks available after relinking for regional availability."""

    href: Optional[str] = UNSET
    """A link to the full track or artist data for this seed. For tracks this will be a link to a Track Object. For
    artists a link to an Artist Object. For genre seeds, this value will be ``null``."""

    id: Optional[str] = UNSET
    """The id used to select this seed. This will be the same as the string used in the ``seed_artists``,
    ``seed_tracks`` or ``seed_genres`` parameter."""

    initial_pool_size: Optional[int] = Field(default=UNSET, alias="initialPoolSize")
    """The number of recommended tracks available for this seed."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The entity type of this seed. One of ``artist``, ``track`` or ``genre``."""


class RecommendationSeedObjectDict(TypedDict):
    after_filtering_size: NotRequired[int]
    after_relinking_size: NotRequired[int]
    href: NotRequired[str]
    id: NotRequired[str]
    initial_pool_size: NotRequired[int]
    type_: NotRequired[str]
