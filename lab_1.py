import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-0.5, 1.0, -0.5, 1.0)


upper_back_triangle = ((-0.016, 0.384), (-0.016, 0.832), (0.652, 0.384))
lower_back_triangle = ((-0.016, -0.016), (-0.016, 0.632), (0.652, -0.016))
upper_triangle = ((0.0, 0.4), (0, 0.8), (0.605, 0.4),)
lower_triangle = ((0.0, 0.0), (0.0, 0.59), (0.605, 0.0),)
circle_moon = ((0.15, 0.535))
circle_moon_upper = ((0.15, 0.53))
circle_sun = ((0.15, 0.19))


def upper_blue_triangle():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    for vertex in upper_back_triangle:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x, y)
    glEnd()


def lower_blue_triangle():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    for vertex in lower_back_triangle:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x, y)
    glEnd()


def upper_red_triangle():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    for vertex in upper_triangle:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x, y)
    glEnd()


def lower_red_triangle():
    glBegin(GL_TRIANGLES)
    for vertex in lower_triangle:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x, y)
    glEnd()


def lower_moon():
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(2)
    glBegin(GL_TRIANGLE_FAN)
    cx = circle_moon[0]
    cy = circle_moon[1]
    r = 0.08
    for i in range(180, 360):
        theta = 3.1415926 * float(i) / float(180)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f((x + cx), (y + cy))
    glEnd()


def upper_moon():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    cx = circle_moon_upper[0]
    cy = circle_moon_upper[1]
    r = 0.05
    for i in range(0, 360):
        theta = 3.1415926 * float(i) / float(360)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f((x + cx), (y + cy))
    glEnd()


def sun():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    cx = circle_sun[0]
    cy = circle_sun[1]
    r = 0.08
    for i in range(0, 360):
        theta = 2 * 3.1415926 * float(i) / float(360)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f((x + cx), (y + cy))
    glEnd()


def flag():
    glClear(GL_COLOR_BUFFER_BIT)
    upper_blue_triangle()
    lower_blue_triangle()
    upper_red_triangle()
    lower_red_triangle()
    upper_moon()
    lower_moon()
    sun()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(650, 650)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Nepal Flag")
    glutDisplayFunc(flag)
    clearScreen()
    glutMainLoop()


main()
