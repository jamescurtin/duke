from typing import Tuple

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont

from duke.constants import TILE_FONT
from duke.types import RGBA, Dimensions, Point

TRANSPARENT_COLOR: RGBA = RGBA(255, 0, 0, 0)

# Keeps text from touching sides of the container
TITLE_BUFFER = 100
# Keeps short messages from getting excessively large
MAX_FONT_SIZE = 150
TITLE_DIMS: Dimensions = Dimensions(1000, 400)


def generate_block_container(dimensions: Dimensions, background_color: RGBA) -> Image:
    """Generates a empty image block that can be used as a canvas.

    Args:
        dimensions (Dimensions): Dimensions of the image block
        background_color (RGBA): RGBA of the background color

    Returns:
        Image: Image block
    """
    return Image.new("RGBA", [*dimensions], background_color)


def _generate_font(font_path: str, font_size: int) -> FreeTypeFont:
    """Create a FreeType font of a given size.

    Args:
        font_path (str): Path to font file
        font_size (int): Point size of the font

    Returns:
        FreeTypeFont:
    """
    return ImageFont.truetype(font_path, font_size)


def _get_message_dimensions(text: str, font: FreeTypeFont) -> Dimensions:
    """Determines the dimensions of a text block, given a sized font.

    Args:
        text (str): Text of the message
        font (FreeTypeFont): Font of the message

    Returns:
        Dimensions: Dimensions of the message, in poxels
    """
    img = generate_block_container(TITLE_DIMS, TRANSPARENT_COLOR)
    img_draw = ImageDraw.Draw(img)
    width, height = img_draw.textsize(text, font=font, spacing=0)
    return Dimensions(width, height)


def _get_sized_message(
    text: str, font_path: str, max_dims: Dimensions
) -> Tuple[FreeTypeFont, Dimensions]:
    """Determines the maximum font size for a message to fit into a given box.

    Args:
        text (str): Text of the message
        font_path (str): Path the the font file
        max_dims (Dimensions): Dimensions the text must fit within

    Returns:
        Tuple[FreeTypeFont, Dimensions]: Maximally sized font and message dimensions
    """
    # Start at the minimum font size and work upward
    font_size = 1
    font = _generate_font(font_path, font_size)

    title_width, title_height = max_dims
    width, height = _get_message_dimensions(text, font)

    # Keep increasing the font size as long as the text still fits in the box
    while width <= title_width - TITLE_BUFFER and height <= title_height - TITLE_BUFFER:
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)
        width, height = _get_message_dimensions(text, font)

    return font, Dimensions(width, height)


def _center_text_coordinates(
    text_dims: Dimensions, container_dims: Dimensions, font_size: int
) -> Point:
    """Generates origin coordinates for centering text in a container.

    Args:
        text_dims (Dimensions): Dimensions of the text block
        container_dims (Dimensions): Dimensions of the container
        font_size (int): Font size of the message

    Returns:
        Point: Coordinate to place text
    """
    # For fonts that have extra vertical whitespace; this is a visually subjective
    # offset factor based on the font used.
    vertical_font_offset = font_size * 0.2
    x = (container_dims.width - text_dims.width) / 2
    y = ((container_dims.height - text_dims.height) / 2) - vertical_font_offset
    return Point(x, y)


def generate_font_block(text: str) -> ImageDraw:
    """Generates an image containing centered text that fills the available space.

    Args:
        text (str): Message

    Returns:
        ImageDraw: Image containing the text
    """
    img = generate_block_container(TITLE_DIMS, TRANSPARENT_COLOR)
    draw = ImageDraw.Draw(img)
    font, message_dims = _get_sized_message(text, TILE_FONT, TITLE_DIMS)
    draw.text(
        _center_text_coordinates(message_dims, TITLE_DIMS, font.size),
        text,
        fill="black",
        font=font,
    )
    return img
