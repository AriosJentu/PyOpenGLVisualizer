from PIL import Image
import numpy as np
from OpenGL.GL import *
from os import path

def MTL(filename, withtextures=True):

    contents = {}
    mtl = None

    fpath = "" 
    if filename.rfind("/") != -1:
        fpath = filename[:filename.rfind("/")+1]
    
    for line in open(filename, "r"):
    
        if line.startswith('#'): continue
    
        values = line.split()
        if not values: continue
    
        if values[0] == 'newmtl':
            mtl = contents[values[1]] = {}
    
        elif mtl is None:
            raise ValueError("mtl file doesn't start with newmtl stmt")
    
        elif values[0] == 'map_Kd':
    
            # load the texture referred to by this declaration
            mtl[values[0]] = values[1]

            if not path.isfile(mtl['map_Kd']):
                if path.isfile(fpath + mtl['map_Kd']):
                    mtl['map_Kd'] = fpath + mtl['map_Kd']

            if withtextures:

                surf = Image.open(mtl['map_Kd']).convert("RGBA")
                img = np.fromstring(surf.tobytes(), np.uint8)
                ix, iy = surf.size

                texid = mtl['texture_Kd'] = glGenTextures(1)
        
                glBindTexture(GL_TEXTURE_2D, texid)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                    GL_LINEAR)
        
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                    GL_LINEAR)

                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA,
                    GL_UNSIGNED_BYTE, img)

        else:
            mtl[values[0]] = tuple([float(i) for i in values[1:]])

    return contents

class OBJ:
    def __init__(self, filename, swapyz=False, withtextures=True):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        material = None

        path = "" 
        if filename.rfind("/") != -1:
            path = filename[:filename.rfind("/")+1]

        for line in open(filename, "r"):
        
            if line.startswith('#'): continue
        
            values = line.split()
            if not values: continue
        
            if values[0] == 'v':

                v = [float(i) for i in values[1:4]]
                # print(v)
            
                if swapyz:
                    v[1], v[2] = v[2], v[1]

                # print("Verticies", len(tuple(v)), tuple(v))
                self.vertices.append(tuple(v))
            
            elif values[0] == 'vn':

                v = [float(i) for i in values[1:4]]
                if swapyz:
                    v[1], v[2] = v[2], v[1]

                # print("Normals", len(tuple(v)), tuple(v))
                self.normals.append(tuple(v))
           
            elif values[0] == 'vt':

                v = [float(i) for i in values[1:3]]
                # print("Textures", len(tuple(v)), tuple(v))
                self.texcoords.append(tuple(v))
            
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            
            elif values[0] == 'mtllib':
                self.mtl = MTL(path+values[1], withtextures)
            
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))

                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    
                    else:
                        texcoords.append(0)
                    
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    
                    else:
                        norms.append(0)
                
                self.faces.append((face, norms, texcoords, material))

        self.gl_list = glGenLists(1)
        
        glNewList(self.gl_list, GL_COMPILE)
        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)

        self.generateList()

        glDisable(GL_TEXTURE_2D)
        glEndList()

    def generateList(self):

        for face in self.faces:
            vertices, normals, texture_coords, material = face

            mtl = self.mtl[material]

            if 'texture_Kd' in mtl:
                # use diffuse texmap
                glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
            
            else:
                # just use diffuse colour
                glColor(*mtl['Kd'])

            glBegin(GL_POLYGON)
            
            for i in range(len(vertices)):
                
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
            
                if texture_coords[i] > 0:
                    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
            
                glVertex3fv(self.vertices[vertices[i] - 1])
            
            glEnd()

    def draw(self):
        glCallList(self.gl_list)