import pygame
from py_thumbpad import PY_THUMBPAD_Directions

class SingleSquare:
    def __init__(self, position, size, color, bounds) -> None:
        self.x = position[0]
        self.y = position[1]
        self.bounds_x = bounds[0]
        self.bounds_y = bounds[1]
        self.rect = pygame.Rect(self.x, self.y, size, size )
        self.color = color
        self.speed = 5
        self.size = 50

    def move(self, directions):
        if PY_THUMBPAD_Directions.LEFT in directions:
            self.rect.x -= self.speed
        if PY_THUMBPAD_Directions.RIGHT in directions:
            self.rect.x += self.speed
        if PY_THUMBPAD_Directions.TOP in directions:
            self.rect.y -= self.speed
        if PY_THUMBPAD_Directions.BOTTOM in directions:
            self.rect.y += self.speed

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.y < 0:
            self.rect.y = 0

        # Apply bounds checks
        self.rect.x = max(0, min(self.rect.x, self.bounds_x - self.size))
        self.rect.y = max(0, min(self.rect.y, self.bounds_y - self.size))

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)