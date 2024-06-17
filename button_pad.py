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

    def listen_events(self, event, donut): 
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN:
            # Check if the click is inside the circle
            if distance(mouse_pos, [self.rect.x + self.radius, self.rect.y + self.radius]) <= self.radius:
                self.dragging = True

        if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.FINGERUP:
            self.dragging = False

        if (event.type == pygame.MOUSEMOTION or event.type == pygame.FINGERMOTION) and self.dragging:
            self.update_position(mouse_pos, donut)

    def update_position(self, mouse_pos, donut):
        dist_to_center = distance(mouse_pos, donut.position)

        # Ensure the small circle stays within the container
        if dist_to_center + self.radius <= donut.outer_radius:
            self.rect.x = mouse_pos[0]
            self.rect.y = mouse_pos[1]
        
        if dist_to_center + self.radius > donut.outer_radius:
            angle = math.atan2(mouse_pos[1] - donut.position[1], mouse_pos[0] - donut.position[0])
            self.rect.x = donut.position[0] + ( donut.outer_radius - self.radius ) * math.cos(angle) 
            self.rect.y = donut.position[1] + ( donut.outer_radius - self.radius ) * math.sin(angle) 

        self.rect.x = self.rect.x - self.radius
        self.rect.y = self.rect.y - self.radius

    def update(self):
        pass

    def render(self, screen):
        pygame.draw.circle(self.surface, self.color, (self.radius, self.radius), self.radius)
        screen.blit(self.surface, (self.rect.x, self.rect.y))
