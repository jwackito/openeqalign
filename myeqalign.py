import pygame
import pygame.camera
import sys

pygame.init()
pygame.camera.init()
size = (800,600)
(w, h) = size
screen = pygame.display.set_mode((w, h))
s =  pygame.Surface((w, h), depth=24)
crossair = pygame.image.load("crossair.png")
crossrect = crossair.get_rect()
crossrect = crossrect.move((w/2)-150,(h/2)-150 )
c = pygame.camera.Camera('/dev/video0', size)
c.start()
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			c.stop()
			sys.exit()
	s1 = c.get_image()
	screen.blit(s1, (0,0))
	screen.blit(crossair, crossrect)
	pygame.display.flip()



