from texture import Texture
from ellipse import Ellipse
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Planet:
    def __init__(self, imageId, major_axis, minor_axis, speed, rot_speed, size, textureMoon=None, moonOrbitParams=None):
        self.texture = Texture(imageId)
        self.qobj = gluNewQuadric()
        gluQuadricTexture(self.qobj, GL_TRUE)
        self.ellipse = Ellipse(major_axis, minor_axis, speed)
        self.rotation = 0
        self.lastCoords = 0
        self.rot_speed = rot_speed
        self.size = size
        if(textureMoon is None):
            self.moon = False
        else:
            self.moon = True
            self.textureMoon = Texture(textureMoon)
            self.moonSize = moonOrbitParams[2]
            self.moonOrbit = Ellipse(moonOrbitParams[0], moonOrbitParams[0], moonOrbitParams[1])

    def draw(self):
        coords = self.ellipse.getCoords()
        glPushMatrix()
        glTranslatef(coords[0], 0.0, coords[1])
        self.lastCoords = coords
        if(self.moon):
            glPushMatrix()
            self.moonOrbit.render()
            coords = self.moonOrbit.getCoords()
            glTranslatef(coords[0], 0.0, coords[1])
            glScalef(self.moonSize, self.moonSize, self.moonSize)
            glBindTexture(GL_TEXTURE_2D, self.textureMoon.textureId)
            gluSphere(self.qobj, 1, 50, 50)
            glPopMatrix()
        glRotatef(270, 1.0, 0.0, 0.0)
        glRotatef(self.rotation, 0.0, 0.0, 1.0)
        glScalef(self.size, self.size, self.size)
        glBindTexture(GL_TEXTURE_2D, self.texture.textureId)
        gluSphere(self.qobj, 1, 50, 50)
        glPopMatrix()
        self.ellipse.render()
        self.rotation += self.rot_speed
