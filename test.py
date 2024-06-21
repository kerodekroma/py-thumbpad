import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Calculate Angle Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Reference coordinate
reference_coord = (400, 300)

# Initialize font
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Function to calculate angle in degrees from reference_coord to mouse position
def calculate_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    radians = math.atan2(dy, dx)
    degrees = math.degrees(radians)
    return degrees

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate angle
    angle = calculate_angle(reference_coord[0], reference_coord[1], mouse_x, mouse_y)

    # Create the text surface
    text_surface = font.render(f'Angle: {angle:.2f}°', True, WHITE)
    text_rect = text_surface.get_rect(center=(400, 50))
    screen.blit(text_surface, text_rect)

    # Draw the reference point and line to the mouse position
    pygame.draw.circle(screen, BLUE, reference_coord, 5)
    pygame.draw.line(screen, BLUE, reference_coord, (mouse_x, mouse_y), 2)

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
