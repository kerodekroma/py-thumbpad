import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Linear Ease Motion of a Circle")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Circle properties
circle_radius = 20

# Starting and ending positions
start_pos = (100, 300)
end_pos = (700, 300)
current_pos = list(start_pos)

# Animation properties
duration = 2  # Duration in seconds
start_time = None

def ease_in_out(t):
    # Cubic easing function: ease-in and ease-out
    return t * t * (3 - 2 * t)

def linear_interpolate(start, end, t):
    return start + t * (end - start)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_time = pygame.time.get_ticks() / 1000  # Start the animation

    # Clear the screen
    screen.fill(BLACK)

    # If the animation has started
    if start_time is not None:
        current_time = pygame.time.get_ticks() / 1000
        elapsed_time = current_time - start_time
        t = min(elapsed_time / duration, 1)  # Clamp t to [0, 1]

         # Apply easing function
        eased_t = ease_in_out(t)

        current_pos[0] = linear_interpolate(start_pos[0], end_pos[0], eased_t)
        current_pos[1] = linear_interpolate(start_pos[1], end_pos[1], eased_t)

    # Draw the circle at the current position
    pygame.draw.circle(screen, BLUE, (int(current_pos[0]), int(current_pos[1])), circle_radius)

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
