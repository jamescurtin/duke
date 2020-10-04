from duke.models import _util
from duke.types import Point

SOME_POINT = Point(4, 7)
SOME_SCALE_FACTOR = 25


def test_get_board_coordinates():
    assert _util.get_board_coordinates(SOME_POINT, SOME_SCALE_FACTOR) == Point(100, 175)


def test_get_png(mocker):
    mock_open = mocker.patch("duke.models._util.Image.open")
    _util.get_png("foo", "bar")
    expected_path = "/duke/assets/tiles/foo/bar.png"
    open_path = mock_open.call_args[0][0]
    assert expected_path in str(open_path)
