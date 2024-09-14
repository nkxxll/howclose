import json

import requests

from howclose import EarthquakeAPIURLBuilder, FormatType, OrderType, cli


def main():
    args = cli()
    url = (
        EarthquakeAPIURLBuilder()
        .format(FormatType.GEOJSON)
        .time(starttime=args.starttime, endtime=args.endtime)
        .limit(limit=args.limit)
        .minmagnitude(minmagnitude=6)
        .orderby(OrderType.MAGNITUDE)
        .finalize()
    )
    response: requests.Response = requests.get(url=url)
    print(json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    main()
