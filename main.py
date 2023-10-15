import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot Effect")

PLANET_MASS: int = 100
SHIP_MASS: int = 5
G: int = 5
FPS: int = 60
PLANET_SIZE: int = 50
OBJ_SIZE: int = 5
VEL_SCALE: int = 100

BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

WHITE: tuple = (255, 255, 255)
RED: tuple = (255, 0, 0)
BLUE: tuple = (0, 0, 255)


def main() -> None:
    running: bool = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        win.blit(BG, (0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()