from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

COMMAND_MOVE = (Movement.COMMAND, Movement.MOVE)

_obverse_positions = (
    (Movement.JUMP, EMPTY, EMPTY, EMPTY, Movement.JUMP),
    EMPTY_ROW,
    (EMPTY, Movement.SLIDE_L_L, Movement.ORIGIN, Movement.SLIDE_R_R, EMPTY),
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
)

_reverse_positions = (
    EMPTY_ROW,
    (EMPTY, COMMAND_MOVE, COMMAND_MOVE, COMMAND_MOVE, EMPTY),
    (Movement.MOVE, Movement.MOVE, Movement.ORIGIN, Movement.MOVE, Movement.MOVE),
    (EMPTY, Movement.MOVE, EMPTY, Movement.MOVE, EMPTY),
    EMPTY_ROW,
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Marshall(Tile):
    """Marshall tile."""

    troop = Troop.MARSHALL
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
