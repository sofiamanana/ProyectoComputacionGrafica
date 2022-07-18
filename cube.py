import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
<<<<<<< HEAD
#vertices de las pages
vertices = [[1,1],[1,-1],[-1,-1],[-1,1]]
#arcos entre las pages
edges = [[0,1],[1,2],[2,3],[3,0]]
vertices2 = [[1,1.5],[1,-1.5],[-1,-3.5],[-1,3.5]]
#arcos entre las pages
edges2 = [(0,1),(1,2),(2,3),(3,0)]

=======
from math import *   
import numpy as np

vertices1 = [[1,1],[1,-1],[-1,-1],[-1,1]]
edges1 = ((0,1),(1,2),(2,3),(3,0))

vertices2 = [[1,3.5],[-1,3.5],[-1,1.5],[1,1.5]]
edges2 = ((0,1),(1,2),(2,3),(3,0))

vertices3 = [[1,-1.5],[-1,-1.5],[-1,-3.5],[1,-3.5]]
edges3 = ((0,1),(1,2),(2,3),(3,0))

vertices1 = np.array(vertices1,dtype=np.float32)
vertices2 = np.array(vertices2,dtype=np.float32)
vertices3 = np.array(vertices3,dtype=np.float32)

def circle():
    pos_x, pos_y = 1,1   
    sides = 24    
    radius = 0.5   
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + pos_x    
        sine  = radius * sin(i*2*pi/sides) + pos_y    
        glVertex2f(cosine,sine)

def norm(x, y):
    temp_y = y*(-1)
    x_norm = x - 250
    y_norm = temp_y + 250
    return x_norm/250, y_norm/250

>>>>>>> f208351d53b5c28506198421c7222928fa8eea1b
def sq(vertices, edges):
    glBegin(GL_LINES)
    glColor3f(133/255,68/255,194/255)
    for e in edges:
        for vertex in e:
            glVertex2fv(vertices[vertex])
    
    glEnd()

<<<<<<< HEAD
def norm(x, y):
    temp_y = y*(-1)
    x_norm = x - 250
    y_norm = temp_y + 250
    return x_norm/250, y_norm/250
=======
def move():
    new_x,new_y = pg.mouse.get_pos()
    new_x,new_y = norm(new_x,new_y)
    new_x -= 0.5
    new_y -= 0.5
    return new_x, new_y
>>>>>>> f208351d53b5c28506198421c7222928fa8eea1b

def main():
    pg.init()
    display = (500,500)
    pg.display.set_mode(display, pg.DOUBLEBUF|pg.OPENGL|pg.RESIZABLE)
    gluPerspective(40,(display[0]/display[1]),1,10)
    glTranslatef(0.0,0.0,-10.0)
    #glRotatef(0,0,1,1)

    while True:
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if (event.type == pg.quit):
                pg.quit()
                quit()
            x,y = pg.mouse.get_pos()
            x_norm,y_norm = norm(x,y)
            #Cuadrado 1
            #vertices2 = [[1,3.5],[-1,3.5],[-1,1.5],[1,1.5]]
            if keys[K_1] and keys[K_LEFT]:
                if keys[K_w]:
                    vertices2[1][1] += 0.1
                if keys[K_a]:
                    vertices2[1][0] -= 0.1
                if keys[K_s]:
                    vertices2[1][1] -= 0.1
                if keys[K_d]:
                    vertices2[1][0] += 0.1
            if keys[K_1] and keys[K_RIGHT]:
                if keys[K_w]:
                    vertices2[0][1] += 0.1
                if keys[K_s]:
                    vertices2[0][0] -= 0.1
                if keys[K_c]:
                    vertices2[0][1] -= 0.1
                if keys[K_d]:
                    vertices2[0][0] += 0.1
            if keys[K_1] and keys[K_DOWN]:
                if keys[K_w]:
                    vertices2[2][1] += 0.1
                if keys[K_s]:
                    vertices2[2][0] -= 0.1
                if keys[K_c]:
                    vertices2[2][1] -= 0.1
                if keys[K_d]:
                    vertices2[2][0] += 0.1
            if keys[K_1] and keys[K_UP]:
                if keys[K_w]:
                    vertices2[3][1] += 0.1
                if keys[K_a]:
                    vertices2[3][0] -= 0.1
                if keys[K_s]:
                    vertices2[3][1] -= 0.1
                if keys[K_d]:
                    vertices2[3][0] += 0.1
            #Cuadrado 2 
            if keys[K_2] and keys[K_LEFT]:
                if keys[K_q]:
                    vertices1[3][1] += 0.1
                if keys[K_a]:
                    vertices1[3][0] -= 0.1
                if keys[K_s]:
                    vertices1[3][1] -= 0.1
                if keys[K_d]:
                    vertices1[3][0] += 0.1
            if keys[K_2] and keys[K_RIGHT]:
                if keys[K_q]:
                    vertices1[0][1] += 0.1
                if keys[K_a]:
                    vertices1[0][0] -= 0.1
                if keys[K_c]:
                    vertices1[0][1] -= 0.1
                if keys[K_d]:
                    vertices1[0][0] += 0.1
            if keys[K_2] and keys[K_DOWN]:
                if keys[K_q]:
                    vertices1[2][1] += 0.1
                if keys[K_a]:
                    vertices1[2][0] -= 0.1
                if keys[K_c]:
                    vertices1[2][1] -= 0.1
                if keys[K_d]:
                    vertices1[2][0] += 0.1
            if keys[K_2] and keys[K_UP]:
                if keys[K_q]:
                    vertices1[1][1] += 0.1
                if keys[K_a]:
                    vertices1[1][0] -= 0.1
                if keys[K_s]:
                    vertices1[1][1] -= 0.1
                if keys[K_d]:
                    vertices1[1][0] += 0.1

            #Cuadrado 3 ----------------------------------------------------------
            if keys[K_3] and keys[K_LEFT]:
                if keys[K_w]:
                    vertices3[1][1] += 0.1
                if keys[K_a]:
                    vertices3[1][0] -= 0.1
                if keys[K_s]:
                    vertices3[1][1] -= 0.1
                if keys[K_d]:
                    vertices3[1][0] += 0.1
            if keys[K_3] and keys[K_RIGHT]:
                if keys[K_q]:
                    vertices3[0][1] += 0.1
                if keys[K_a]:
                    vertices3[0][0] -= 0.1
                if keys[K_s]:
                    vertices3[0][1] -= 0.1
                if keys[K_f]:
                    vertices3[0][0] += 0.1
            if keys[K_3] and keys[K_DOWN]:
                if keys[K_q]:
                    vertices3[2][1] += 0.1
                if keys[K_a]:
                    vertices3[2][0] -= 0.1
                if keys[K_s]:
                    vertices3[2][1] -= 0.1
                if keys[K_f]:
                    vertices3[2][0] += 0.1
            if keys[K_3] and keys[K_UP]:
                if keys[K_w]:
                    vertices3[3][1] += 0.1
                if keys[K_a]:
                    vertices3[3][0] -= 0.1
                if keys[K_s]:
                    vertices3[3][1] -= 0.1
                if keys[K_d]:
                    vertices3[3][0] += 0.1
            print(x_norm,y_norm)          
            

            #print(pg.mouse.get_pressed())
            #(1,2,3) -> true if is pressed

            print(pg.mouse.get_pos())
            
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
<<<<<<< HEAD
        sq(vertices,edges)
        sq(vertices2,edges2)
=======
        sq(vertices1,edges1)
        sq(vertices2,edges2)
        sq(vertices3,edges3)
>>>>>>> f208351d53b5c28506198421c7222928fa8eea1b
        pg.display.flip()
        pg.time.wait(10)

main()