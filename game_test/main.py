#coding:utf-8
import pygame


def colors(color="darkBlue"):
	if color == "darkBlue":
		return (1,66,81)
	elif color == "blue":
		return (76,210,243)
	elif color == "green":
		return (30,241,36)
	elif color == "white":
		return (255,255,255)
	elif color == "black":
		return (0,0,0)

def creaTextObj(txt, police):
	txtSurface = police.render(txt, True, colors("white"))
	return txtSurface, txtSurface.get_rect()

def msg(text= "jeu par Aroun"):
	BigTxt = pygame.font.Font('data/BradBunR.ttf', 150)
	SmallTxt = pygame.font.Font('data/BradBunR.ttf', 30)

	BigTextSurf, BigTextRect = creaTextObj(text, BigTxt)
	BigTextRect.center = surfaceW/2, ((surfaceH/2) - 50)
	surface.blit(BigTextSurf, BigTextRect)
	
	smallTextSurf, smallTextRect = creaTextObj("Appuyer sur une touche", SmallTxt)
	smallTextRect.center = surfaceW/2, ((surfaceH/2) + 50)
	surface.blit(smallTextSurf, smallTextRect)

	smallTextSurf2, smallTextRect2 = creaTextObj("par Aroun Le BriCodeur", SmallTxt)
	smallTextRect2.center = surfaceW/2, ((surfaceH/2) + 75)
	surface.blit(smallTextSurf2, smallTextRect2)

	pygame.display.update()


def endGame():
	msg("Fin de partie.")

pygame.init()

surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66


surface = pygame.display.set_mode((surfaceW, surfaceH))
pygame.display.set_caption("Mcf-Stud'Games by Aroun Le BriCodeur")


img = pygame.image.load('data/Ballon01.png')

def ballon(px, py, pimg):
	surface.blit(pimg, (px, py))

def mainGame():
	x = 150
	y = 200
	move_y = 0
	game_over = False


	while not game_over:
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				game_over = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
					move_y = -1.5
			if event.type == pygame.KEYUP:
				move_y = 0.5

		y += move_y

		surface.fill(colors("blue"))
		ballon(x, y, img)

		if y > surfaceH - 40 or y < -10:
			endGame()

		pygame.display.update()

mainGame()
pygame.quit()
quit()