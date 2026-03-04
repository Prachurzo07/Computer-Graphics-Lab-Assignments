#  Task 1


# from OpenGL.GL import *      
# from OpenGL.GLUT import *    
# from OpenGL.GLU import *     
# import math
# import random

# WINDOW_WIDTH, WINDOW_HEIGHT = 900, 900
 
# store = []
# droplets = 500
# move = 0
# rain_speed = 2 

# def create_rain(n):
#     global store
#     if n <= 0:
#         return

#     x = random.uniform(-900 / 2, 900 / 2)
#     y = random.uniform(0, 900 / 2)
#     speed = random.uniform(1, 4.5)
#     store.append([x, y, speed])

#     create_rain(n - 1)

# def convert_coordinate(x, y):

#     a = x - (WINDOW_WIDTH / 2)
#     b = (WINDOW_HEIGHT / 2) - y
#     return a, b

# def draw_grass():
#     glBegin(GL_TRIANGLES)
#     glColor3f(0.71,0.40,0.11)
#     glVertex2d(-450,190)
#     glColor3f(0.71,0.40,0.11)
#     glVertex2d(450,190)
#     glColor3f(0.71,0.40,0.11)
#     glVertex2d(450,-450)
#     glColor3f(0.71,0.40,0.11)
#     glVertex2d(-450,190)
#     glColor3f(0.71,0.40,0.11)
#     glVertex2d(-450,-450)
#     glColor3f(0.71,0.40,0.11)
#     glVertex2d(450,-450)
#     glEnd()



# def draw_roof():

#     glBegin(GL_TRIANGLES)
#     glColor3f(0.4, 0, 0.6)
#     glVertex2d(0,200)
#     glColor3f(0.4, 0, 0.6)
#     glVertex2d(200,80)
#     glColor3f(0.4, 0,0.6)
#     glVertex2d(-200, 80)
#     glEnd()

# def draw_tree():
#     glBegin(GL_TRIANGLES)
#     x1=-450
#     x2=-400
#     while x2<=450:
#          glColor3f(0.0,1.0,0.0)
#          y1=182
#          y2=60
#          glVertex2d(x1,y2)
#          glVertex2d(x2,y2)
#          mid=(x1+x2)/2
#          glColor3f(0.71,0.40,0.11)
#          glVertex2d(mid,y1)
#          x1=x2
#          x2+=50
#     glEnd()



# def draw_building():
#     glBegin(GL_TRIANGLES)
#     glColor3f(1.0,0.75,0.80)
#     glVertex2d(-180,80)
#     glColor3f(1.0,0.75,0.80)
#     glVertex2d(180,80)
#     glColor3f(1.0,0.75,0.80)
#     glVertex2d(180,-100)
#     glColor3f(1.0,0.75,0.80)
#     glVertex2d(-180,80)
#     glColor3f(1.0,0.75,0.80)
#     glVertex2d(-180,-100)
#     glColor3f(1.0,0.75,0.80)
#     glVertex2d(180,-100)
#     glEnd()

# def draw_door():
#     glBegin(GL_TRIANGLES)
#     glColor3f(0.4,0.0,0.6)
#     glVertex2d(-45,40)
#     glVertex2d(45,40)
#     glVertex2d(45,-100)
#     glVertex2d(45,-100)
#     glVertex2d(-45,-100)
#     glVertex2d(-45,40)
#     glEnd()

# def draw_doorknob():
#     glPointSize(9)
#     glBegin(GL_POINTS)
#     glColor3f(0.0, 0.0, 0.0)
#     glVertex2f(32,-30)
#     glEnd()

# def draw_window():
#     glBegin(GL_TRIANGLES)
#     glColor3f(0.4,0.0,0.6)
#     glVertex2d(80,40)
#     glVertex2d(150,40)
#     glVertex2d(150,-20)
#     glVertex2d(150,-20)
#     glVertex2d(80,-20)
#     glVertex2d(80,40)
#     glVertex2d(-80,40)
#     glVertex2d(-150,40)
#     glVertex2d(-150,-20)
#     glVertex2d(-150,-20)
#     glVertex2d(-80,-20)
#     glVertex2d(-80,40)
#     glEnd()

# def draw_window_grill():
#     glLineWidth(3)
#     glBegin(GL_LINES)
#     glColor3f(0.0, 0.0, 0.0)
#     glVertex2f(115,40)
#     glVertex2f(115,-20)
#     glVertex2f(80,10)
#     glVertex2f(150,10)  

#     glColor3f(0.0, 0.0, 0.0)
#     glVertex2f(-115,40)
#     glVertex2f(-115,-20)
#     glVertex2f(-80,10)
#     glVertex2f(-150,10)
#     glEnd()

# def draw_sky(r,g,b):
#     glBegin(GL_TRIANGLES)
#     glColor3f(r,g,b)
#     glVertex2d(-450,450)
#     glVertex2d(450,450)
#     glVertex2d(450,190)

#     glVertex2d(450,190)
#     glVertex2d(-450,190)
#     glVertex2d(-450,450)    
#     glEnd()

# r=0.0
# g=0.0
# b=0.0
# status="night"
# def keyboard_listener(key, x, y):
    
#     global r,g,b,status 
#     if key == b'd':  
#         status="day"
#     elif key == b'n':  
#         status="night" 


#     glutPostRedisplay()


# def draw_rain():
#     global store, move
#     glColor3f(0.6, 0.6, 0.8)
#     glLineWidth(1.5)
#     glBegin(GL_LINES)
#     l=len(store)
#     k=0
#     while k<l:
#         x, y, q=store[k]
#         glVertex2f(x, y)
#         glVertex2f(x + move, y - 15)
#         k+=1
#     glEnd()


# def special_key_listener(key, x, y):
#     global move
#     if key == GLUT_KEY_RIGHT:
#         move = min(move + 5, 20)
#     elif key == GLUT_KEY_LEFT:
#         move = max(move - 5, -20)
#     glutPostRedisplay()


  

# def setup_projection():

#     glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(-450, 450, -450, 450, 0, 1)
#     glMatrixMode(GL_MODELVIEW)

# def display():

#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
#     glLoadIdentity()
#     setup_projection()
#     draw_grass()
#     draw_tree()
#     draw_sky(r,g,b)
#     draw_roof()
#     draw_building()
#     draw_door()
#     draw_doorknob()
#     draw_window()
#     draw_window_grill()
#     draw_rain()
#     glutSwapBuffers()
    

# def animate():
#     global r,g,b,status,store,rain_speed
#     if status=="day" and r!=1.0 and g!=1.0 and b!=1.0:
#         if 0.14<r<0.16 or 0.25<r<0.27 or 0.29<r<0.31 or 0.43<r<0.45 or  0.51<r<0.53 or 0.57<r<0.59 or 0.71<r<0.73 or 0.86<r<0.88 :
#             r+=0.000027037
#             g+=0.000027037
#             b+=0.000027037
#         else:
#             r+=0.00037037
#             g+=0.00037037
#             b+=0.00037037
#     elif status=="night"  and r!=0.0 and g!=0.0 and b!=0.0:
#         if 0.14<r<0.16  or 0.29<r<0.31 or 0.43<r<0.45 or  0.51<r<0.53 or 0.57<r<0.59 or 0.71<r<0.73   or 0.86<r<0.88 :
#             r-=0.000027037
#             g-=0.000027037
#             b-=0.000027037
#         else:        
#             r-=0.00037037
#             g-=0.00037037
#             b-=0.00037037
#     l=len(store)
#     t=0
#     while t<l:
#         q=store[t]
#         q[1] -= q[2] * rain_speed
#         q[0]+=move*0.25
#         if q[1] < -900 / 2:
#             q[1] = 900 / 2
#         if q[0]>900/2:

#             q[0]=-900/2
#         elif q[0]<-900/2:
#             q[0]=900/2    
#         t+=1    
#     glutPostRedisplay()        


# def main():
#     glutInit()
#     glutInitDisplayMode(GLUT_RGBA)
#     glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
#     glutInitWindowPosition(100, 100)
#     glutCreateWindow(b"OpenGL Interactive Animation")

#     create_rain(droplets)
#     glutDisplayFunc(display)
#     glutIdleFunc(animate) 
#     glutKeyboardFunc(keyboard_listener)
#     glutSpecialFunc(special_key_listener) 

#     glutMainLoop() 



# if __name__ == "__main__":
#     main()






# Task 2

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time


WINDOW_WIDTH, WINDOW_HEIGHT = 900, 900 
BOUNDARY = 450 

store= [] 
global_speed = 1.5
point_size = 9 
game_state = 'move'
blink_state = 'dont_blink'

def convert_coordinate(x, y):
    a = x - (WINDOW_WIDTH / 2)
    b = (WINDOW_HEIGHT / 2) - y
    return a, b

def draw_point(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def keyboard_listener(key, x, y):
    global point_size, game_state    
    if key == b' ':
        if game_state == 'freeze':
            game_state = 'move'
        else:
            game_state='freeze'  
    if game_state == 'freeze':
        return        
    glutPostRedisplay()


def special_key_listener(key, x, y):
    global global_speed, blink_state   
    if game_state == 'freeze':
        return
    if key == GLUT_KEY_LEFT:
        if blink_state=="do_blink":
            blink_state = 'dont_blink' 
        else:
            blink_state='do_blink'            
    elif key == GLUT_KEY_UP:
        global_speed *= 1.2
    elif key == GLUT_KEY_DOWN:
        global_speed /= 1.2
        global_speed = max(0.01, global_speed)        
    glutPostRedisplay()


def mouse_listener(button, state, x, y):
    global store,game_state   
    if game_state == 'freeze':
        return        
    if state == GLUT_DOWN: 
        if button == GLUT_LEFT_BUTTON:
            pass
        elif button == GLUT_RIGHT_BUTTON:
            mouse_x, mouse_y = convert_coordinate(x, y)
            r=random.random()
            g=random.random()
            b = random.random()
            dx = random.choice([1, -1])
            dy = random.choice([1, -1])            
            point_info = (mouse_x, mouse_y, r, g, b, dx, dy)
            store.append(point_info)            
    glutPostRedisplay()

def draw_from_store(i,store,show_screen,point_size):
    if i==len(store):
        return
    info=store[i]
    x, y, r, g, b, p, q = info         
    if show_screen=="yes":
        glColor3f(r, g, b)  
    else:
        glColor3f(0.0, 0.0, 0.0)         
    draw_point(x, y, point_size) 
    draw_from_store(i+1,store,show_screen,point_size)

def setup_projection():

    glViewport(0, 0,900,900)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-BOUNDARY, BOUNDARY, -BOUNDARY, BOUNDARY, 0, 1)
    glMatrixMode(GL_MODELVIEW)

start_time=0.0

def show_ball():
    global blink_state,game_state,store,point_size,start_time
    current_time_in_ms=(time.time()-start_time)*1000
    show_screen="yes"
    if blink_state == 'do_blink' and game_state != 'freeze':
        if (current_time_in_ms // 500) % 2 != 0:
            show_screen="no"
    draw_from_store(0,store,show_screen,point_size)        
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    setup_projection()
    show_ball() 
    glutSwapBuffers()


def animate():
    global store,game_state
    if game_state == 'freeze':
        return
    nlist= []
    l=len(store)
    i=0
    while i<len(store):
        info=store[i]
        x, y, r, g, b, dx, dy = info        
        x_new = x + (dx * global_speed)
        y_new = y + (dy * global_speed)
        if x_new >= 450:
            x_new = 450  
            dx = -dx          
        elif x_new <= -450:
            x_new = -450 
            dx = -dx                      
        if y_new >= 450:
            y_new = 450
            dy = -dy
        elif y_new <= -450:
            y_new = -450
            dy = -dy
        new_info = (x_new, y_new, r, g, b, dx, dy)
        nlist.append(new_info)
        i+=1
    store = nlist
    glutPostRedisplay() 
def main():
    global start_time
    start_time= time.time()
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Amazing Box")

    glutDisplayFunc(display)
    glutIdleFunc(animate) 
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener) 
    glutMouseFunc(mouse_listener)
    glutMainLoop() 



if __name__ == "__main__":
    main()