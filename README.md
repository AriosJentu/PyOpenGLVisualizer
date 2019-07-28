# PyOpenGLVisualizer
Project for CATS, visualize user's 3D models, and compare with task's model 

## How to use
1. First of all, you need to create models. First - original model, which will be compared with another, user's model. Second - user model.
Recommend to use Blender 3D. Export models in *.obj* type.

2. You need to generate tests. Tests containing original object file location, width and height of render, camera position and coordinates where look at, boolean for rendering with or without textures, FOV, and Draw Distance
Original object location puts in file *header.txt*, another tests parameters puts in *test**K**.txt*, where **K** is index of test. Numeration starts from 1, and if next index not found, testing will be finished.

3. Run tester program using next syntax:  
`python tester.py USERMODELDIR REMOVEAFTER`  
where **USERMODELDIR** is location of user model (if it has material, *.mat* file need to be called same as *.obj*), and **REMOVEAFTER** is boolean value (0 or 1), which telling program that after execution test, remove render images.

## Header and test files syntax
1. Header's filename is `header.txt`.
Header file contains only original object location:  
```
filename.obj
```  
[Example](header.txt) (Here **ORIGMODEL** is just a comment)

2. Test's filename is `testK.txt`, where **K** is index of test. Starts from 1, and if file with **K+1** index doesn't exists, testing ends.
Test's file contains information about camera, render size and texture in next style:  
```
WIDTH HEIGHT CAMERA_X CAMERA_Y CAMERA_Z LOOKAT_X LOOKAT_Y LOOKAT_Z TEXTURED FOV DRAWDISTANCE
```  
Where  
- **WIDTH** and **HEIGHT** - render picture size,  
- **CAMERA_XYZ** - camera location in scene,  
- **LOOKAT_XYZ** - camera focus location, where camera looking at,  
- **TEXTURED** - can be 0 or 1, means render model with (1) or without (0) texture (*default 1*),  
- **FOV** - camera field of view (*default is 75*),  
- **DRAWDISTANCE** - distance of model visibility (*default - 60*)  

[Example 1](test1.txt), [Example 2](test2.txt), ...

## Requirements
- `OpenGL` - OpenGL library *(pip package - `PyOpenGL`, `PyOpenGL-accelerate`)*
- `glfw` - Library for visualization OpenGL (render) *(pip package - `glfw`)*
- `cv2` - Library for work with images in OpenGL and for comparing *(pip package - `opencv-python`)*
- `numpy` - NumPy *(pip package - `numpy`)*
- `PIL.Image` - Library for comparing images *(pip package - `Pillow`)*

