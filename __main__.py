from datetime import datetime, timedelta

from howclose import EarthquakeAPIURLBuilder, FormatType, OrderType


def main():
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
    print(url)


if __name__ == "__main__":
    main()
