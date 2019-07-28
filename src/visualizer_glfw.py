import cv2
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

import obj

def glSceneInitialize(objectdir, w, h, fov, fardistance, withtexture=True):

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
	myobj = obj.OBJ(objectdir, False, withtexture)

	glMatrixMode(GL_MODELVIEW)
	glEnable(GL_DEPTH_TEST)

	return myobj

def setCameraLookAt(x, z, y, lx, lz, ly):
	gluLookAt(x, y, z, lx, ly, lz, 0, -1, 0) #0, -1, 0 - inverse positive vertical oriented vector coordinates

def load(objectdir, outputdir, width, height, camerapos, cameralookat, withtexture=True, fov=75, fardistance=60):

	# Initialize the library
	if not glfw.init():
		return
	
	# Set window hint NOT visible
	glfw.window_hint(glfw.VISIBLE, False)

	# Create a windowed mode window and its OpenGL context
	window = glfw.create_window(width, height, "hidden window", None, None)
	if not window:
		glfw.terminate()
		return

	# Make the window's context current
	glfw.make_context_current(window)

	# Initialize object and camera
	myobj = glSceneInitialize(objectdir, width, height, fov, fardistance, withtexture)
	setCameraLookAt(*camerapos, *cameralookat)

	# Empty scene
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# Draw model
	myobj.draw()

	# Read image from GLFW window (RGBA)
	image_buffer = glReadPixels(0, 0, width, height, OpenGL.GL.GL_RGBA, OpenGL.GL.GL_UNSIGNED_BYTE)
	image = np.frombuffer(image_buffer, dtype=np.uint8).reshape(height, width, 4)

	# Save image
	cv2.imwrite(outputdir, image)

	# Drop window
	glfw.destroy_window(window)
	glfw.terminate()