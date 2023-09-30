import pygame

from config.config import read_config
from chunks.chunk import Chunk
from utils.utils import create_surfaces, singleton

config: dict = read_config()


@singleton
class DynamicChunk:
    def __init__(self):
        self._virtual_surfaces: dict[(int, int), pygame.surface.Surface] = {}
        self._is_loaded: bool = False

    def get_virtual_surfaces(self) -> dict[(int, int), pygame.surface.Surface]:
        return self._virtual_surfaces

    def prepare_chunks(self):
        if not self._is_loaded:
            surfaces: dict[(int, int), pygame.surface.Surface] = create_surfaces()
            for coordinates, surface in surfaces.items():
                Chunk(coordinates[0], coordinates[1], surface).draw()
            self._virtual_surfaces = surfaces
            self._is_loaded = True
