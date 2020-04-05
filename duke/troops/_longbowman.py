from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    EMPTY_ROW,
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (EMPTY, Movement.MOVE, Movement.ORIGIN, Movement.MOVE, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
)

_reverse_positions = (
    (EMPTY, EMPTY, Movement.STRIKE, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.STRIKE, EMPTY, EMPTY),
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    (EMPTY, Movement.MOVE, EMPTY, Movement.MOVE, EMPTY),
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Longbowman(Tile):
    """Longbowman tile."""

    troop = Troop.LONGBOWMAN
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
