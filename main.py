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


class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass

    def draw(self):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), OBJ_SIZE)


def main() -> None:
    running: bool = True
    clock = pygame.time.Clock()

    objects = []
    temp_obj_pos = None

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    t_x, t_y = temp_obj_pos
                    obj = Spacecraft(t_x, t_y, 0, 0, SHIP_MASS)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

        win.blit(BG, (0, 0))

        if temp_obj_pos:
            pygame.draw.line(win, WHITE,temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(win, RED, temp_obj_pos, OBJ_SIZE)

        for obj in objects:
            obj.draw()

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()