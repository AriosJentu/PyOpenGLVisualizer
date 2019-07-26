import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import obj

def glSceneInitialize(objectdir, w, h, fov, fardistance):


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
	myobj = obj.OBJ("untitled.obj", False)

	glMatrixMode(GL_MODELVIEW)
	glEnable(GL_DEPTH_TEST)

	return myobj

def setCameraLookAt(x, y, z, lx, ly, lz):
	gluLookAt(x, y, z, lx, ly, lz, 0, 1, 0) #0, 1, 0 - positive vertical oriented vector coordinates

def main():

	pygame.init()
	display = (800, 600)
	window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

	window, obj = glSceneInitialize("untitled.obj", 800, 600, 60, 50.0)

	#KeyPress states for PyGame
	shift_pressed = False
	ctrl_pressed = False
	alt_pressed = False
	
	#Camera position controllers
	multiplicator = 0.5
	x_move = 0
	y_move = 0
	z_move = 0
	x_rot = 0
	y_rot = 0
	z_rot = 0

	setCameraLookAt(0, 0, 5, 0, 0, 0)

	k = 0
	while k == 0:
		k+= 1
	
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_LSHIFT:
					shift_pressed = True

				if event.key == pygame.K_LCTRL:
					ctrl_pressed = True	

				if event.key == pygame.K_LALT:
					alt_pressed = True	

				if event.key == pygame.K_LEFT:
					if shift_pressed:
						y_rot = 1
					else:
						x_move = 0.5

				if event.key == pygame.K_RIGHT:
					
					if shift_pressed:
						y_rot = -1
					else:
						x_move = -0.5

				if event.key == pygame.K_UP:
					if ctrl_pressed:
						z_move = 0.5
					elif shift_pressed:
						x_rot = 1
					else:
						y_move = -0.5

				if event.key == pygame.K_DOWN:
					if ctrl_pressed:
						z_move = -0.5
					elif shift_pressed:
						x_rot = -1
					else:
						y_move = 0.5

			elif event.type == pygame.KEYUP:
				
				if event.key == pygame.K_LSHIFT:
					shift_pressed = False

				if event.key == pygame.K_LCTRL:
					ctrl_pressed = False	

				if event.key == pygame.K_LALT:
					alt_pressed = False	

				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_move = 0
					y_rot = 0

				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					z_move = 0
					y_move = 0
					x_rot = 0


		mul = 1 if alt_pressed else multiplicator
		glTranslatef(x_move*mul, y_move*mul, z_move*mul)

		glRotatef(2*mul, x_rot, y_rot, z_rot);

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		obj.draw()
		pygame.image.save(window, "test.png")


		pygame.display.flip()
		pygame.time.wait(5)

if __name__ == "__main__":
	main()
	pygame.quit()
	quit()