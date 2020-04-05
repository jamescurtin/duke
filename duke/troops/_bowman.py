from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (Movement.JUMP, Movement.MOVE, Movement.ORIGIN, Movement.MOVE, Movement.JUMP),
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
)

_reverse_positions = (
    (EMPTY, EMPTY, Movement.STRIKE, EMPTY, EMPTY),
    (EMPTY, Movement.STRIKE, Movement.MOVE, Movement.STRIKE, EMPTY),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    (EMPTY, Movement.MOVE, EMPTY, Movement.MOVE, EMPTY),
    EMPTY_ROW,
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Bowman(Tile):
    """Bowman tile."""

    troop = Troop.BOWMAN
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
