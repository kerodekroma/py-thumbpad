import pygame

# Initialize Pygame
pygame.init()

# Screen size of iPhone 6s (750 x 1334)
screen_width, screen_height = 750/3, 1334/3
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Thumbpad Example")

# Thumbpad properties
thumbpad_center = (150, screen_height - 150)  # Bottom-left corner with margin
thumbpad_radius = 75  # Thumbpad size
active_radius = 125   # Active area size

# Colors
BACKGROUND_COLOR = (0, 0, 0)
THUMBPAD_COLOR = (100, 100, 255)
ACTIVE_COLOR = (100, 255, 100)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw active area
    pygame.draw.circle(screen, ACTIVE_COLOR, thumbpad_center, active_radius, 1)

    # Draw thumbpad
    pygame.draw.circle(screen, THUMBPAD_COLOR, thumbpad_center, thumbpad_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
