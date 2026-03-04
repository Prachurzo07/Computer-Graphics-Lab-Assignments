from OpenGL.GL import *      # Core OpenGL functions
from OpenGL.GLUT import *    # GLUT library for window and input handling
from OpenGL.GLU import *     # OpenGL Utility library
import math
import random 

WINDOW_WIDTH, WINDOW_HEIGHT = 800,800

cheat="off"

def convert_coordinate(x, y):
    a = x - (WINDOW_WIDTH / 2)
    b = (WINDOW_HEIGHT / 2) - y
    return a, b

def draw_point(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def findzone(dx,dy):
    zone=0
    if dx>0 and dy>0:
        if abs(dx)>abs(dy):
            zone=0
        else:
            zone=1
    elif dx>0 and dy<0:
        if abs(dx)>abs(dy):
            zone=7
        else:
            zone=6
    elif dx<0 and dy>0:
        if abs(dx)>abs(dy):
            zone=3
        else:
            zone=2
    elif dx<0 and dy<0:
        if abs(dx)>abs(dy):
            zone=4
        else:
            zone=5
    return zone            

def convert_to_zero(x,y,zone):
    a=0
    b=0
    if zone==1:
        a=y
        b=x
    elif zone==2:
        a=y
        b=-x
    elif zone==3:
        a=-x
        b=y
    elif zone==4:
        a=-x
        b=-y
    elif zone==5:
        a=-y
        b=-x
    elif zone==6:
        a=-y
        b=x
    elif zone==7:
        a=x
        b=-y
    new=(a,b)
    return new                            

def original(a,target):
    x,y=a
    p=0
    q=0
    if target==1:
        p,q=y,x
    elif target==2:
        p,q=-y,x
    elif target==3:
        p,q=-x,y
    elif target==4:
        p,q=-x,-y
    elif target==5:
        p,q=-y,-x
    elif target==6:
        p,q=y,-x
    elif target==7:
        p,q=x,-y
    zone=(p,q)
    return zone

def draw_line(store,point_size):
    l=len(store)
    i=0
    while i<l:
        present=store[i]
        x, y = present
        draw_point(x, y, point_size)
        i+=1   

def mpl(p,q):
    x1,y1=p
    x2,y2=q
    delx=x2-x1
    dely=y2-y1

    if delx == 0:
        pixel = []        
        if y1 > y2:
            y1, y2 = y2, y1        
        latest_y = y1
        while latest_y <= y2:
            pixel.append((x1,latest_y))
            latest_y += 1 
        draw_line(pixel, 3)
        return 
    original_zone=findzone(delx,dely)
    if original_zone!=0:
        nstart=convert_to_zero(x1,y1,original_zone)
        nend=convert_to_zero(x2,y2,original_zone)
        x1,y1=nstart
        x2,y2=nend
    dx=x2-x1
    dy=y2-y1
    dinit=(2*dy)-dx
    dNE=2*(dy-dx)
    dE= 2*dy
    pixel=[]
    while x1<=x2:
        if dinit>0:
            dinit+=dNE
            pixel.append((x1,y1))
            x1+=1
            y1+=1
        else:
            dinit+=dE
            pixel.append((x1,y1))
            x1+=1
            y1=y1
    pixel.append((x2,y2))
    if original_zone!=0:
        temp=[]
        l=len(pixel)
        i=0
        while i<l:
            present=pixel[i]
            zone=original(present,original_zone)
            temp.append(zone)
            i+=1
        pixel=temp
    draw_line(pixel,3)
red=1.0
green=1.0
blue=1.0

x1,y1,x2,y2,x3,y3,x4,y4=0,395,20,370,0,345,-20,370

def draw_diamond():
    global x1,y1,x2,y2,x3,y3,x4,y4,red,green,blue
    glColor3f(red,green,blue)
    a=(x1,y1)
    b=(x2,y2)
    c=(x2,y2)
    d=(x3,y3)
    e=(x3,y3)
    f=(x4,y4)
    g=(x4,y4)
    h=(x1,y1)
    mpl(a,b)
    mpl(c,d)
    mpl(e,f)
    mpl(g,h)


def draw_play():
    glColor3f(1.0,0.75,0.0)
    mpl((-32, 360), (12, 374)) 
    mpl((-32, 392), (12, 374))
    mpl((-32, 360), (-32, 392))

def draw_pause():
    glColor3f(1.0,0.75,0.0)
    mpl((12, 392), (12, 355)) 
    mpl((-12, 355), (-12, 392))


def restart_game():
    global x1,y1,x2,y2,x3,y3,x4,y4,speed,mode,score,red,green,blue,cred,cgreen,cblue,over,p1,p2,p3,p4,cheat
    red=1.0
    green=1.0
    blue=1.0
    mode="yes"
    x1,y1,x2,y2,x3,y3,x4,y4=0,395,20,370,0,345,-20,370
    p2=(-80,-370)
    p1=(80, -370)
    p4=(60, -400)
    p3=(-60, -400)

    cred=1
    cgreen=1
    cblue=1

    speed=1
    score=0
    over="no"
    cheat="off"
mode="yes"
def mouse_listener(button, state, x, y):
    global mode,over,score 
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
      m,n= convert_coordinate(x, y)
      if -380<=m<=-335 and 340<=n<=380:
          restart_game()
          print(f"Starting Over!")
      if 330<=m<=370 and 340<=n<=380:
          print(f"Goodbye! Score: {score}")
          glutLeaveMainLoop()    
      if over!="yes":   
        if mode=="yes":
            if -12<=m<=12 and 355<=n<=392:
                mode="no"
        elif mode=="no":
            if -32<=m<=12 and 360<=n<=392:
                mode="yes"        
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        pass

    glutPostRedisplay()


def show_state():
    global mode
    if mode=="yes":
        draw_pause()            
    elif mode=="no":
        draw_play()    

def arrow():
    glColor3f(0,1,1)
    mpl((-360, 380), (-380, 360))
    mpl((-360, 340), (-380, 360))
    mpl((-380, 360), (-335, 360)) 
    


def cross():
    glColor3f(1.0, 0.0, 0.0)
    mpl((330, 380), (370, 340))
    mpl((330, 340), (370, 380))



p2=(-80,-370)
p1=(80, -370)
p4=(60, -400)
p3=(-60, -400)

cred=1
cgreen=1
cblue=1

def draw_catcher():
    global p1,p2,p3,p4,cred,cgreen,cblue
    glColor3f(cred,cgreen,cblue)
    mpl(p2,p1)
    mpl(p2,p3)
    mpl(p3,p4)
    mpl(p4,p1)

def keyboard_listener(key, x, y):
    
    global p1,p2,p3,p4,x1, y1, x2, y2, x3, y3, x4, y4,cheat
    if key == b'c':
        if cheat=="on":
            cheat="off"
            print(f"Cheat mode is turned off")
        else:
            cheat="on"
            print(f"Cheat mode is turned on ")

    glutPostRedisplay()

def special_key_listener(key, x, y):
    global p1,p2,p3,p4,mode,over,cheat        
    if mode!="no" and over!="yes" and cheat=="off":
     if key == GLUT_KEY_LEFT:
        m=p2[0]
        if m-40>=-400:
            p1=(p1[0]-40,p1[1])
            p2=(p2[0]-40,p2[1])
            p3=(p3[0]-40,p3[1])
            p4=(p4[0]-40,p4[1])
                        
     elif key == GLUT_KEY_RIGHT:
        b=p1[0]
        if b+40<=400:
            p1=(p1[0]+40,p1[1])
            p2=(p2[0]+40,p2[1])
            p3=(p3[0]+40,p3[1])
            p4=(p4[0]+40,p4[1])            


    glutPostRedisplay()


# ===== Projection Setup =====
def setup_projection():
    """Defines a 2D orthographic coordinate system."""
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-400, 400, -400, 400, 0, 1)
    glMatrixMode(GL_MODELVIEW)



# ===== Display callback =====
def display():  #It is made by us and we will work in this function 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer depth buffer 
    glLoadIdentity()                                    # Reset transformations
    setup_projection()                                  # Set up coordinate system                           
    draw_diamond()     
    draw_catcher()   
    show_state()
    arrow()
    cross()
    glutSwapBuffers()                                   # Swap buffers (double buffering) it helps to show what we see on screen 



def collision_checker():
    global x1, y1, x2, y2, x3, y3, x4, y4 
    global p1, p2, p3, p4,catch  
    diamondright=max(x1,x2,x3,x4)
    diamondtop=max(y1,y2,y3,y4)
    diamondbottom=min(y1,y2,y3,y4)
    diamondleft=min(x1,x2,x3,x4)

    catcherright=max(p1[0],p2[0],p3[0],p4[0])
    catcherleft=min(p1[0],p2[0],p3[0],p4[0])
    catchertop=max(p1[1],p2[1],p3[1],p4[1])
    catcherbottom=min(p1[1],p2[1],p3[1],p4[1])

    if diamondleft<catcherright and diamondright>catcherleft and diamondbottom<catchertop and diamondtop>catcherbottom:
        catch="yes"
    else:
        catch="no"    
    return catch
speed=1
score=0
over="no"
def animate():
    global x1,y1,x2,y2,x3,y3,x4,y4,speed,mode,score,red,green,blue,cred,cgreen,cblue,over,cheat,p1,p2,p3,p4
    if mode=="no" or over=="yes":
        return 
    change=1*speed
    y1-=change
    y2-=change
    y3-=change
    y4-=change
    if cheat=="on":
        catcherchange=1.2*change
        if x2-40<p2[0]:
            p1=(p1[0]-catcherchange,p1[1])
            p2=(p2[0]-catcherchange,p2[1])
            p3=(p3[0]-catcherchange,p3[1])
            p4=(p4[0]-catcherchange,p4[1])
        elif x4+40>p1[0]:
            p1=(p1[0]+catcherchange,p1[1])
            p2=(p2[0]+catcherchange,p2[1])
            p3=(p3[0]+catcherchange,p3[1])
            p4=(p4[0]+catcherchange,p4[1])

    check=collision_checker()
    if check=="yes":
        score+=1
        print(f"Score: {score}")
        speed+=0.125
        options= [-370, -330, -290, -250, -210, -170, -130, -90, -50, -10,30, 70, 110, 150, 190, 230, 270, 310, 350]    
        changex=random.choice(options)
        x1, x2, x3, x4 = 0, 20, 0,-20
        x1+=changex
        x2+=changex
        x3+=changex
        x4+=changex
        y1=395
        y2=370
        y3=345
        y4=370
        red=random.uniform(0.0,1.0)
        green=random.uniform(0.0,1.0)
        blue=random.uniform(0.0,1.0)        
        if red==0.0 and green==0.0 and blue==0.0:
            red=random.uniform(0.0,1.0)
            green=random.uniform(0.0,1.0)
            blue=random.uniform(0.0,1.0)
    elif y4<=-400:
        cred=1.0
        cgreen=0.0
        cblue=0.0
        print(f"Game Over! Score: {score}")
        x1,y1,x2,y2,x3,y3,x4,y4 = 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000
        over="yes"
        cheat="off"


    draw_diamond()         
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA )
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(200, 100)
    glutCreateWindow(b"Diamond Catcher")
   # Register callback functions
    glutDisplayFunc(display)
    glutIdleFunc(animate) #all the activities that will happen during idle time 
    glutKeyboardFunc(keyboard_listener)  # Directs to keyboard so that we can do change using keyboard using keys which have ascii value 
    glutSpecialFunc(special_key_listener) # We can do changes using the keys of keyboard which doesnt have ascii value 
    glutMouseFunc(mouse_listener)

    glutMainLoop() 


# ===== Entry Point =====
if __name__ == "__main__":
    main()
