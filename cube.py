import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *   
#vertices de las pages
vertices = [[1,1],[1,-1],[-1,-1],[-1,1]]
pos_v = [[319,181],[319,319],[181,319],[181,181]]
#arcos entre las pages
edges = ((0,1),(1,2),(2,3),(3,0))

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

def sq():
    glBegin(GL_LINES)
    
    for e in edges:
        for vertex in e:
            glVertex2iv(vertices[vertex])
    
    glEnd()
def move():
    new_x,new_y = pg.mouse.get_pos()
    new_x,new_y = norm(new_x,new_y)
    new_x -= 0.5
    new_y -= 0.5
    return new_x, new_y

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
            x,y = pg.mouse.get_pos()
            x_norm,y_norm = norm(x,y)
            if (event.type == pg.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    if (-0.6 < x_norm < -0.5) and ( 0.5 < y_norm < 0.6):
                        new_x,new_y = move()
                        vertices[3] = [int(new_x), int(new_y)]
            print(x_norm,y_norm)
            keys = pg.key.get_pressed()
            if keys[K_w]:
                vertices[3][1] += 1
            if keys[K_a]:
                vertices[3][0] -= 1
            if keys[K_s]:
                vertices[3][1] -= 1
            if keys[K_d]:
                vertices[3][0] += 1

            #print(pg.mouse.get_pressed())
            #(1,2,3) -> true if is pressed





            '''
            if (event.type == pg.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    if (pg.mouse.get_pos()[0] == pos_v[3][0] or pg.mouse.get_pos()[0] == (pos_v[3][0]+1) or pg.mouse.get_pos()[0] == (pos_v[3][0]+2)):
                        vertices[3][0] -= 1
                        pos_v[3][0] -= 181
                    if (pg.mouse.get_pos()[0] == pos_v[0][0] or pg.mouse.get_pos()[0] == (pos_v[0][0]+1) or pg.mouse.get_pos()[0] == (pos_v[0][0]+2)):
                        vertices[0][0] += 1
                        pos_v[0][0] += 181
                    if (pg.mouse.get_pos()[1] == pos_v[1][0] or pg.mouse.get_pos()[1] == (pos_v[1][0]+1) or pg.mouse.get_pos()[1] == (pos_v[1][0]+2)):
                        vertices[1][0] -= 1
                        pos_v[1][0] -= 181
                    if (pg.mouse.get_pos()[1] == pos_v[2][0] or pg.mouse.get_pos()[0] == (pos_v[2][0]+1) or pg.mouse.get_pos()[0] == (pos_v[2][0]+2)):
                        vertices[2][0] += 1
                        pos_v[2][0] += 181
            if (event.type == pg.MOUSEBUTTONUP):
                if (event.button == 3):
                    if (pg.mouse.get_pos()[0] == pos_v[3][0] or pg.mouse.get_pos()[0] == (pos_v[3][0]+1) or pg.mouse.get_pos()[0] == (pos_v[3][0]+2)):
                        vertices[3][0] += 1
                        pos_v[3][0] += 181
                    if (pg.mouse.get_pos()[0] == pos_v[0][0] or pg.mouse.get_pos()[0] == (pos_v[0][0]+1) or pg.mouse.get_pos()[0] == (pos_v[0][0]+2)):
                        vertices[0][0] -= 1
                        pos_v[0][0] -= 181
                    if (pg.mouse.get_pos()[1] == pos_v[1][0] or pg.mouse.get_pos()[1] == (pos_v[1][0]+1) or pg.mouse.get_pos()[1] == (pos_v[1][0]+2)):
                        vertices[1][0] += 1
                        pos_v[1][0] += 181
                    if (pg.mouse.get_pos()[1] == pos_v[2][0] or pg.mouse.get_pos()[0] == (pos_v[2][0]+1) or pg.mouse.get_pos()[0] == (pos_v[2][0]+2)):
                        vertices[2][0] -= 1
                        pos_v[2][0] -= 181
            '''
            print(pg.mouse.get_pos())
            
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #circle()
        sq()
        pg.display.flip()
        pg.time.wait(10)

main()