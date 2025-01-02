import pygame

from neural_network_ml import FRAME_RATE, SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def basic_renderer() -> None:
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        pygame.display.flip()

        clock.tick(FRAME_RATE)

    pygame.quit()
