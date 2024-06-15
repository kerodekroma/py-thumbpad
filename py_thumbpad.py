import pygame
import donut
import button_pad

class PyThumbPad:
    def __init__(self, position):
        self.donut_outer_radius = 70
        self.donut_inner_radius = 65
        self.position = position
        self.donut_color = (123, 157, 243)
        self.button_color = (255, 255, 0)
        self.donut = donut.Donut(self.position, self.donut_outer_radius, self.donut_inner_radius, self.donut_color)
        self.button_pad = button_pad.ButtonPad(self.position, 30, self.button_color) 

    def render(self, screen):
        self.donut.render(screen)
        self.button_pad.render(screen)

    def update(self, screen):
        pass

    def listen_events(self, event):
        pass