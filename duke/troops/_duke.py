from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    EMPTY_ROW,
    EMPTY_ROW,
    (EMPTY, Movement.SLIDE_L_L, Movement.ORIGIN, Movement.SLIDE_R_R, EMPTY),
    EMPTY_ROW,
    EMPTY_ROW,
)

_reverse_positions = (
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.SLIDE_U_U, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.SLIDE_D_D, EMPTY, EMPTY),
    EMPTY_ROW,
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Duke(Tile):
    """Duke tile."""

    troop = Troop.DUKE
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
