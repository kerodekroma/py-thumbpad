import pygame
import sys
import math

# Easing functions
def ease_in_out(t):
    return t * t * (3 - 2 * t)

def ease_in(t):
    return t * t

def ease_out(t):
    return t * (2 - t)

def linear(t):
    return t

# Dictionary of easing functions
easing_functions = {
    'ease_in_out': ease_in_out,
    'ease_in': ease_in,
    'ease_out': ease_out,
    'linear': linear
}

class Tween:
    def __init__(self, obj, attr, start_value, end_value, duration, easing_func_name):
        self.obj = obj
        self.attr = attr
        self.start_value = start_value
        self.end_value = end_value
        self.duration = duration
        self.easing_func = easing_functions[easing_func_name]
        self.start_time = None

    def start(self):
        self.start_time = pygame.time.get_ticks() / 1000

    def update(self):
        if self.start_time is None:
            return
        
        current_time = pygame.time.get_ticks() / 1000
        elapsed_time = current_time - self.start_time
        t = min(elapsed_time / self.duration, 1)  # Clamp t to [0, 1]
        
        eased_t = self.easing_func(t)
        current_value = self.interpolate(self.start_value, self.end_value, eased_t)

        # Set the current value to the object's attribute
        setattr(self.obj, self.attr, current_value)

    def interpolate(self, start, end, t):
        return start + t * (end - start)

    @classmethod
    def tween(cls, obj, attr, start_value, end_value, duration, easing_func_name):
        tween_instance = cls(obj, attr, start_value, end_value, duration, easing_func_name)
        tween_instance.start()
        return tween_instance

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dynamic Tween Class Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Circle properties
circle = Circle(100, 300, 20)

# Create Tween objects for x and y positions
tweens = [
    Tween.tween(circle, 'x', 100, 700, 2, 'ease_in_out'),
    Tween.tween(circle, 'y', 300, 300, 2, 'ease_in_out')  # This is static but added for completeness
]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for tween in tweens:
                    tween.start()

    # Update the tweens
    for tween in tweens:
        tween.update()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the circle at the current position
    pygame.draw.circle(screen, BLUE, (int(circle.x), int(circle.y)), circle.radius)

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
