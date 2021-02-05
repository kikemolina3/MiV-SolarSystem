import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Ellipse:
    def __init__(self, major_axis, minor_axis, speed):
        self.a = major_axis
        self.b = minor_axis
        self.speed = speed
        self.angle = 0
        self.gl_list = 0
        self.generateOrbit()
        self.lastCoords = []
    
    def getCoords(self):
        radians = math.radians(self.angle)
        x = math.cos(radians) * self.a
        z = math.sin(radians) * self.b
        self.angle += self.speed
        if (self.angle > 360):
            angle = 0
        self.lastCoords = [x, z]
        return [x, z]

    def generateOrbit(self):
        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glDisable(GL_LIGHTING)
        glDisable(GL_TEXTURE_2D)
        glLineWidth(0.2)
        glBegin(GL_LINE_LOOP)
        glColor4f(0.3, 0.3, 0.0, 1.0)
        for i in range(0, 360):
            radians = math.radians(i)
            i = math.cos(radians) * self.a
            j = math.sin(radians) * self.b
            glVertex3f(i, 0.0, j)
        glEnd()
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_LIGHTING)
        glEndList()
        
    def render(self):
        glCallList(self.gl_list)
