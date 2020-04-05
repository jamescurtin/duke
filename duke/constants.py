from pathlib import Path

###########################
# ASSETS
###########################
CURRENT_DIR = Path(__file__).resolve().parent
ASSET_DIR = CURRENT_DIR / "assets"
TILES_DIR = ASSET_DIR / "tiles"

TILE_FONT = (ASSET_DIR / "fonts" / "YatraOne-Regular.ttf").as_posix()
