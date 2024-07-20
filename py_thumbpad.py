import pygame
import donut
import button_pad
from utils import calculate_angle, get_direction, get_direction_expanded

class PyThumbPad:
    def __init__(self, position, quadrants=4):
        self.donut_outer_radius = 100
        self.donut_inner_radius = 90
        self.position = position
        self.donut_color = (123, 157, 243)
        self.button_color = (255, 255, 0)
        self.button_radius = 80
        self.donut = donut.Donut(self.position, self.donut_outer_radius, self.donut_inner_radius, self.donut_color)
        self.button_pad = button_pad.ButtonPad(self.position, self.button_radius, self.button_color) 
        self.current_angle = 0.0
        self.quadrants = quadrants
        self.directions = []
        self.touch_in_progress = False

    def update(self):
        self.button_pad.update()

    def render(self, screen):
        self.donut.render(screen)
        self.button_pad.render(screen)

    def listen_events(self, event):
        if not self.touch_in_progress or self.button_pad.dragging: 
            self.button_pad.listen_events(event, self.donut)
            self.directions = self.get_directions(0)
            self.current_angle = 0.0
            if self.button_pad.dragging:
                self.touch_in_progress = True
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.current_angle = calculate_angle(self.position[0], self.position[1], mouse_x, mouse_y )
                self.directions = self.get_directions(self.current_angle)
            if not self.button_pad.dragging:
                self.touch_in_progress = False

    def get_directions(self, current_angle):
        if self.quadrants == 4:
            return get_direction(current_angle)
        return get_direction_expanded(current_angle)