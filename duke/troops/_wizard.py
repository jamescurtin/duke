from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    EMPTY_ROW,
    (EMPTY, Movement.MOVE, Movement.MOVE, Movement.MOVE, EMPTY),
    (EMPTY, Movement.MOVE, Movement.ORIGIN, Movement.MOVE, EMPTY),
    (EMPTY, Movement.MOVE, Movement.MOVE, Movement.MOVE, EMPTY),
    EMPTY_ROW,
)

_reverse_positions = (
    (Movement.JUMP, EMPTY, Movement.JUMP, EMPTY, Movement.JUMP),
    EMPTY_ROW,
    (Movement.JUMP, EMPTY, Movement.ORIGIN, EMPTY, Movement.JUMP),
    EMPTY_ROW,
    (Movement.JUMP, EMPTY, Movement.JUMP, EMPTY, Movement.JUMP),
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Wizard(Tile):
    """Wizard tile."""

    troop = Troop.WIZARD
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
