from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

COMMAND_MOVE = (Movement.COMMAND, Movement.MOVE)

_obverse_positions = (
    (EMPTY, Movement.JUMP, EMPTY, Movement.JUMP, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (Movement.MOVE, EMPTY, Movement.ORIGIN, EMPTY, Movement.MOVE),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    EMPTY_ROW,
)

_reverse_positions = (
    (EMPTY, Movement.JUMP, EMPTY, Movement.JUMP, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (Movement.MOVE, COMMAND_MOVE, Movement.ORIGIN, COMMAND_MOVE, Movement.MOVE),
    (EMPTY, Movement.COMMAND, Movement.COMMAND, Movement.COMMAND, EMPTY),
    EMPTY_ROW,
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class General(Tile):
    """General tile."""

    troop = Troop.GENERAL
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
