import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Road to Washington")
clock = pygame.time.Clock()

running = True
color = (100,149,240)  # Define color outside the loop

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(color)  # Fill screen with yellow
    pygame.display.flip()  # Update the display

pygame.quit()