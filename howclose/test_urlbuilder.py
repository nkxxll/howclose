from datetime import datetime, timedelta
from json import dumps

from requests import Response, get

from .urlbuilder import EarthquakeAPIURLBuilder, FormatType, OrderType

SNAPDIR = "snapshots"
TEST_DATE = "2023-09-13T22:21:22"
TEST_START = datetime.fromisoformat(TEST_DATE) - timedelta(days=10)
TEST_END = datetime.fromisoformat(TEST_DATE)


def test_limit(snapshot):
    snapshot.snapshot_dir = SNAPDIR
    url = (
        EarthquakeAPIURLBuilder()
        .time(starttime=TEST_START, endtime=TEST_END)
        .limit(limit=10)
        .finalize()
    )
    snapshot.assert_match(url, "test_url_builder_limit.txt")


def test_time(snapshot):
    snapshot.snapshot_dir = SNAPDIR
    url = (
        EarthquakeAPIURLBuilder()
        .time(starttime=TEST_START, endtime=TEST_END)
        .finalize()
    )
    snapshot.assert_match(url, "test_url_builder_time.txt")


def test_time_request(snapshot):
    snapshot.snapshot_dir = SNAPDIR
    url = (
        EarthquakeAPIURLBuilder()
        .limit(limit=10)
        .time(starttime=TEST_START, endtime=TEST_END)
        .finalize()
    )
    response: Response = get(url=url)
    snapshot.assert_match(response.content, "test_url_builder_time_request.txt")


def test_fromat(snapshot):
    snapshot.snapshot_dir = SNAPDIR
    format = FormatType.GEOJSON
    url = EarthquakeAPIURLBuilder().format(format).finalize()
    snapshot.assert_match(url, "test_url_builder_format.txt")


def test_format_request(snapshot):
    snapshot.snapshot_dir = SNAPDIR
    format = FormatType.GEOJSON
    url = (
        EarthquakeAPIURLBuilder()
        .time(starttime=TEST_START, endtime=TEST_END)
        .limit(limit=10)
        .format(format)
        .finalize()
    )
    response: Response = get(url=url)
    snapshot.assert_match(dumps(response.json()), "test_url_builder_format_request.txt")


def test_orderby(snapshot):
    snapshot.snapshot_dir = SNAPDIR
    orderby = OrderType.MAGNITUDEASC
    url = EarthquakeAPIURLBuilder().orderby(orderby).finalize()
    snapshot.assert_match(url, "test_url_builder_format.txt")


def test_orderby_request(snapshot):
    snapshot.snapshot_dir = SNAPDIR
    orderby = OrderType.MAGNITUDEASC
    url = (
        EarthquakeAPIURLBuilder()
        .time(starttime=TEST_START, endtime=TEST_END)
        .limit(limit=10)
        .orderby(orderby)
        .finalize()
    )
    response: Response = get(url=url)
    snapshot.assert_match(response.content, "test_url_builder_orderby_request.txt")
