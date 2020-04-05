from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    (Movement.MOVE, EMPTY, EMPTY, EMPTY, Movement.MOVE),
    (EMPTY, Movement.MOVE, Movement.EMPTY, Movement.MOVE, EMPTY),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    EMPTY_ROW,
    EMPTY_ROW,
)

_reverse_positions = (
    (EMPTY, Movement.STRIKE, EMPTY, Movement.STRIKE, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Pikeman(Tile):
    """Pikeman tile."""

    troop = Troop.PIKEMAN
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
