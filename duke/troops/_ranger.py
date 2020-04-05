from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    (EMPTY, Movement.JUMP, EMPTY, Movement.JUMP, EMPTY),
    (Movement.JUMP, EMPTY, Movement.SLIDE_U_U, EMPTY, Movement.JUMP),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.SLIDE_D_D, EMPTY, EMPTY),
    EMPTY_ROW,
)

_reverse_positions = (
    EMPTY_ROW,
    (EMPTY, Movement.SLIDE_U_L, EMPTY, Movement.SLIDE_U_R, EMPTY),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    EMPTY_ROW,
    (EMPTY, Movement.JUMP, EMPTY, Movement.JUMP, EMPTY),
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Ranger(Tile):
    """Ranger tile."""

    troop = Troop.RANGER
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
