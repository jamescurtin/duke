from duke.models import _generate
from duke.types import RGBA, Dimensions, Point

SOME_DIMENSIONS = Dimensions(100, 200)
SOME_COLOR = RGBA(0, 0, 0, 0)
SOME_PATH = "/foo/bar"
SOME_FONT_SIZE = 10
SOME_TEXT = "Hello world"
SOME_POINT = Point(0, 0)


def test_generate_block_container__call_args(mocker):
    mock_image = mocker.patch("duke.models._generate.Image.new")
    _generate.generate_block_container(SOME_DIMENSIONS, SOME_COLOR)

    mock_image.assert_called_with("RGBA", [*SOME_DIMENSIONS], SOME_COLOR)


def test_generate_font__call_args(mocker):
    mock_font = mocker.patch("duke.models._generate.ImageFont.truetype")
    _generate._generate_font(SOME_PATH, SOME_FONT_SIZE)

    mock_font.assert_called_with(SOME_PATH, SOME_FONT_SIZE)


def test_get_message_dimensions__returns_dimensions(mocker):
    mock_image = mocker.MagicMock()
    mock_image.textsize.return_value = tuple(SOME_DIMENSIONS)
    mock_imagedraw = mocker.patch(
        "duke.models._generate.ImageDraw.Draw", return_value=mock_image
    )
    result = _generate._get_message_dimensions(SOME_TEXT, mocker.MagicMock())
    assert result == SOME_DIMENSIONS


def test_get_sized_message(mocker):
    return_dimensions = [(200, 200), (300, 300), (400, 400)]
    mocker.patch("duke.models._generate.ImageFont")
    mocker.patch("duke.models._generate._generate_font")
    mock_dimensions = mocker.patch(
        "duke.models._generate._get_message_dimensions", side_effect=return_dimensions
    )
    _, dims = _generate._get_sized_message(SOME_TEXT, SOME_PATH, Dimensions(450, 450))

    assert mock_dimensions.call_count == 3
    assert dims == Dimensions(400, 400)


def test_center_text_coordinates():
    text_dims = Dimensions(100, 200)
    container_dims = Dimensions(1000, 2000)
    point = _generate._center_text_coordinates(text_dims, container_dims, 20)
    assert point == Point(450, 896)


def test_generate_font_block__call_args(mocker):
    draw_mock = mocker.MagicMock()
    font_mock = mocker.MagicMock()
    mocker.patch("duke.models._generate.generate_block_container")
    mocker.patch("duke.models._generate.ImageDraw.Draw", return_value=draw_mock)
    mocker.patch(
        "duke.models._generate._get_sized_message",
        return_value=(font_mock, SOME_DIMENSIONS),
    )
    mocker.patch(
        "duke.models._generate._center_text_coordinates", return_value=SOME_POINT
    )
    _generate.generate_font_block(SOME_TEXT)

    draw_mock.text.assert_called_with(
        SOME_POINT, SOME_TEXT, fill="black", font=font_mock
    )
