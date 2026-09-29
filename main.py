import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Rat-Chase")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    screen.fill("White")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    pygame.display.flip()

    clock.tick(60) 

pygame.quit()