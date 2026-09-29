import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Rat-Chase")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

text_surface = pygame.Rect(0, 0, 200, 60)
text_surface.center = (WIDTH // 2, 600)

while running:
    screen.fill("White")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    pygame.display.flip()

    clock.tick(60) 

pygame.quit()