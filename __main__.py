import geocoder
import requests

from howclose import (
    EarthquakeAPIURLBuilder,
    FormatType,
    OrderType,
    cli_args,
    process_georequest,
)
from howclose.process_response import Coordinate


def main():
    args = cli_args()
    url = (
        EarthquakeAPIURLBuilder()
        .format(FormatType.GEOJSON)
        .time(starttime=args.starttime, endtime=args.endtime)
        .limit(limit=args.limit)
        .minmagnitude(minmagnitude=args.minmagnitude)
        .orderby(OrderType.MAGNITUDE)
        .finalize()
    )
    response: requests.Response = requests.get(url=url)
    # print(json.dumps(response.json(), indent=2))
    (lat, lon) = geocoder.ip("me").latlng
    current = Coordinate(lon=lon, lat=lat)
    data = process_georequest(response.json(), current, args.output_format)
    print(data)


if __name__ == "__main__":
    main()
