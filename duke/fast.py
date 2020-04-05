import itertools
from os.path import isfile

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from duke import troops
from duke.constants import CURRENT_DIR
from duke.models.tile import Player, Side, Troop

app = FastAPI()

DIST_DIR = CURRENT_DIR.parent / "dist"
app.mount("/static", StaticFiles(directory=DIST_DIR.as_posix()), name="static")

templates = Jinja2Templates(directory="duke/assets/templates")


@app.get("/")
def index(request: Request):
    """Hello world."""
    return f"Read the docs: {request.base_url}docs"


@app.get("/troop/{troop}")
async def get_troop(request: Request, troop: Troop):
    """Renders tile image for a given troop."""
    troop_name = troop.value.title()
    troop_class = getattr(troops, troop_name)
    image_combos = itertools.product(Player, Side)
    images = []
    for combo in image_combos:
        player, side = combo
        file_name = f"{troop.value}-{player.name.lower()}-{side.value}.png"
        destination_path = DIST_DIR / file_name
        if not isfile(destination_path):
            tile = troop_class().generate_tile(player, side)
            tile.save(destination_path)
        images.append(file_name)

    return templates.TemplateResponse(
        "index.html", {"request": request, "images": images, "troop_name": troop_name},
    )
