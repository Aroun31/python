import pygame

pygame.init()

surfaceW = 800
surfaceH = 500

surface = pygame.display.set_mode((surfaceW, surfaceH))
pygame.display.set_caption("Vol petit ballon")



game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True

pygame.quit()
quit()