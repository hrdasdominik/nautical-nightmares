import random

import pygame

from config.config import read_config
from tiles.tile import Tile
from tiles.tile_sea_shallow import TileSeaShallow
from tiles.tile_sea_deep import TileSeaDeep
from tiles.tile_sea_abyssal import TileSeaAbyssal


class Chunk:
    def __init__(self, x: int, y: int, surface: pygame.surface.Surface):
        self._x = x
        self._y = y
        self._surface: pygame.surface.Surface = surface
        self._tile_data: dict[(int, int), Tile] = {}
        self._tile_size: int = 32
        self._tiles = self.generate()

    def generate(self):
        tile_grid = {}

        config: dict = read_config()
        window_size = config["window_size"]
        total_tiles_by_width = config["total_tiles_by_width"]
        total_tiles_by_height = config["total_tiles_by_height"]

        for axis_y in range(total_tiles_by_height):
            for axis_x in range(total_tiles_by_width):
                random_number = random.randint(1, 1000)

                if random_number == 1:
                    tile_type = TileSeaAbyssal
                elif random_number < 100:
                    tile_type = TileSeaDeep
                else:
                    tile_type = TileSeaShallow

                tile = tile_type(self._x, self._y, axis_x, axis_y, window_size,
                                 self._surface)

                tile_grid[axis_x, axis_y] = tile
        return tile_grid

    def draw(self):
        for tile in self._tiles.values():
            # target_x = self._x * self._tiles[(0, 0)].get_size()
            # target_y = self._y * self._tiles[(0, 0)].get_size()
            tile.draw()
