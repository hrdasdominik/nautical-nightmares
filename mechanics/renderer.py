import pygame

from chunks.dynamic_chunk import DynamicChunk
from config.config import read_config
from mechanics.camera import Camera
from mechanics.debugger import Debugger
from player.player import Player
from utils.utils import singleton


@singleton
class Renderer:
    def __init__(self):
        self._window_size: tuple[int, int] = read_config()["window_size"]
        self._is_running: bool = True
        self._dynamic_chunk: DynamicChunk = DynamicChunk()
        self._player: Player = Player((0, 0))
        self._clock: pygame.time.Clock = pygame.time.Clock()
        self._screen: pygame.Surface = pygame.display.set_mode(
            self._window_size,
            0,
            32)
        self._display: pygame.Surface = pygame.Surface(
            (self._window_size[0] // 2, self._window_size[1] // 2)
        )
        self._debugger: Debugger = Debugger()
        self._camera: Camera = Camera(self._player, self._window_size)

    def run(self):
        self.set_game_title_on_window()
        self.set_icon_on_window()

        while self._is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False

            self._dynamic_chunk.prepare_chunks()

            keys = pygame.key.get_pressed()

            direction_x, direction_y = 0, 0
            if keys[pygame.K_LEFT]:
                direction_x = -1
            if keys[pygame.K_RIGHT]:
                direction_x = 1
            if keys[pygame.K_UP]:
                direction_y = -1
            if keys[pygame.K_DOWN]:
                direction_y = 1

            for coordinates, surface in self._dynamic_chunk.get_virtual_surfaces().items():
                # target_x: int = coordinates[0] - 1 + int(round(
                #     self._camera.scroll()[0] / read_config()["tile_size"]))
                # target_y: int = coordinates[1] - 1 + int(round(
                #     self._camera.scroll()[1] / read_config()["tile_size"]))
                #
                # target_chunk: tuple[int, int] = (target_x, target_y)

                x = coordinates[0]  # - self._camera.scroll()[0]
                y = coordinates[1]  # - self._camera.scroll()[1]
                self._display.blit(surface, (x, y))

            if direction_x != 0 or direction_y != 0:
                self._player.move(direction_x, direction_y,
                                  self._camera.scroll())

            self._player.draw(self._display, self._camera.scroll()[0],
                              self._camera.scroll()[1])

            # self._camera.update(self._player.get_x(), self._player.get_y(),
            #                     self._window_size)

            self._debugger.render_player_coordinates(self._player,
                                                     self._display)

            self._debugger.render_camera_coordinates(self._camera,
                                                     self._display)

            self._screen.blit(
                pygame.transform.scale(self._display, self._window_size),
                (0, 0))

            pygame.display.update()
            self._clock.tick(60)

    @staticmethod
    def set_game_title_on_window():
        pygame.display.set_caption("Nautical Nightmares")

    @staticmethod
    def set_icon_on_window():
        # pygame.display.set_icon()
        pass
