import json
import os

CONFIG_DATA = None


def create_config():
    global CONFIG_DATA
    CONFIG_DATA = {
        "language": "en",
        "window_size": (1280, 720),
        "tile_size": 32
    }

    if CONFIG_DATA["window_size"][0] % CONFIG_DATA["tile_size"] == 0:
        CONFIG_DATA["total_tiles_by_width"] = CONFIG_DATA["window_size"][0] // \
                                              CONFIG_DATA["tile_size"]
    else:
        CONFIG_DATA["total_tiles_by_width"] = int(
            CONFIG_DATA["window_size"][0] // CONFIG_DATA["tile_size"]) + 1

    if CONFIG_DATA["window_size"][1] % CONFIG_DATA["tile_size"] == 0:
        CONFIG_DATA["total_tiles_by_height"] = CONFIG_DATA["window_size"][1] // \
                                               CONFIG_DATA["tile_size"]
    else:
        CONFIG_DATA["total_tiles_by_height"] = int(
            CONFIG_DATA["window_size"][1] // CONFIG_DATA["tile_size"]) + 1

    with open("config.json", "w") as f:
        json.dump(CONFIG_DATA, f, indent=4)


def read_config():
    global CONFIG_DATA

    if CONFIG_DATA is not None:
        return CONFIG_DATA

    # just for development
    if os.path.exists("config.json"):
        os.remove("config.json")

    if not os.path.exists("config.json"):
        create_config()

    with open("config.json", "r") as f:
        CONFIG_DATA = json.load(f)

    return CONFIG_DATA
