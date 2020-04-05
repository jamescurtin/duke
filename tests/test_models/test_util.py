from pathlib import Path

from duke.models import _util
from duke.types import Point

SOME_POINT = Point(4, 7)
SOME_SCALE_FACTOR = 25


def test_get_board_coordinates():
    assert _util.get_board_coordinates(SOME_POINT, SOME_SCALE_FACTOR) == Point(100, 175)


def test_get_png(mocker):
    mock_open = mocker.patch("duke.models._util.Image.open")
    _util.get_png("foo", "bar")
    expected_path = Path("/app/duke/assets/tiles/foo/bar.png")
    mock_open.assert_called_with(expected_path)
