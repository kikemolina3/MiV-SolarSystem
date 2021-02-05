from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.ARB.multitexture import *
from PIL import Image

# TEXTURE CLASS
class Texture:
	def __init__(self, imageId):
		if type(imageId) is str:
			self.textureId = glGenTextures(1)

			image = Image.open("tex/" + imageId) 
			ix = image.size[0]
			iy = image.size[1]
			image = image.tobytes("raw", "RGBX", 0, -1)

			glBindTexture(GL_TEXTURE_2D, self.textureId)

			glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
			glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

		elif type(imageId) is list:
			self.textureId = glGenTextures(1)
			glBindTexture(GL_TEXTURE_CUBE_MAP, self.textureId)

			for i in range(0, 6):
				image = Image.open("tex/" + imageId[i]) 
				ix = image.size[0]
				iy = image.size[1]
				image = image.tobytes("raw", "RGBX", 0, -1)
				glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)



		
