# Importing pg module
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *   

#vertices de las pages
vertices = [[1,1],[1,-1],[-1,-1],[-1,1]]
#arcos entre las pages
edges = ((0,1),(1,2),(2,3),(3,0))
def circle():
    posx, posy = 0,0    
    sides = 32    
    radius = 1    
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)

def main():
    pg.init()
    display = (500,500)
    pg.display.set_mode(display, pg.DOUBLEBUF|pg.OPENGL|pg.RESIZABLE)
    gluPerspective(40,(display[0]/display[1]),1,10)
    glTranslatef(0.0,0.0,-5.0)
    #glRotatef(0,0,1,1)

    while True:
        for event in pg.event.get():
            if (event.type == pg.quit):
                pg.quit()
                quit()
            
        #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        circle()
        pg.display.flip()
        pg.time.wait(10)

main()