import asyncio
import pygame
import sys
from single_square import SingleSquare
from py_thumbpad import PyThumbPad, PY_THUMBPAD_Directions

WIDTH, HEIGHT = 800, 600

# COLORS PALETTE: https://lospec.com/palette-list/akc12
PALETTE = [
   pygame.Color(color) for color in 
   ["#201127",
   "#201433", 
   "#1b1e34", 
   "#355d68", 
   "#6aaf9d", 
   "#94c5ac", 
   "#ffeb99", 
   "#ffc27a", 
   "#ec9a6d", 
   "#d9626b", 
   "#c24b6e", 
   "#a73169"
]]

class App:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Demo of ThumbPad")
    self.thumb_pad = PyThumbPad((150, HEIGHT - 150), {
       "quadrants": 8,
       "button_color": PALETTE[2],
       "donut_color": PALETTE[5],
       "donut_bg_color": PALETTE[3],
    })
    #font
    self.font = pygame.font.Font('assets/font/PixelSimpel.otf', 32)

    #single square
    square_size = 50
    self.single_square = SingleSquare(( ( WIDTH - square_size )//2, (HEIGHT - square_size)//2 ), square_size, PALETTE[7], (WIDTH, HEIGHT))
  async def render(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            self.thumb_pad.listen_events(event)

        self.screen.fill(PALETTE[1])


        # Check the direction the thumbpad is pointing to
        if PY_THUMBPAD_Directions.TOP in self.thumb_pad.directions:
            print("Moving UP!")
        elif PY_THUMBPAD_Directions.BOTTOM in self.thumb_pad.directions:
            print("Moving DOWN!")
        elif PY_THUMBPAD_Directions.LEFT in self.thumb_pad.directions:
            print("Moving LEFT!")
        elif PY_THUMBPAD_Directions.RIGHT in self.thumb_pad.directions:
            print("Moving RIGHT!")

        self.single_square.move(self.thumb_pad.directions)
        # bg to highlight the slider with theme 'one'
        pygame.draw.rect(self.screen, PALETTE[0], (0, 0, self.screen.get_width(), 120))

        # printing the radian values and position
        text_surface = self.font.render(f'Angle: {self.thumb_pad.current_angle:.2f}°', True, PALETTE[5])
        text_rect = text_surface.get_rect(center=(400, 50))
        self.screen.blit(text_surface, text_rect)

        text_surface = self.font.render(f'Direction: {", ".join([direction.name for direction in self.thumb_pad.directions])}', True, PALETTE[5])
        text_rect = text_surface.get_rect(center=(400, 100))
        self.screen.blit(text_surface, text_rect)

        #on boarding
        text_surface = self.font.render("<-- You should press and drag it", True, PALETTE[5])
        text_rect = text_surface.get_rect(center=(WIDTH - 230, HEIGHT - 150))
        self.screen.blit(text_surface, text_rect)

        # update thumbpad
        self.thumb_pad.update()

        # render thumbpad
        self.thumb_pad.render(self.screen)

        # render square example
        self.single_square.render(self.screen)

        #update the display
        pygame.display.flip()
        # clock
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)
        
asyncio.run(App().render())