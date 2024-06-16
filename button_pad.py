import pygame 
import math

def distance(point_1, point_2):
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)
class ButtonPad:
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color
        self.dragging = False
        self.setup()

    def setup(self):
        self.surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.x = self.position[0] - self.radius
        self.rect.y = self.position[1] - self.radius
        self.rect.width = self.radius * 2
        self.rect.height = self.radius * 2

    def listen_events(self, event): 
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN:
            if self.rect.collidepoint(mouse_pos):
                self.dragging = True

        if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.FINGERUP:
            self.dragging = False

        if self.dragging:
            self.update_position(mouse_pos)

        if (event.type == pygame.MOUSEMOTION or event.type == pygame.FINGERMOTION) and self.dragging:
            self.update_position(mouse_pos)

    def update_position(self, mouse_pos):
        self.rect.x = mouse_pos[0] - self.radius
        self.rect.y = mouse_pos[1] - self.radius

    def update(self):
        pass

    def render(self, screen):
        pygame.draw.circle(self.surface, self.color, (self.radius, self.radius), self.radius)
        screen.blit(self.surface, (self.rect.x, self.rect.y))
