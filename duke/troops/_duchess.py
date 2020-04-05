from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

COMMAND_MOVE = (Movement.COMMAND, Movement.MOVE)

_obverse_positions = (
    EMPTY_ROW,
    EMPTY_ROW,
    (Movement.COMMAND, COMMAND_MOVE, Movement.ORIGIN, COMMAND_MOVE, Movement.COMMAND),
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
)

_reverse_positions = _obverse_positions


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Duchess(Tile):
    """Duchess tile."""

    troop = Troop.DUCHESS
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
