from duke.models import tile


def test_tile__tile_board__returns_png(mocker):
    mock_get_png = mocker.patch("duke.models.tile.get_png")

    class Noop(tile.Tile):
        obverse = None
        reverse = None
        troop = None

    Noop().tile_board
    mock_get_png.assert_called_with("tile", "tile")


def test_tile__two_troop_images__returns_false():
    class Noop(tile.Tile):
        obverse = None
        reverse = None
        troop = None

    assert not Noop().two_troop_images


#  def generate_tile(self, player: Player, side: Side) -> Image:
#         board = getattr(self, side.value)

#         base = generate_block_container(TILE_DIMS, player.value)
#         base.paste(self.tile_board, ORIGIN, self.tile_board)

#         for y, row in enumerate(board.positions):
#             for x, col in enumerate(row):
#                 movements = (col,) if isinstance(col, Movement) else col
#                 for move in movements:
#                     move = board.origin if move == Movement.ORIGIN else move
#                     move_img = get_png("movements", move.value)
#                     coordinates = get_board_coordinates(Point(x, y), TILE_SQUARE_PIXELS)
#                     base.paste(move_img, coordinates, move_img)

#         font_block = generate_font_block(self.troop.value.title())
#         title_coords = get_board_coordinates(TITLE_LOCATION, TILE_SQUARE_PIXELS)
#         base.paste(font_block, title_coords, font_block)

#         if self.two_troop_images:
#             icon = get_png("troops", f"{self.troop.value}-{side.value}")
#         else:
#             icon = get_png("troops", self.troop.value)

#         icon_coords = get_board_coordinates(IMAGE_LOCATION, TILE_SQUARE_PIXELS)
#         base.paste(icon, icon_coords, icon)

#         return base
