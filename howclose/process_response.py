from math import asin, cos, radians, sin, sqrt
from operator import attrgetter
from typing import Self

from .cli import OutputFormat


class Coordinate:
    def __init__(self, lon: float, lat: float) -> None:
        self.lon = lon
        self.lat = lat

    def haversine(self, other: Self) -> float:
        """
        Calculate the great circle distance in kilometers between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(
            radians, [self.lon, self.lat, other.lon, other.lat]
        )

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
        return c * r


class Data:
    def __init__(self, feature: dict, current: Coordinate) -> None:
        self.lon, self.lat = feature["coordinate"][0], feature["coordinate"][1]
        self.distance = current.haversine(Coordinate(self.lon, self.lat))

    def json(self):
        # todo: json representation
        return "json"

    def text(self):
        # todo: text representation
        return "text"


def process_georequest(response_json: dict, current: Coordinate, format: OutputFormat):
    if response_json["metadata"]["count"] < 1:
        return "No events found in the given time frame!"
    dataset = []
    for feature in response_json["features"]:
        d = Data(feature, current)
        dataset.append(d)
    data = min(dataset, key=attrgetter("distance"))
    if format == OutputFormat.JSON:
        return data.json()
    elif format == OutputFormat.TEXT:
        return data.text()
    assert "OutputFormat is not matched exaustive"
