import pygame

class Donut:
    def __init__(self, position, outer_radius, inner_radius, color):
        self.position = position
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius
        self.color = color

    def update(self):
        pass

    def render(self, screen):
        # outher circle
        outer_surface = pygame.Surface((self.outer_radius * 2, self.outer_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(outer_surface, (0,0,0), (self.outer_radius, self.outer_radius), self.outer_radius)
        outer_mask = pygame.mask.from_surface(outer_surface)

        # inner circle
        inner_surface = pygame.Surface((self.outer_radius * 2, self.outer_radius * 2), pygame.SRCALPHA)
        inner_surface.fill((0,0,0,0))
        pygame.draw.circle(inner_surface, (0, 0, 0), (self.outer_radius, self.outer_radius), self.inner_radius)

        # Subtract the inner mask from the outer mask to create the donut mask
        donut_mask = outer_mask.to_surface(setcolor=self.color, unsetcolor=(0, 0, 0, 0))
        donut_mask.blit(inner_surface, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        screen.blit(donut_mask, (self.position[0] - self.outer_radius, self.position[1] - self.outer_radius))