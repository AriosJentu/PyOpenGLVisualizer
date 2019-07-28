# PyOpenGLVisualizer
Project for CATS, visualize user's 3D models, and compare with task's model 

## How to use
1. First of all, you need to create models. First - original model, which will be compared with another, user's model. Second - user model.
Recommend to use [Blender 3D](https://www.blender.org/). Export models in *.obj* type (*.mat* will be created automatically, if it needs).

2. You need to generate tests. Tests containing original object file location, width and height of render, camera position and coordinates where look at, boolean for rendering with or without textures, FOV, and Draw Distance
Original object location puts in file *header.txt*, another tests parameters puts in *test**K**.txt*, where **K** is index of test. Numeration starts from 1, and if next index not found, testing will be finished.

3. Run tester program using next syntax:  
`./run USERMODELLOCATION REMOVEAFTER`  
where **USERMODELLOCATION** is location of user model (if it has material, *.mat* file need to be called same as *.obj*), and **REMOVEAFTER** is boolean value (0 or 1), which telling program that after execution test, remove render images *(default 1)*.  
By default, renders saving in `renders` directory.

## Header and test files syntax
This files all located in directory `tests`.
1. Header's filename is `header.txt`.
Header file containing only location of original object:  
```
location/filename.obj
```  
[Example](tests/header.txt) (Here **ORIGMODEL** is just a comment)

2. Test's filename is `testK.txt`, where **K** is index of test. Starts from 1, and if file with **K+1** index doesn't exists, testing ends.
Test's file containing information about camera, render size and texture in next style:  
```
WIDTH HEIGHT CAMERA_X CAMERA_Y CAMERA_Z LOOKAT_X LOOKAT_Y LOOKAT_Z TEXTURED FOV DRAWDISTANCE
```  
Where  
- **WIDTH** and **HEIGHT** - render picture size,  
- **CAMERA_XYZ** - camera location in scene,  
- **LOOKAT_XYZ** - camera focus location, where camera looking at,  
- **TEXTURED** - can be 0 or 1, means rendering model *with (1)* or *without (0)* texture (*default 1*),  
- **FOV** - camera field of view (*default is 75*),  
- **DRAWDISTANCE** - distance of model visibility (*default - 60*)  

### Note
**X**, **Y** and **Z** is not inversed like in OpenGL. **X** axis is horizontal axis *(from left to right)*, **Y** axis is perpendicular to monitor *(from **viewer** to **monitor**)*, and **Z** axis is vertical axis *(from bottom to top)*.

[Example 1](tests/test1.txt), [Example 2](tests/test2.txt), ...

## Requirements
- `OpenGL` - Standard OpenGL bindings for Python *(pip package - `PyOpenGL`, `PyOpenGL-accelerate`)*
- `glfw` - A ctypes-based wrapper for GLFW3 *(pip package - `glfw`)*
- `cv2` - Wrapper package for OpenCV python bindings *(pip package - `opencv-python`)*
- `numpy` - NumPy is the fundamental package for array computing with Python *(pip package - `numpy`)*
- `PIL.Image` - Python Imaging Library *(pip package - `Pillow`)*

All this packages can be installed with *pip* next way:
```
pip install PyOpenGL PyOpenGL-accelerate glfw opencv-python numpy Pillow
```
