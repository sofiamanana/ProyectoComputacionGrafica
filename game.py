import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
#vertices de las pages
vertices = ((1,1,1),(1,-1,1),(-1,-1,1),(-1,1,1),
            (1,1,-1),(1,-1,-1),(-1,-1,-1),(-1,1,-1))
#arcos entre las pages
edges = ((0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
        )

def sq():
    glBegin(GL_LINES)
    for e in edges:
        for vertex in e:
            glVertex2iv(vertices[vertex])
    glEnd()


class App:

    def __init__(self):
        pg.init()
        display = (500,500)
        pg.display.set_mode(display, pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0,0,-5,1)
        #gluPerspective(40,display[0]/display[1],1,10)
        #glTranslatef(0.0,0.0,-5)
        #glRotatef(45,1,0,0)
        self.mainLoop()

    def mainLoop(self):
        running = True
        while(running):
            for event in pg.event.get():
                if (event.type == pg.quit):
                    running = False
            #sq()
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()
            self.clock.tick(60)

    def quit(self):
        pg.quit()
    
if __name__ == '__main__':
    myApp = App()