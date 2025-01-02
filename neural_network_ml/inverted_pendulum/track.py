import pygame

from neural_network_ml import SCREEN_HEIGHT, SCREEN_WIDTH


class Track:
    start: pygame.Vector2 = pygame.Vector2(0.1 * SCREEN_WIDTH, 0.5 * SCREEN_HEIGHT)
    end: pygame.Vector2 = pygame.Vector2(0.9 * SCREEN_WIDTH, 0.5 * SCREEN_HEIGHT)
