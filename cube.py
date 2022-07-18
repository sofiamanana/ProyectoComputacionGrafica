import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
#vertices de las pages
vertices = [[1,1],[1,-1],[-1,-1],[-1,1]]
#arcos entre las pages
edges = [[0,1],[1,2],[2,3],[3,0]]
vertices2 = [[1,1.5],[1,-1.5],[-1,-3.5],[-1,3.5]]
#arcos entre las pages
edges2 = [(0,1),(1,2),(2,3),(3,0)]

def sq(vertices, edges):
    glBegin(GL_LINES)
    
    for e in edges:
        for vertex in e:
            glVertex2fv(vertices[vertex])
    
    glEnd()

def norm(x, y):
    temp_y = y*(-1)
    x_norm = x - 250
    y_norm = temp_y + 250
    return x_norm/250, y_norm/250

def main():
    pg.init()
    display = (500,500)
    pg.display.set_mode(display, pg.DOUBLEBUF|pg.OPENGL|pg.RESIZABLE)
    gluPerspective(40,(display[0]/display[1]),1,10)
    glTranslatef(0.0,0.0,-5)
    glRotatef(0,0,1,1)

    while True:
        for event in pg.event.get():
            if (event.type == pg.quit):
                pg.quit()
                quit()

            if (event.type == pg.MOUSEBUTTONDOWN):
                vertices[0][0] += 1
            keys = pg.key.get_pressed()
            if(keys[K_w]):
                glTranslatef(0,0.5,0)
            if(keys[K_a]):
                glTranslatef(-0.5,0,0)
            if(keys[K_s]):
                glTranslatef(0,-0.5,0)
            if(keys[K_w]):
                glTranslatef(0.5,0,0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        sq(vertices,edges)
        sq(vertices2,edges2)
        pg.display.flip()
        pg.time.wait(10)

main()