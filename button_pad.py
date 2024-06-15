import pygame 

class ButtonPad:
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color

    def update(self):
        pass

    def render(self, screen):
        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, self.color, (self.radius, self.radius), self.radius)
        screen.blit(surface, (self.position[0] - self.radius, self.position[1] - self.radius))

