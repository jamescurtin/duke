from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (EMPTY, Movement.MOVE, Movement.ORIGIN, Movement.MOVE, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    EMPTY_ROW,
)

_reverse_positions = (
    (EMPTY, Movement.JUMP, EMPTY, Movement.JUMP, EMPTY),
    EMPTY_ROW,
    (EMPTY, Movement.JUMP, Movement.ORIGIN, Movement.JUMP, EMPTY),
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Knight(Tile):
    """Knight tile."""

    troop = Troop.KNIGHT
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
