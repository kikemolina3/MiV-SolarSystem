from vertex4 import Vertex4
from OpenGL.GLU import *
import math
import numpy as np

class Camera:
    def __init__(self):
        self.pos = Vertex4(0.0, 40.0, 0.0, 1.0)
        self.forward = Vertex4(0.0, -1.0, 0.0, 0.0)
        self.up = Vertex4(0.0, 0.0, 1.0, 0.0)
        self.side = Vertex4(1.0, 0.0, 0.0, 0.0)
        self.asteroid = False
    
    def moveLeft(self, inc):
        self.pos = self.pos.add(self.side.normalize().mult(-inc))

    def moveRight(self, inc):
        self.pos = self.pos.add(self.side.normalize().mult(inc))

    def moveUp(self, inc):
        self.pos = self.pos.add(self.up.normalize().mult(inc))

    def moveDown(self, inc):
        self.pos = self.pos.add(self.up.normalize().mult(-inc))

    def moveForward(self, inc):
        self.pos = self.pos.add(self.forward.normalize().mult(inc))

    def moveBackward(self, inc):
        self.pos = self.pos.add(self.forward.normalize().mult(-inc))

    def roll(self, angle):
        up = self.rotate(angle, self.forward.get(0), self.forward.get(1), self.forward.get(2), self.up)
        for i in range(0 ,3):
            self.up.set(i, up[i])
        self.up.normalize()
        self.setSide()

    def yaw(self, angle):
        forward = self.rotate(angle, self.up.get(0), self.up.get(1), self.up.get(2), self.forward)
        for i in range(0 ,3):
            self.forward.set(i, forward[i])
        self.forward.normalize()
        self.setSide()

    def pitch(self, angle):
        forward = self.rotate(angle, self.side.get(0), self.side.get(1), self.side.get(2), self.forward)
        for i in range(0 ,3):
            self.forward.set(i, forward[i])
        self.forward.normalize()
        up = self.rotate(angle, self.side.get(0), self.side.get(1), self.side.get(2), self.up)
        for i in range(0 ,3):
            self.up.set(i, up[i])
        self.up.normalize()

    def rotate(self, angle, x, y, z, vector):
        angle = math.radians(angle)
        cos = math.cos(angle)
        sin = math.sin(angle)
        vector = np.array(vector.values)
        rot = np.array([[x*x*(1-cos)+cos, x*y*(1-cos)-z*sin, x*z*(1-cos)+y*sin, 0], [y*x*(1-cos)+z*sin, y*y*(1-cos)+cos, y*z*(1-cos)-x*sin, 0], [z*x*(1-cos)-y*sin, z*y*(1-cos)+x*sin, z*z*(1-cos)+cos, 0], [0,0,0,1]])
        result = rot.dot(vector)
        result = result.tolist()
        return result

    def setSide(self):
        forward = np.array([self.forward.get(0), self.forward.get(1), self.forward.get(2)])
        up = np.array([self.up.get(0), self.up.get(1), self.up.get(2)])
        side = np.cross(up, forward)
        side = side.tolist()
        for i in range(0, 3):
            self.side.set(i,side[i])

    def look(self):
        center = self.pos.add(self.forward)
        gluLookAt(self.pos.get(0), self.pos.get(1), self.pos.get(2), center.get(0), center.get(1), center.get(2), self.up.get(0), self.up.get(1), self.up.get(2))