import pygame

class SingleSquare:
    def __init__(self, position, size, color) -> None:
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.color = color
        self.speed = 5
        self.size = 50

    def move(self, directions):
        if "left" in directions:
            self.x -= self.speed
        if "right" in directions:
            self.x += self.speed
        if "top" in directions:
            self.y -= self.speed
        if "bottom" in directions:
            self.y += self.speed

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))