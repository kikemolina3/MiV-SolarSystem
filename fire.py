from fire_particle import FireParticle
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from texture import Texture

class Fire:
    def __init__(self):
        self.particles = []
        for i in range(300):
            self.particles.append(FireParticle())
        self.texture = 0
        self.loadParticleTexture()
    
    def drawSystem(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture.textureId)
        for i in self.particles:
            i.drawParticle()
        self.manageParticles()
        glDisable(GL_TEXTURE_2D)

    def manageParticles(self):
        for i in self.particles:
            if i.y > 1:
                self.particles.remove(i)
                self.particles.append(FireParticle())

    def loadParticleTexture(self):
        self.texture = Texture("flame.jpg")
        
    

