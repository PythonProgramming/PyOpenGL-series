import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )


colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )


def Cube():
    glBegin(GL_QUADS)
    
    for surface in surfaces:
        x = 0

        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
        
    glEnd()
    


    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0,0, -40)

    object_passed = False

    #glRotatef(25, 2, 1, 0)

    while not object_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-0.5,0,0)

                if event.key == pygame.K_UP:
                    glTranslatef(0,-1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,1,0)

##            if event.type == pygame.MOUSEBUTTONDOWN:
##                if event.button == 4:
##                    glTranslatef(0,0,1.0)
##
##                if event.button == 5:
##                    glTranslatef(0,0,-1.0)
                    
                    

        

        #glRotatef(1, 3, 1, 1)

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        #print(x)

        
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        
        if camera_z < -1:
            object_passed = True
        

                    
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glTranslatef(0,0,.50)
        
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

for x in range(10):
    main()
pygame.quit()
quit()


















