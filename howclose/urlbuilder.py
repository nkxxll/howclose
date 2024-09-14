"""build earthquake API URL

This module provides all the necessary tools to build a URL for the
`earthquake.usgs.gov` API. URLs can be build with the `EarthquakeAPIURLBuilder` and
its methods. For the format type a enum was created and for the order type
another enum is provided. The URL string can be obtained by calling `str()` on
the `EarthquakeAPIURLBuilder` or use the `.finalize()` method.

Example:
```python
from howclose import EarthquakeAPIURLBuilder, FormatType, OrderType
default_delta = timedelta(days=30)
now = datetime.now()
url = (
    EarthquakeAPIURLBuilder()
    .format(FormatType.GEOJSON)
    .time(starttime=now - default_delta, endtime=now)
    .limit(number=10)
    .maxdepth(depth=10)
    .magnitude(magnitude=6)
    .orderby(OrderType.MAGNITUDE)
    .finalize()
)
"""

from datetime import datetime
from enum import StrEnum
from logging import getLogger
from typing import Self
from urllib.parse import urlparse

logger = getLogger(__name__)

DEFAULT_STATE: str = "https://earthquake.usgs.gov/fdsnws/event/1/query?"


def uri_validator(x):
    """Validate whether URI is valid

    Args:
        x (str): URI to validate

    Returns:
        bool: is (true) or is not valid (false)
    """
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False


class OrderType(StrEnum):
    """Types to order the results of the API call

    Attributes:
        MAGNITUDE: Order by magnitude
        MAGNITUDEASC: Order by magnitude ascending
        TIME: Order by time
        TIMEASC: Order by time ascending
    """

    MAGNITUDE = "magnitude"
    MAGNITUDEASC = "magnitude-asc"
    TIME = "time"
    TIMEASC = "time-asc"


class FormatType(StrEnum):
    """Types of API response format

    Attributes:
        CSV: As csv
        GEOJSON: As geojson
        KML: As kml
        QUAKEML: As quakeml
        TEXT: As text
        XML: Ax xml
    """

    CSV = "csv"
    GEOJSON = "geojson"
    KML = "kml"
    QUAKEML = "quakeml"
    TEXT = "text"
    XML = "xml"


class EarthquakeAPIURLBuilder:
    """Helper class to build a earthquake URL for the API

    Attributes:
        state: Current URL (default: base URL for a query request
    """

    def __init__(self, state: str = DEFAULT_STATE) -> None:
        self.state: str = state

    def __str__(self) -> str:
        if not uri_validator(self.state):
            logger.warning(f"URI could not be parsed: {self.state}")
        return self.state

    def format(self, type: FormatType) -> Self:
        self.state += f"format={type}&"
        return self

    def orderby(self, ordertype: OrderType) -> Self:
        self.state += f"orderby={ordertype}&"
        return self

    def time(self, starttime: datetime, endtime: datetime) -> Self:
        self.state += (
            f"starttime={starttime.isoformat()}&endtime={endtime.isoformat()}&"
        )
        return self

    def limit(self, limit: int) -> Self:
        if limit < 1 or limit > 20000:
            logger.warning(
                f"Limit should be within 1 and 20000! You entered {limit}.\
                    Limit was set to the nearest boundary!"
            )
            if limit < 1:
                limit = 1
            else:
                limit = 20000
        self.state += f"limit={limit}&"
        return self

    def maxdepth(self, maxdepth: int) -> Self:
        if maxdepth < -100 or maxdepth > 1000:
            logger.warning(
                f"Maxdepth should be within -100 and 1000! You entered\
                {maxdepth}. Maxdepth was set to the nearest boundary!"
            )
            if maxdepth < 1:
                maxdepth = -100
            else:
                maxdepth = 1000
        self.state += f"maxdepth={maxdepth}&"
        return self

    def maxmagnitude(self, maxmagnitude: int) -> Self:
        self.state += f"maxmagnitude={maxmagnitude}&"
        return self

    def minmagnitude(self, minmagnitude: int) -> Self:
        self.state += f"minmagnitude={minmagnitude}&"
        return self

    def finalize(self) -> str:
        if not uri_validator(self.state):
            logger.warning(f"URI could not be parsed: {self.state}")
        return self.state
