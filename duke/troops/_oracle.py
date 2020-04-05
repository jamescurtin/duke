from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    EMPTY_ROW,
    (EMPTY, Movement.MOVE, EMPTY, Movement.MOVE, EMPTY),
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    (EMPTY, Movement.MOVE, EMPTY, Movement.MOVE, EMPTY),
    EMPTY_ROW,
)

_reverse_positions = (
    EMPTY_ROW,
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    EMPTY_ROW,
    EMPTY_ROW,
)


_obverse = TileSide(Side.OBVERSE, _obverse_positions)
_reverse = TileSide(Side.REVERSE, _reverse_positions)


class Oracle(Tile):
    """Oracle tile."""

    troop = Troop.ORACLE
    two_troop_images = True

    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
