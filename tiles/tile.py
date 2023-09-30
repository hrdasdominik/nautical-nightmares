import pygame

from config.config import read_config


class Tile:
    def __init__(self, x_chunk: int, y_chunk: int, x_axis: int, y_axis: int,
                 window_size: tuple[int, int], surface: pygame.Surface):
        self._size: int = read_config()["tile_size"]
        self._x_axis: int = x_axis
        self._y_axis: int = y_axis
        self._x_pixels: int = (x_chunk * window_size[0]) + (
                self._x_axis * self._size)
        self._y_pixels: int = (y_chunk * window_size[1]) + (
                self._y_axis * self._size)
        self._color: tuple[int, int, int] = (255, 255, 255)
        self._surface: pygame.Surface = surface

    def get_x_pixels(self) -> int:
        return self._x_pixels

    def get_y_pixels(self) -> int:
        return self._y_pixels

    def get_size(self) -> int:
        return self._size

    def draw(self):
        pygame.draw.rect(self._surface, self._color,
                         (self._x_pixels, self._y_pixels, self._size,
                          self._size))
