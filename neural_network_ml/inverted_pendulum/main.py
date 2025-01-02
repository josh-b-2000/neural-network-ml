import pygame

from neural_network_ml import FRAME_RATE, SCREEN_HEIGHT, SCREEN_WIDTH
from neural_network_ml.inverted_pendulum.cart import Cart
from neural_network_ml.inverted_pendulum.pendulum import Pendulum
from neural_network_ml.inverted_pendulum.track import Track
from neural_network_ml.inverted_pendulum.utils import calculate_accelerations
from neural_network_ml.main import clock, screen


def run() -> None:
    running = True
    pendulum = Pendulum(initial_angle=0.6)
    cart = Cart()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("grey")

        # Track
        pygame.draw.line(screen, "black", Track.start, Track.end, 1)

        # Pendulum
        cart_position = pygame.Vector2(cart.x * SCREEN_WIDTH, cart.y * SCREEN_HEIGHT)
        pendulum_position = cart_position + pendulum.get_relative_coords()
        pygame.draw.circle(screen, "black", cart_position, 5)
        pygame.draw.line(screen, "black", cart_position, pendulum_position, 3)
        pygame.draw.circle(screen, "red", pendulum_position, 10)

        # Update function
        accelerations = calculate_accelerations(pendulum, cart, force=0.0, drag_coefficient=10.0)
        pendulum.update(accelerations.theta_ddot)
        cart.update(accelerations.x_ddot)

        pygame.display.flip()

        clock.tick(FRAME_RATE)

    pygame.quit()
