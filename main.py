import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

text_font = pygame.font.Font("fonts/AldotheApache.ttf", 50)

square_surface = pygame.Surface((20,20))
square_surface.fill("aquamarine3")
text_surface = text_font.render("Jogo da Cobrinha", False, "aquamarine3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(square_surface, (200,100))
    screen.blit(text_surface, (230,20))
    
    pygame.display.update()
    clock.tick(60)