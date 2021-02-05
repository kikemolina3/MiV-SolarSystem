from vertex4 import Vertex4
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.ARB.multitexture import *
from texture import Texture
from objloader import OBJ
from camera import Camera
from planet import Planet
from sun import Sun
from asteroid import Asteroid
from fire import Fire
import pywavefront
from pywavefront import visualization

WIDTH, HEIGHT = 1920, 1080 
refresh_mills = 15

light_amb_0 = [1.0, 1.0, 1.0]
light_pos_0 = [2.0, 0.0, 0.0, 1.0]

light_amb_1 = [0.2, 0.2, 0.2]
light_dif_1 = [0.3, 0.3, 0.3]
light_pos_1 = [29.625663771064346, 15.118880677888288, 15.281901561773827, 1.0]
light_dir_1 = [-0.5985750013959417, -0.6812986738691316, -0.4213550577459516]

def init_gl():
    global obj
    global cam
    global sun
    global mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
    global planets
    global asteroid
    global t
    global quad
    global ship

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glEnable(GL_LIGHTING)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_amb_0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos_0)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT1, GL_POSITION, light_pos_1)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, light_dir_1)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_amb_1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_dif_1)
    glEnable(GL_LIGHT1)

    obj = OBJ("cube.obj", textureFile="stars.jpg")
    obj.generate()

    cam = Camera()

    sun = Sun(textureFile="sun.jpg")

    mercury = Planet("mercury.jpg", 8, 5, 0.5, 0.1, 0.25)
    venus = Planet("venus.jpg", 9.6, 6, 0.4, 0.1, 0.35)
    earth = Planet("earth.jpg", 11.2, 7, 0.3, 0.1, 0.45, "moon.jpg", [0.7, 0.8, 0.09])
    mars = Planet("mars.jpg", 12.8, 8, 0.2, 0.1, 0.33)
    jupiter = Planet("jupiter.jpg", 19.2, 12, 0.2, 1, 1.5, "jupiter-moon.jpg", [3, 1, 0.3])
    saturn = Planet("saturn.jpg", 25.6, 16, 0.15, 0.2, 1.1)
    uranus = Planet("uranus.jpg", 30.4, 19, 0.11, 0.2, 0.8)
    neptune = Planet("neptune.jpg", 32.8, 20.5, 0.09, 0.2, 0.7)
    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    quad = gluNewQuadric()
    gluQuadricTexture(quad, GL_TRUE)

    asteroid = Asteroid(Fire())

    t = Texture("rings.jpg")

    ship = pywavefront.Wavefront('Apollo/apollo.obj')


def display_callback():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_TEXTURE_2D)

    if cam.asteroid is True:
        cam.forward = Vertex4(asteroid.ellipse.lastCoords[0], 0, asteroid.ellipse.lastCoords[1], 0.0)
        cam.up = Vertex4(0.0, 1.0, 0.0, 0.0)
        cam.setSide()
        cam.yaw(35)

    cam.look()
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos_0)

    for i in planets:
        i.draw()

    sun.render()

    asteroid.draw()

    obj.render()

    # SPACESHIP
    glPushMatrix()
    glTranslatef(25.0, 10.0, 12.5)
    glRotatef(55, 0.0, 1.0, 0.0)
    visualization.draw(ship)
    glPopMatrix()

    # SATURN RINGS
    glTranslatef(saturn.lastCoords[0], 0.0, saturn.lastCoords[1])
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(25, 1.0, 1.0, 0.0)
    glColor4f(1.0, 1.0, 1.0, 0.5)
    glScalef(0.2, 0.2, 0.2)
    glEnable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE)
    glBindTexture(GL_TEXTURE_2D, t.textureId)
    gluDisk(quad, 9, 14, 64, 1)
    glDisable(GL_BLEND)
    glEnable(GL_LIGHTING)
    glDisable(GL_TEXTURE_2D)

    # CONTROL KEYS LINES
    draw_text("CONTROL KEYS", 5, 190)
    draw_text("(a)->left, (s)->down, (d)->up, (w)->right", 5, 150)
    draw_text("(z)->zoom +, (x)->zoom -", 5, 110)
    draw_text("(1)->yaw left, (2)->yaw right, (3)->roll left, (4)->roll right, (5)->pitch down, (6)->pitch up", 5, 70)
    draw_text("(7)->top-bottom view, (8)->spaceship view, (9)->asteroid view", 5, 30)
    
    glutSwapBuffers()


def draw_text(string, x, y):
    glDisable(GL_LIGHTING)
    glMatrixMode(GL_PROJECTION)
    matrix = glGetDouble(GL_PROJECTION_MATRIX)
    glColor3f(1.0, 1.0, 1.0)
    glLoadIdentity()
    glOrtho(0.0, HEIGHT or 32, 0.0, WIDTH or 32, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2i(x, y)

    for character in string:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(character))
        
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glLoadMatrixd(matrix)

    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_LIGHTING)

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(refresh_mills, timer, 0)

def reshape_callback(width, height):
    
    if height == 0:
        height = 1
    aspect = width / height

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, aspect, 0.1, 150.0)


def keyboard_callback(key, x, y):
    key = key.decode("utf-8")

    # Camera keys
    if key == "a":
        cam.moveRight(0.2)
    elif key == "s":
        cam.moveDown(0.2)
    elif key == "d":
        cam.moveLeft(0.2)
    elif key == "w":
        cam.moveUp(0.2)
    elif key == "z":
        cam.moveForward(0.2)
    elif key == "x":
        cam.moveBackward(0.2)
    elif key == "1":
        cam.yaw(1)
    elif key == "2":
        cam.yaw(-1)
    elif key == "3":
        cam.roll(-1)
    elif key == "4":
        cam.roll(1)
    elif key == "5":
        cam.pitch(1)
    elif key == "6":
        cam.pitch(-1)
    elif key == "7":
        cam.asteroid = False
        cam.pos = Vertex4(0.0, 40.0, 0.0, 1.0)
        cam.forward = Vertex4(0.0, -1.0, 0.0, 0.0)
        cam.up = Vertex4(0.0, 0.0, 1.0, 0.0)
        cam.side = Vertex4(1.0, 0.0, 0.0, 0.0)
    elif key == "8":
        cam.asteroid = False
        cam.pos = Vertex4(29.625663771064346, 15.118880677888288, 15.281901561773827, 1.0)
        cam.forward = Vertex4(-0.5985750013959417, -0.6812986738691316, -0.4213550577459516, 0.0)
        cam.up = Vertex4(-0.5554190929671481, 0.7320023911966542, -0.3945657492105234, 0.0)
        cam.side = Vertex4(-0.5772500315041509, 0.002148549894103041, 0.8165646238124838, 0.0)
    elif key == "9":
        cam.asteroid = True
        cam.pos = Vertex4(13.0, 0.0, 8.0, 0.0)


if __name__ == "__main__":
    glutInit() 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)  
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Sun System") 
    glutDisplayFunc(display_callback) 
    glutReshapeFunc(reshape_callback)
    glutKeyboardFunc(keyboard_callback)
    init_gl()
    glutTimerFunc(0, timer, 0)
    glutMainLoop()
