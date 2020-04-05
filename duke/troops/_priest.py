from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    EMPTY_ROW,
    (EMPTY, Movement.SLIDE_U_L, EMPTY, Movement.SLIDE_U_R, EMPTY),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    (EMPTY, Movement.SLIDE_D_L, EMPTY, Movement.SLIDE_D_R, EMPTY),
    EMPTY_ROW,
)

_reverse_positions = (
    (Movement.JUMP, EMPTY, EMPTY, EMPTY, Movement.JUMP),
    (EMPTY, Movement.MOVE, EMPTY, Movement.MOVE, EMPTY),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    (EMPTY, Movement.MOVE, EMPTY, Movement.MOVE, EMPTY),
    (Movement.JUMP, EMPTY, EMPTY, EMPTY, Movement.JUMP),
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Priest(Tile):
    """Priest tile."""

    troop = Troop.PRIEST
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
