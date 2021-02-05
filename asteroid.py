from ellipse import Ellipse
from objloader import OBJ
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

class Asteroid:
    def __init__(self, fire):
        self.asteroid = OBJ("asteroid.obj", textureFile="asteroid.jpg")
        self.ellipse = Ellipse(18, 4, 0.17)
        self.fire = fire
        self.angle = 0

    def draw(self):
        coords = self.ellipse.getCoords()
        glPushMatrix()
        glTranslatef(13.0, 0.0, 8.0)
        glRotatef(35, 0.0, 1.0, 0.0)
        self.ellipse.render()
        glTranslatef(coords[0], 0, coords[1]-0.35)
        glPushMatrix()
        glScalef(0.0006, 0.0006, 0.0006)
        self.asteroid.render()
        glPopMatrix()
        glRotatef(90, 0, 0, 1)
        glRotatef(90*math.sin(math.radians(self.angle)), 1.0, 0.0, 0.0)
        self.fire.drawSystem()
        glPopMatrix()
        self.angle += 0.17

    