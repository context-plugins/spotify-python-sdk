from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExternalIdObject(SdkBaseModel):
    isrc: Optional[str] = UNSET
    """`International Standard Recording Code <http://en.wikipedia.org/wiki/International_Standard_Recording_Code>`__"""

    ean: Optional[str] = UNSET
    """`International Article Number <http://en.wikipedia.org/wiki/International_Article_Number_%28EAN%29>`__"""

    upc: Optional[str] = UNSET
    """`Universal Product Code <http://en.wikipedia.org/wiki/Universal_Product_Code>`__"""


class ExternalIdObjectDict(TypedDict):
    isrc: NotRequired[str]
    ean: NotRequired[str]
    upc: NotRequired[str]
