
import pygame
import random
import math

pygame.init()
dimensiones = (700, 500)
pantalla = pygame.display.set_mode(dimensiones)

NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)

pi = 3.141518
hecho = False
reloj = pygame.time.Clock()

fuente = pygame.font.Font(None, 25)
texto = fuente.render("Mi texto", True, NEGRO)

while not hecho:
	
	for accion in pygame.event.get():
		if accion.type == pygame.QUIT:
			print("El usuario solicitó salir.")
			hecho = True
		elif accion.type == pygame.KEYDOWN:
			print("El usuario presionó una tecla.")
		elif accion.type == pygame.KEYUP:
			print("El usuario soltó una tecla.")
		elif accion.type == pygame.MOUSEBUTTONDOWN:
			print("El usuario presionó un botón del ratón")

	#R= random.randint(0,255)
	#G = random.randint(0,255)
	#B = random.randint(0,255)
	#color = ( R , G , B )
	#pygame.draw.rect( pantalla , color , [ 10,10,random.randint(0,200),random.randint(0,100)] , 4 )
	#pygame.draw.line(pantalla, color, [100, 0], [100, 100], 5)

	
	desplazar_y = 0
	while  desplazar_y < 100:
		pygame.draw.line(pantalla, ROJO, [0, 10 + desplazar_y], [100, 110 + desplazar_y], 5)
		desplazar_y = desplazar_y + 30

	for i in range(200): 
		radianes_x = i / 20
		radianes_y = i / 6 
		x = int( 75 * math.sin(radianes_x)) + 200
		y = int( 75 * math.cos(radianes_y)) + 200
		pygame.draw.line(pantalla, NEGRO, [x, y], [x + 5, y], 5)
		pygame.draw.ellipse(pantalla, NEGRO, [20, 20, 250, 100], 2)
		pygame.draw.arc(pantalla, VERDE, [100, 100, 250, 200], pi/2, pi, 2)
		pygame.draw.polygon(pantalla, NEGRO, [[100, 100],[0, 200],[200, 200]], 5)

		pantalla.blit(texto, [350, 250])

	pygame.display.flip()
	pantalla.fill( (255,255,255) )
	reloj.tick(20)

pygame.quit()
