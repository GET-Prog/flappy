import pygame
from flappy.helpers import get_image_path
from flappy.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    GRAVITY,
    SPEED,
    MAX_DOWN_ANGLE,
    DOWN_ANGLE,
    UP_ANGLE,
)


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [
            self.get_surface(filename)
            for filename in (
                "bluebird-upflap.png",
                "bluebird-midflap.png",
                "bluebird-downflap.png",
            )
        ]

        self.current_angle = 0
        self.current_speed = SPEED
        self.current_image = 0
        self.image = self.images[self.current_image]

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 4
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % len(self.images)

        self.current_angle -= DOWN_ANGLE

        if self.current_angle < -MAX_DOWN_ANGLE:
            self.current_angle = -MAX_DOWN_ANGLE

        self.image = pygame.transform.rotate(
            self.images[self.current_image], self.current_angle
        )

        self.current_speed += GRAVITY
        self.rect[1] += self.current_speed

    def bump(self):
        self.current_speed = -SPEED
        self.current_angle = UP_ANGLE

    def get_surface(self, filename, angle=0, scale=1.5):
        return pygame.transform.rotozoom(
            pygame.image.load(get_image_path(filename)).convert_alpha(),
            angle,
            scale,
        )
