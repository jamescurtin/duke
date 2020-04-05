from PIL import Image

from duke.constants import TILES_DIR
from duke.types import Point


def get_board_coordinates(square_location: Point, scale_factor: int) -> Point:
    """Returns coordinates for a given square on a board.

    Based on the top left square being indexed at (0,0). Requires the width of
    each square to determine the corresponding pixel coordinates.

    Args:
        square_location(Point): Coordinates of square
        scale_factor (int): width, in pixels, of each square

    Returns:
        Point: Pixel coordinates to place an object in the given square
    """
    return Point(square_location.x * scale_factor, square_location.y * scale_factor)


def get_png(image_subdir: str, icon_name: str) -> Image:
    """Gets a PNG image asset.

    Args:
        image_subdir (str): Subdirectory containing the image
        icon_name (str): Name of the image

    Returns:
        Image: The image
    """
    return Image.open(TILES_DIR / image_subdir / f"{icon_name}.png")
