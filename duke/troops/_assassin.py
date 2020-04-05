from duke.models.tile import EMPTY, EMPTY_ROW, Movement, Side, Tile, TileSide, Troop

_obverse_positions = (
    (EMPTY, EMPTY, Movement.JUMP_SLIDE_U_U, EMPTY, EMPTY,),
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    EMPTY_ROW,
    (Movement.JUMP_SLIDE_D_L, EMPTY, EMPTY, EMPTY, Movement.JUMP_SLIDE_D_R,),
)

_reverse_positions = (
    (Movement.JUMP_SLIDE_U_L, EMPTY, EMPTY, EMPTY, Movement.JUMP_SLIDE_U_R,),
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.ORIGIN, EMPTY, EMPTY),
    EMPTY_ROW,
    (EMPTY, EMPTY, Movement.JUMP_SLIDE_D_D, EMPTY, EMPTY,),
)


class Assassin(Tile):
    """Assassin tile."""

    troop = Troop.ASSASSIN
    obverse = TileSide(Side.OBVERSE, _obverse_positions)
    reverse = TileSide(Side.REVERSE, _reverse_positions)
