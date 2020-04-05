from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    (Movement.STRIKE, EMPTY, Movement.STRIKE, EMPTY, Movement.STRIKE),
    EMPTY_ROW,
    (EMPTY, Movement.MOVE, Movement.ORIGIN, Movement.MOVE, EMPTY),
    EMPTY_ROW,
    EMPTY_ROW,
)

_reverse_positions = (
    (EMPTY, Movement.JUMP, Movement.MOVE, Movement.JUMP, EMPTY),
    (EMPTY, EMPTY, Movement.MOVE, EMPTY, EMPTY),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    (EMPTY, Movement.SLIDE_D_L, EMPTY, Movement.SLIDE_D_R, EMPTY),
    EMPTY_ROW,
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Dragoon(Tile):
    """Dragoon tile."""

    troop = Troop.DRAGOON
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
