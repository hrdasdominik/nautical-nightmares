import pygame

from tiles.tile import Tile


class TileIsland(Tile):
    def __init__(self, x_chunk: int, y_chunk: int, x_axis: int, y_axis: int,
                 window_size: tuple[int, int], surface: pygame.Surface):
        super().__init__(x_chunk, y_chunk, x_axis, y_axis, window_size, surface)
        self._color: tuple[int, int, int] = (246, 215, 176)
