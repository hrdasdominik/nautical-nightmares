import pygame

from config.config import read_config
from utils.utils import singleton


@singleton
class Player:
    def __init__(self, coordination: tuple[int, int]):
        self._x: int = coordination[0]
        self._y: int = coordination[1]
        self._color: tuple[int, int, int] = (0, 255, 0)
        self._speed: int = 2
        self._tile_size: tuple[int, int] = read_config()["tile_size"]

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def draw(self, surface, camera_x=0, camera_y=0):
        pygame.draw.rect(surface, self._color, (
            self._x - camera_x, self._y - camera_y, self._tile_size,
            self._tile_size))

    def move(self, direction_x: int, direction_y: int,
             camera_scroll: tuple[float, float]):
        self._x += direction_x * self._speed  # - int(camera_scroll[0])
        self._y += direction_y * self._speed  # - int(camera_scroll[1])
