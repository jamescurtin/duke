import abc
from dataclasses import dataclass, field
from enum import Enum, auto

from PIL import Image

from duke.models._generate import generate_block_container, generate_font_block
from duke.models._util import get_board_coordinates, get_png
from duke.types import RGBA, BoardPositions, Dimensions, Point

PLAYER_ONE_COLOR = RGBA(255, 255, 255, 100)
PLAYER_TWO_COLOR = RGBA(210, 186, 140, 100)

TILE_SQUARE_PIXELS = 200
TILE_DIMS = Dimensions(1400, 1400)

ORIGIN = Point(0, 0)
TITLE_LOCATION = Point(0, 5)
IMAGE_LOCATION = Point(5, 0)


class AutoName(Enum):
    """Auto generate names for Enums."""

    def _generate_next_value_(name, start, count, last_values):  # noqa: N805
        return name.lower().replace("_", "-")


class Player(Enum):
    """Players."""

    PLAYER_ONE = PLAYER_ONE_COLOR
    PLAYER_TWO = PLAYER_TWO_COLOR


class Side(AutoName):
    """Tile Sides."""

    OBVERSE = auto()
    REVERSE = auto()


class Movement(AutoName):
    """Tile movements."""

    CENTER_OBVERSE = auto()
    CENTER_REVERSE = auto()
    COMMAND = auto()
    DEFENSE = auto()
    DREAD = auto()
    EMPTY = auto()
    JUMP = auto()
    JUMP_SLIDE_D_D = auto()
    JUMP_SLIDE_D_L = auto()
    JUMP_SLIDE_D_R = auto()
    JUMP_SLIDE_L_L = auto()
    JUMP_SLIDE_R_R = auto()
    JUMP_SLIDE_U_L = auto()
    JUMP_SLIDE_U_R = auto()
    JUMP_SLIDE_U_U = auto()
    MOVE = auto()
    ORIGIN = auto()
    SLIDE_D_D = auto()
    SLIDE_D_L = auto()
    SLIDE_D_R = auto()
    SLIDE_L_L = auto()
    SLIDE_R_R = auto()
    SLIDE_U_L = auto()
    SLIDE_U_R = auto()
    SLIDE_U_U = auto()
    STRIKE = auto()


EMPTY = Movement.EMPTY
EMPTY_ROW = (
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
)


class Troop(AutoName):
    """Troop Types."""

    ASSASSIN = auto()
    BOWMAN = auto()
    CHAMPION = auto()
    DRAGOON = auto()
    DUCHESS = auto()
    DUKE = auto()
    FOOTMAN = auto()
    GENERAL = auto()
    KNIGHT = auto()
    LONGBOWMAN = auto()
    MARSHALL = auto()
    ORACLE = auto()
    PIKEMAN = auto()
    PRIEST = auto()
    RANGER = auto()
    SEER = auto()
    WIZARD = auto()


@dataclass
class TileSide:
    """Tile Side."""

    side: Side
    positions: BoardPositions
    origin: Movement = field(init=False)

    def __post_init__(self):
        """Sets additional attributes."""
        if self.side == Side.OBVERSE:
            self.origin = Movement.CENTER_OBVERSE
        else:
            self.origin = Movement.CENTER_REVERSE


class Tile(abc.ABC):
    """Tile."""

    @property
    @abc.abstractmethod
    def troop(self) -> Troop:
        """Troop type."""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def obverse(self) -> TileSide:
        """Tile obverse."""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def reverse(self) -> TileSide:
        """Tile reverse."""
        raise NotImplementedError

    @property
    def tile_board(self):
        """Base tile PNG."""
        return get_png("tile", "tile")

    @property
    def two_troop_images(self) -> bool:
        """If the tile has different images on the obverse and reverse."""
        return False

    def generate_tile(self, player: Player, side: Side) -> Image:
        """Generates a PNG of the tile.

        Args:
            player (Player): Player associated with the tile (determines color)
            side (Side): Side of the tile (determines movement placement)

        Returns:
            Image: PNG of the tile
        """
        board = getattr(self, side.value)

        base = generate_block_container(TILE_DIMS, player.value)
        base.paste(self.tile_board, ORIGIN, self.tile_board)

        for y, row in enumerate(board.positions):
            for x, col in enumerate(row):
                movements = (col,) if isinstance(col, Movement) else col
                for move in movements:
                    move = board.origin if move == Movement.ORIGIN else move
                    move_img = get_png("movements", move.value)
                    coordinates = get_board_coordinates(Point(x, y), TILE_SQUARE_PIXELS)
                    base.paste(move_img, coordinates, move_img)

        font_block = generate_font_block(self.troop.value.title())
        title_coords = get_board_coordinates(TITLE_LOCATION, TILE_SQUARE_PIXELS)
        base.paste(font_block, title_coords, font_block)

        if self.two_troop_images:
            icon = get_png("troops", f"{self.troop.value}-{side.value}")
        else:
            icon = get_png("troops", self.troop.value)

        icon_coords = get_board_coordinates(IMAGE_LOCATION, TILE_SQUARE_PIXELS)
        base.paste(icon, icon_coords, icon)

        return base
