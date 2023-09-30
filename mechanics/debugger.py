import pygame

from mechanics.camera import Camera
from player.player import Player


class Debugger:
    def __init__(self):
        self.my_font: pygame.font.Font = pygame.font.SysFont('Comic Sans MS',
                                                             15)

    def render_player_coordinates(self, player: Player,
                                  surface: pygame.Surface):
        text_surface = self.my_font.render(
            f'Player: ({player.get_x()}, {player.get_y()})', False,
            (255, 0, 0))
        surface.blit(text_surface, (10, 10))

    def render_camera_coordinates(self, camera: Camera,
                                  surface: pygame.Surface):
        text_surface = self.my_font.render(
            f'Camera: ({camera.get_x()}, {camera.get_y()})', False,
            (255, 0, 0))
        surface.blit(text_surface, (10, 30))
