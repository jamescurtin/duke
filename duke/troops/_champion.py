from duke.models.tile import EMPTY, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (Movement.JUMP, Movement.MOVE, Movement.ORIGIN, Movement.MOVE, Movement.JUMP),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
)

_reverse_positions = (
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.STRIKE, EMPTY, EMPTY),
    (Movement.JUMP, Movement.STRIKE, Movement.ORIGIN, Movement.STRIKE, Movement.JUMP),
    (EMPTY, EMPTY, Movement.STRIKE, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.JUMP, EMPTY, EMPTY),
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Champion(Tile):
    """Champion tile."""

    troop = Troop.CHAMPION
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
