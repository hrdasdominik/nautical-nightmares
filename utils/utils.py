from typing import Any

import pygame

from config.config import read_config


def create_surfaces() -> dict[(int, int), pygame.surface.Surface]:
    config: Any = read_config()
    surfaces: dict[(int, int), pygame.surface.Surface] = {}

    x = -2
    y = -2
    count = 0
    while count < 25:
        if count % 5 == 0 and count != 0:
            y += 1
            x = -2

        surfaces[(x, y)] = pygame.surface.Surface(config["window_size"])

        x += 1
        count += 1

    return surfaces


def round_up(number, multiple):
    return number + ((multiple - (number % multiple)) % multiple)


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
