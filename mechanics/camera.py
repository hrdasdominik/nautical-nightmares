from player.player import Player
from utils.utils import singleton


@singleton
class Camera:
    def __init__(self, player: Player, window_size: tuple[int, int]):
        self._player: Player = player
        self._window_size: tuple[int, int] = window_size
        self._x: int = 0
        self._y: int = 0

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def set_x(self, x: int):
        self._x = x

    def set_y(self, y: int):
        self._y = y

    def update(self, target_x: int, target_y: int,
               window_size: tuple[int, int]):
        self._x = -target_x + window_size[0]
        self._y = -target_y + window_size[1]

    def scroll(self) -> tuple[float, float]:
        return (
            self._player.get_x() - self._x - self._window_size[0] / 20,
            self._player.get_y() - self._y - self._window_size[1] / 20
        )
