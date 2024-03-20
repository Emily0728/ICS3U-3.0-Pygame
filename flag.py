"""
File: template.py
Author: Your Name
Date: 2024-03-20
Description: Template for basic Pygame graphics setup.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Program")

# Define colours
BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
RED = pygame.Color("red3")
BLUE = pygame.Color("royalblue4")
GREEN = pygame.Color("seagreen")

# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics - BEGIN YOUR PROGRAM HERE
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 200, 400))
    pygame.draw.rect(screen, WHITE, pygame.Rect(200, 0, 200, 400))
    pygame.draw.rect(screen, RED, pygame.Rect(400, 0, 200, 400))
    

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
