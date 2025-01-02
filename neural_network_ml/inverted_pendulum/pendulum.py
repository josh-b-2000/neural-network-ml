import math

import pygame

from neural_network_ml import SCREEN_WIDTH, TIME_DELTA


class Pendulum:
    # Constants
    MASS: float = 0.1
    LENGTH: float = 0.1

    # Position constraints
    THETA_MAX: float = 2.0 * math.pi
    THETA_MIN: float = 0.0

    # Variables
    theta: float
    theta_dot: float

    def __init__(self, *, initial_angle: float) -> None:
        self.theta = initial_angle
        self.theta_dot = 0.0

    def update(self, theta_ddot: float) -> None:
        self.theta_dot += theta_ddot * TIME_DELTA

        self.theta += self.theta_dot * TIME_DELTA

        if self.theta > 2.0 * math.pi:
            self.theta = self.theta - 2.0 * math.pi
        if self.theta < 0.0:
            self.theta = 2.0 * math.pi - self.theta

    def get_relative_coords(self) -> pygame.Vector2:
        return pygame.Vector2(
            -self.LENGTH * math.sin(self.theta), self.LENGTH * math.cos(self.theta)
        ) * SCREEN_WIDTH
