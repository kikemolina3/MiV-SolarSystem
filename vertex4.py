import math

class Vertex4:
    def __init__(self, x, y, z, w):
        self.values = [x, y, z, w]

    def get(self, index):
        return self.values[index]

    def set(self, index, value):
        self.values[index] = value
    
    def module(self):
        length = 0.0
        for i in range(0, 4):
            length += self.values[i] * self.values[i]
        return math.sqrt(length)

    def normalize(self):
        l = self.module()
        if (l == 0):
            return self
        else:
            return Vertex4(self.values[0] / l, self.values[1] / l, self.values[2] / l, self.values[3] / l)

    def add(self, vertex):
        v = Vertex4(0, 0, 0, 0)
        for i in range(0, 4):
            v.set(i, self.values[i] + vertex.values[i])
        return v
    
    def mult(self, d):
        v = Vertex4(0, 0, 0, 0)
        for i in range(0, 4):
            v.set(i, self.values[i] * d)
        return v

    def __str__(self):
        return str(self.values[0]) + ", " + str(self.values[1]) + ", " + str(self.values[2]) + ", " + str(self.values[3])

    

