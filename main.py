import asyncio
import pygame
from py_thumbpad import PyThumbPad
import sys

WIDTH, HEIGHT = 800, 600

class App:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Demo of ThumbPad")
    self.thumb_pad = PyThumbPad((150, HEIGHT - 150), 8)
    #font
    self.font = pygame.font.Font('assets/font/PixelSimpel.otf', 32)

  async def render(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            self.thumb_pad.listen_events(event)

        self.screen.fill((10, 220, 10))

        # bg to highlight the slider with theme 'one'
        pygame.draw.rect(self.screen, (123, 157, 243), (0, 0, self.screen.get_width(), 120))

        # printing the radian values and position
        text_surface = self.font.render(f'Angle: {self.thumb_pad.current_angle:.2f}°', True, (0,0,0))
        text_rect = text_surface.get_rect(center=(400, 50))
        self.screen.blit(text_surface, text_rect)

        text_surface = self.font.render(f'Direction: {", ".join( self.thumb_pad.directions )}', True, (0,0,0))
        text_rect = text_surface.get_rect(center=(400, 100))
        self.screen.blit(text_surface, text_rect)

        #printing the touches
        text_surface = self.font.render(f'Num of touches: {", ".join( self.touches.values())}', True, (0,0,0))
        text_rect = text_surface.get_rect(center=(400, 140))
        self.screen.blit(text_surface, text_rect)

        # update thumbpad
        self.thumb_pad.update()

        # render thumbpad
        self.thumb_pad.render(self.screen)

        #update the display
        pygame.display.flip()
        # clock
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)
        
asyncio.run(App().render())