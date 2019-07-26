import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import obj

def glSceneInitialize(objectdir, w, h, fov, fardistance):

	pygame.init()
	display = (w, h)
	window = pygame.display.set_mode(display, pygame.OPENGLBLIT)# | DOUBLEBUF | OPENGL)

	gluPerspective(fov, w/h, 0.1, fardistance)

	#Construct basic light for scene
	glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
	glLightfv(GL_LIGHT0, GL_AMBIENT, (0.1, 0.1, 0.1, 1.0))
	glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.05, 0.05, 0.05, 1.0))
	glEnable(GL_LIGHT0)
	glEnable(GL_LIGHTING)
	glEnable(GL_COLOR_MATERIAL)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	#Load object	
	myobj = obj.OBJ(objectdir, False)


	glMatrixMode(GL_MODELVIEW)
	glEnable(GL_DEPTH_TEST)

	return window, myobj

def setCameraLookAt(x, y, z, lx, ly, lz):
	gluLookAt(x, y, z, lx, ly, lz, 0, 1, 0) #0, 1, 0 - positive vertical oriented vector coordinates


def main():

	window, obj = glSceneInitialize("untitled.obj", 800, 600, 60, 50.0)

	setCameraLookAt(0, 0, 5, 0, 0, 0)

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	obj.draw()
	pygame.image.save(window, "test.png")

	pygame.display.flip()
	pygame.time.wait(5)


main()
pygame.quit()
quit()