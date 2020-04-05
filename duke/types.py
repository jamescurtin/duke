from typing import TYPE_CHECKING, NamedTuple, Tuple, Union

if TYPE_CHECKING:
    from duke.models.tile import Movement


class RGBA(NamedTuple):
    """RGBA color values."""

    r: int
    g: int
    b: int
    a: int


class Dimensions(NamedTuple):
    """Dimensions of a rectangle."""

    width: int
    height: int


class Point(NamedTuple):
    """Point coordinates."""

    x: Union[int, float]
    y: Union[int, float]


ControlMovement = Tuple["Movement", "Movement"]
BoardPosition = Union["Movement", ControlMovement]
BoardRow = Tuple[
    BoardPosition, BoardPosition, BoardPosition, BoardPosition, BoardPosition
]
BoardPositions = Tuple[BoardRow, BoardRow, BoardRow, BoardRow, BoardRow]
