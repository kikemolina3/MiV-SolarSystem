from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

class FireParticle:
    def __init__(self):
        self.x = random.random() * math.sin(random.random())
        self.y = 0
        self.z = random.random() * math.cos(random.random())
        self.speed = random.random() * 0.01
        self.rgb = [1.0, 0.0, 0.0]
        self.qobj = gluNewQuadric()
        gluQuadricTexture(self.qobj, GL_TRUE)
    
    def moveParticle(self):
        self.y += self.speed

    def drawParticle(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glScalef(0.02, 0.02, 0.02)
        glDisable(GL_LIGHTING)
        gluSphere(self.qobj, 1, 50, 50)
        glEnable(GL_LIGHTING)
        glPopMatrix()
        # glEnable(GL_TEXTURE_2D)
        self.moveParticle()

    def random(self, min, max):
        return random.random() % max + min
