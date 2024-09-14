import argparse
from datetime import datetime, timedelta
from enum import StrEnum

from .urlbuilder import FormatType


class OutputFormat(StrEnum):
    TEXT = "text"
    JSON = "json"


def valid_date(s: str) -> datetime:
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a valid date: {s!r}")


def cli() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-st",
        "--starttime",
        type=valid_date,
        default=(datetime.now() - timedelta(days=5)).isoformat(),
        help="Starttime for the events in ISO format",
    )
    ap.add_argument(
        "-et",
        "--endtime",
        type=valid_date,
        default=datetime.now(),
        help="Endtime for the events in ISO format",
    )
    ap.add_argument("-l", "--limit", type=int, default=10, help="Limit of results")
    ap.add_argument(
        "-f",
        "--output-format",
        type=OutputFormat,
        choices=list(OutputFormat),
        default=OutputFormat.JSON,
        help="Format type of the app output",
    )
    return ap.parse_args()
