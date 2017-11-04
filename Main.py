from Shape import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
import math


DEBUG = True

DELAY = 0.01
point_matrix = []
point_matrix_old = []
shape = Shape()


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def input_matrix():
    global shape, point_matrix, point_matrix_old
    print('Enter the number of point: ')
    number_of_points = int(input())
    for i in range(number_of_points):
        shape.add_point(input())
        point_matrix = shape.get_point()
        point_matrix_old = shape.get_old_point()
    glutDisplayFunc(draw_plane)


def animate():
	for i in range(100):
		time.sleep(DELAY)
		glClear(GL_COLOR_BUFFER_BIT)
		draw_graph()
		glColor3f(33/255, 150/255, 243/255)
		glBegin(GL_POLYGON)
		tmp = []
		for j in range(shape.num_of_point):
			dX = (shape.point_matrix[j][0] - shape.point_matrix_old[j][0])/100
			dY = (shape.point_matrix[j][1] - shape.point_matrix_old[j][1])/100
			tmp.append([shape.point_matrix_old[j][0]+(i*dX), shape.point_matrix_old[j][1]+(i*dY)])
		for j in tmp:
			glVertex2f(j[0]/500, j[1]/500)
		glEnd()
		glFlush()


def animate_rotate(deg):
	for i in range(100):
		time.sleep(DELAY)
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(33/255, 150/255, 243/255)
		glBegin(GL_POLYGON)
		deg /= 100
		tmp = []
		for j in range(shape.num_of_point):
			dX = (shape.point_matrix[j][0] - shape.point_matrix_old[j][0])/100
			dY = (shape.point_matrix[j][1] - shape.point_matrix_old[j][1])/100
			tmp.append([shape.point_matrix_old[j][0]+(i*dX), shape.point_matrix_old[j][1]+(i*dY)])
		for j in tmp:
			glVertex2f(j[0]/500, j[1]/500)
		glEnd()
		glFlush()


def main_menu():
    print('Enter a task: ')
    input_parse = input().split()
    keyword = input_parse[0]

    global shape

    if keyword == 'input':
        input_matrix()

    elif keyword == 'translate':
        dx = float(input_parse[1])
        dy = float(input_parse[2])
        shape.translate(dx, dy)
        animate()

    elif keyword == 'dilate':
        zoom = float(input_parse[1])
        shape.dilate(zoom)
        animate()

    elif keyword == 'rotate':
        deg = float(input_parse[1])
        x = float(input_parse[2])
        y = float(input_parse[3])
        shape.rotate(deg, x, y)
        animate()

    elif keyword == 'reflect':
        param = input_parse[1]
        shape.reflect(param)
        animate()

    elif keyword == 'exit':
    	glutLeaveMainLoop()

    else :
    	print("Wrong input!")

    glutPostRedisplay()


def draw_graph():
    glColor3f(226/255, 226/255, 226/255)
    glLineWidth(0.01)
    glBegin(GL_LINES)
    for i in range(-24, 25):
        glVertex2f(i/25, 1.0)
        glVertex2f(i/25, -1.0)
        glVertex2f(1.0, i/25)
        glVertex2f(-1.0, i/25)
    glEnd()

    glColor3f(130/255, 130/255, 130/255)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    for i in range(-4, 5):
    	glVertex2f(i/5, 0.025)
    	glVertex2f(i/5,-0.025)
    	glVertex2f(0.025, i/5)
    	glVertex2f(-0.025, i/5)
    glEnd()

    glColor3f(130/255, 130/255, 130/255)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(-1.0, 0.0)
    glEnd()


def cartesian():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    draw_graph()
    glFlush()


def draw_plane():
    global point_matrix, point_matrix_old, shape
    DELAY = 0.001

    glClear(GL_COLOR_BUFFER_BIT)
    draw_graph()

    glColor3f(144/255, 202/255, 249/255)
    glBegin(GL_POLYGON)
    shape.print_point_old()
    for x in point_matrix_old:
        glVertex2f(x[0]/500, x[1]/500)
    glEnd()

    glColor3f(33/255, 150/255, 243/255)
    glBegin(GL_POLYGON)
    shape.print_point()
    for x in point_matrix:
        glVertex2f(x[0]/500, x[1]/500)

    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow('Tubes Algeo II')
    glutDisplayFunc(draw_plane)
    glutIdleFunc(main_menu)
    init()
    glutMainLoop()


main()
