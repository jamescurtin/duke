from duke.models.tile import EMPTY, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
    (EMPTY, Movement.MOVE, EMPTY, Movement.MOVE, EMPTY),
    (Movement.JUMP, EMPTY, Movement.ORIGIN, EMPTY, Movement.JUMP),
    (EMPTY, Movement.MOVE, EMPTY, Movement.MOVE, EMPTY),
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
)

_reverse_positions = (
    (Movement.JUMP, EMPTY, EMPTY, EMPTY, Movement.JUMP),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (EMPTY, Movement.MOVE, Movement.ORIGIN, Movement.MOVE, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (Movement.JUMP, EMPTY, EMPTY, EMPTY, Movement.JUMP),
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Seer(Tile):
    """Seer tile."""

    troop = Troop.SEER
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
