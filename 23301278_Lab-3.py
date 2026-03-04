from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time 
import random 



camera_pos = (0,500,500)
fovY = 120  
player_rotation=0
game_score=0
enemy_count=5
player_life=5
enemy_info={}
bullets={}
bullet_counter=0
bullet_velocity=8
bullets_missed=0
enemy_info={}
enemy_velocity=0.5
next_enemy=0
game_state="play"
cheat_mode="off"
v_press="off"
last_fire_time = 0.0
fire_delay = 0.1


def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    gluOrtho2D(0, 1000, 0, 800)  
    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))    
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def game_board(i, j, tiles_amount, x1, y1):    
    if i >= tiles_amount:
        return
    if j < tiles_amount:        
        if i % 2 == 0:
            if j % 2 == 0:
                glColor3f(1.0, 1.0, 1.0)
            else:
                glColor3f(0.7, 0.5, 0.95)
        else:
            if j % 2 == 0:
                glColor3f(0.7, 0.5, 0.95)
            else:
                glColor3f(1.0, 1.0, 1.0)
        x1 = x1
        y1 = y1
        x2 = x1 + 100
        y2 = y1 + 100

        glVertex3f(x1, y1, 0)
        glVertex3f(x2, y1, 0)
        glVertex3f(x2, y2, 0)
        glVertex3f(x1, y2, 0)

        game_board(i, j + 1, tiles_amount, x1 + 100, y1)

    else:
        game_board(i + 1, 0, tiles_amount, -700.0, y1 + 100)


def draw_floor():
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1) 
    glVertex3f(-700,700, 0)
    glVertex3f(700,700, 0)
    glVertex3f(700, -700, 0)   
    glVertex3f(-700, -700, 0)
    glEnd()
    tiles_amount = 14
    glBegin(GL_QUADS)
    game_board(0, 0, tiles_amount,-700,-700)
    glEnd()


def draw_boundary():
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-708,-700,80)
    glVertex3f(708,-700,80)
    glVertex3f(700, -700, 0)   
    glVertex3f(-700, -700, 0)
    glEnd()

    glBegin(GL_QUADS)   
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-708,-700,80)
    glVertex3f(-708,700,80)
    glVertex3f(-700, 700, 0)   
    glVertex3f(-700, -700, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1)
    glVertex3f(708,-700,80)
    glVertex3f(700,-700,0)
    glVertex3f(700, 700, 0)   
    glVertex3f(708, 700, 80)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,1.0)
    glVertex3f(700,700,0)
    glVertex3f(708,700,80)
    glVertex3f(-708, 700, 80)   
    glVertex3f(-700, 700, 0)
    glEnd()

player_x=0
player_y=0

def draw_torso():

    glPushMatrix()    
    glScalef(2,1,4)
    glTranslatef(0,0,0)
    glColor3f(0.4, 0.5, 0.0) 
    glTranslatef(0, 0,5)
    glutSolidCube(20) 
    glPopMatrix()

def draw_left_leg():

    glPushMatrix()
    glColor3f(0.0, 0.0, 1.0)
    glTranslatef(-20, 0,8) 
    glRotatef(180,1,0,0)
    gluCylinder(gluNewQuadric(), 14, 8,90, 10, 10)
    glPopMatrix()


def draw_right_leg():

    glPushMatrix()
    glColor3f(0.0, 0.0, 1.0) 
    glTranslatef(20, 0,8) 
    glRotatef(180, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 14, 8,90, 10, 10)
    glPopMatrix()    


def draw_head():

    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0) 
    glTranslatef(0, 0,80) 
    gluSphere(gluNewQuadric(),20, 100, 100)
    glPopMatrix()


def draw_left_hand():

    glPushMatrix()
    glColor3f(1.0, 0.7, 0.6) 
    glTranslatef(-25, 0,50)
    glRotatef(-90, 1, 0,0) 
    gluCylinder(gluNewQuadric(), 12, 5,60, 10, 10)
    glPopMatrix()


def draw_right_hand():

    glPushMatrix()
    glColor3f(1.0, 0.7, 0.6)
    glTranslatef(25,0,50)
    glRotatef(-90,1, 0, 0) 
    gluCylinder(gluNewQuadric(), 12, 5,60, 10, 10)
    glPopMatrix()


def draw_weapon():

    glPushMatrix()
    glColor3f(0.6,0.6,0.6)
    glTranslatef(0,0,34)
    glRotatef(-90,1, 0, 0) 
    gluCylinder(gluNewQuadric(), 10, 5,100, 10, 10)
    glPopMatrix()


def draw_player():

    global player_x, player_y,player_rotation
    glPushMatrix()

    glTranslatef(player_x,player_y,0)
    glRotatef(player_rotation, 0, 0, 1)
    draw_torso()
    draw_left_leg()
    draw_right_leg()
    draw_head()
    draw_left_hand()
    draw_right_hand()
    draw_weapon()

    glPopMatrix()


def draw_enemy_body():
    glPushMatrix() 
    glColor3f(1.0,0.0,0.0)
    gluSphere(gluNewQuadric(),36, 100, 100)
    glPopMatrix()

def draw_enemy_head():
    glPushMatrix()
    glTranslatef(0.0,0.0,35)
    glColor3f(0.0,0.0,0.0)
    gluSphere(gluNewQuadric(),20, 100, 100)
    glPopMatrix()        

def draw_enemy():

    glPushMatrix() 
    draw_enemy_body()
    draw_enemy_head()    
    glPopMatrix()


def draw_bullet():
    global bullets,bullets_missed
    
    for whole in bullets.items():
        key,value=whole
        x_pos,y_pos,delx,dely=value
        glPushMatrix()
        glTranslate(x_pos,y_pos,34)
        glColor3f(1.0,0.0,0.0)
        glutSolidCube(12)
        glPopMatrix()


def draw_lying_player():
 
    glPushMatrix()
    glRotatef(90,1, 0, 0) 
    draw_torso()
    draw_left_leg()
    draw_right_leg()
    draw_head()
    draw_left_hand()
    draw_right_hand()
    draw_weapon()
    glPopMatrix()


def manual(y, x):
    if x == 0 and y == 0: return 0.0
    if x == 0:
        return math.pi / 2 if y > 0 else -math.pi / 2    
    reference_angle = math.atan(y / x)    
    if x > 0:
        return reference_angle
    elif y >= 0:
        return reference_angle + math.pi 
    else: 
        return reference_angle - math.pi 


def restart_game():
    global pov,v_press,player_x,player_y,camera_pos,fovY,player_rotation,game_score,enemy_count,player_life,enemy_info,bullets,bullet_counter,bullet_velocity,bullets_missed,enemy_velocity,next_enemy,game_state,cheat_mode,last_fire_time,fire_delay

    camera_pos = (0,500,500)
    fovY = 120  
    player_rotation=0
    game_score=0
    enemy_count=5
    player_life=5
    enemy_info={}
    bullets={}
    bullet_counter=0
    bullet_velocity=8
    bullets_missed=0
    enemy_velocity=0.5
    next_enemy=0
    game_state="play"
    cheat_mode="off"
    last_fire_time = 0.0
    fire_delay = 0.1
    player_x=0
    player_y=0       
    v_press="off"
    pov="tpp"





def keyboardListener(key, x, y):
    global player_x, player_y, player_rotation,cheat_mode,game_state,v_press,pov
    
    a=player_x
    b=player_y
    speed=8

    direction = player_rotation
    resultant=(a*a+b*b)**0.5 
        
    if key == b'w':  
        dx = speed * math.sin(math.radians(-direction)) 
        dy = speed * math.cos(math.radians(-direction))        
        player_x += dx
        if player_x > 700:
            player_x = 700
        elif player_x < -700:
            player_x = -700
        player_y += dy
        if player_y > 700:
            player_y = 700
        elif player_y < -700:
            player_y = -700            
    if key == b's':
        dx = speed * math.sin(math.radians(-direction)) 
        dy = speed * math.cos(math.radians(-direction))
        player_x -= dx 
        if player_x > 700:
            player_x = 700
        elif player_x < -700:
            player_x = -700            
        player_y -= dy 
        if player_y > 700:
            player_y = 700
        elif player_y < -700:
            player_y = -700
    if cheat_mode=="off":
        if key==b"d":
            player_rotation-=8
        if key==b"a":
            player_rotation+=8
    if key==b"c":
        if cheat_mode=="off":
            cheat_mode="on"
        elif cheat_mode=="on":
            cheat_mode="off"
    if key==b"r" and game_state=="over":
        restart_game()       
    if key==b"v" and cheat_mode=="on" and pov=="fpp":
        if v_press=="on":
            v_press="off"
        elif v_press=="off":
            v_press="on"

    glutPostRedisplay()




def manual(y, x):
    if x == 0 and y == 0: return 0.0
    if x == 0:
        return math.pi / 2 if y > 0 else -math.pi / 2    
    reference_angle = math.atan(y / x)    
    if x > 0:
        return reference_angle
    elif y >= 0:
        return reference_angle + math.pi 
    else: 
        return reference_angle - math.pi 





def handlecamera(key, x, y):
    global camera_pos
    x, y, z = camera_pos
    if key == GLUT_KEY_UP:
        if y>0:
            y+=2
        elif y<0:
            y-=2
        z+=3    
    if key == GLUT_KEY_DOWN:
        if y>0:
            y-=2
        elif y<0:
            y+=2
        z-=3    
    resultant= (x*x+y*y)**0.5 
    direction = manual(y, x)        
    if key == GLUT_KEY_LEFT:
        direction -= math.radians(1.3)        
    if key == GLUT_KEY_RIGHT:
        direction += math.radians(1.3)
    x = resultant * math.cos(direction)
    y = resultant * math.sin(direction)
    if z<10:
        z=10
    if z>800:
        z=800 
    if y>600:
        y=600       
    camera_pos = (x, y, z)
    glutPostRedisplay()





def machine_gun(gun,fire,gang):
    machine_x,machine_y=gun
    a=0
    for j in len(gang):
        a+=1
    return a        





pov="tpp"
def mouseListener(button, state, x, y):
    global camera_pos, pov,bullets,bullet_counter,bullet_velocity,player_x,player_y

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if pov == "tpp":
            pov = "fpp"            
        else:
            camera_pos = (0, 500, 500)  
            pov = "tpp"
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        bullet_counter+=1
        direction=math.radians(-player_rotation)
        delx=bullet_velocity*math.sin(direction)
        dely=bullet_velocity*math.cos(direction)
        bullets[bullet_counter]=(player_x,player_y,delx,dely)

    glutPostRedisplay()


def setup_camera():
    global player_x, player_y, player_rotation, camera_pos, pov,cheat_mode,v_press,x,y,z,looking_x,looking_y,looking_z,fwd_x,fwd_y

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 2000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if pov == "tpp":
        x, y, z = camera_pos
        gluLookAt(x, y, z,
                  0, 0, 0,
                  0, 0, 1)
    elif cheat_mode=="off" or v_press=="off":
        angle = math.radians(player_rotation)
        fwd_x = -math.sin(angle)   
        fwd_y = math.cos(angle)   
        behind = 6.0   
        height  = 110.0   
        x = player_x - fwd_x * behind
        y = player_y + fwd_y * behind
        z = height
        looking_x = x + fwd_x * 10
        looking_y = y + fwd_y * 10
        looking_z = z
        gluLookAt(x,y,z,
                  looking_x, looking_y, looking_z,
                  0, 0, 1)

    elif cheat_mode=="on" and v_press=="on":
        behind=6.0
        height=110.0
        x = player_x - fwd_x * behind
        y = player_y + fwd_y * behind
        z = height
        looking_x = x + fwd_x * 10
        looking_y = y + fwd_y * 10
        looking_z = z
        gluLookAt(x,y,z,
                  looking_x, looking_y, looking_z,
                  0, 0, 1) 




def check_collision(p,rp,e,re):
    px,py,pz=p 
    ex,ey,ez=e
    dist=(px-ex)**2+(py-ey)**2
    radi=(rp+re)**2
    return dist<=radi

def hit_enemy(b,rb,e,re):
    bx,by,bz=b
    ex,ey,ez=e
    dist=(bx-ex)**2+(by-ey)**2
    radi=(rb+re)**2
    return dist<=radi

def outside_boundary(x,y):

    if x>700 or x<-700 or y>700 or y<-700:
        return True


def render_bullet():
    global bullets,bullets_missed,enemy_info,game_score
    remove_bullet=[]
    remove_enemy=[]
    for total in bullets.items():
        key,value=total
        x_pos,y_pos,delx,dely=value
        x_pos+=delx
        y_pos+=dely
        if outside_boundary(x_pos,y_pos):
            remove_bullet.append(key)
            bullets_missed+=1
        else:
            bullets[key]=(x_pos,y_pos,delx,dely)

        for enemy in enemy_info.items():
            index,villain=enemy
            ex,ey,ez=villain["pos"]
            if hit_enemy((x_pos,y_pos,0),10,villain["pos"],46):
                game_score+=1
                remove_enemy.append(index)
                remove_bullet.append(key)
    new_bullets={}            
    for k in bullets.keys():
        if k not in remove_bullet:
            new_bullets[k]=bullets[k]

    bullets=new_bullets

    new_enemy={}
    for j in enemy_info.keys():
        if j not in remove_enemy:
            new_enemy[j]=enemy_info[j]

    enemy_info=new_enemy
    render_enemy()        
    glutPostRedisplay()


def render_enemy():
    global enemy_info,next_enemy,enemy_count,player_x,player_y
    min=400
    while len(enemy_info)<enemy_count:

        while True:
            x_pos=random.randint(-664,664)
            y_pos=random.randint(-664,664)
            dist=((x_pos-player_x)**2+(y_pos-player_y)**2)**0.5
            if dist >=min:
                break      

        enemy_info[next_enemy]={"pos":(x_pos,y_pos,0),"last_pulse_time":time.time()+random.uniform(0,math.pi)}
        next_enemy+=1


def generate_enemy():

    global enemy_info

    present_time=time.time()
    for full in enemy_info.items():
        key,value=full
        x,y,z=value["pos"]
        last_time=value["last_pulse_time"]

        diff=present_time-last_time
        sc=1.0+0.2*math.sin(diff*4)
        glPushMatrix()
        glTranslate(x,y,z)
        glScale(sc,sc,sc)
        draw_enemy()
        glPopMatrix()


def player_enemy_interaction():
    global enemy_info,player_x,player_y,player_life
    p=(player_x,player_y,0)
    remove=[]
    for total in enemy_info.items():
        key,value=total
        ex,ey,ez=value["pos"]
        delx=player_x-ex
        dely=player_y-ey
        dist=math.sqrt(delx**2+dely**2)
        if dist>0:
            x_new=ex+(delx/dist*0.25)
            y_new=ey+(dely/dist*0.25)
            value["pos"]=(x_new,y_new,ez)
            
        if check_collision(p,80,value["pos"],32):
            remove.append(key)
            player_life-=1
    for k in remove:
        if k in enemy_info:
            del enemy_info[k]

    render_enemy()


def perform_dot_product(gx,enemy_dx,gy,enemy_dy):
    a=gx*enemy_dx+gy*enemy_dy
    return a


def check_enemy(px,py,p_rotation,enemy_loc):

    angle=math.radians(-p_rotation)
    gx=math.sin(angle)
    gy=math.cos(angle)
    ex,ey,ez=enemy_loc

    enemy_dx=ex-px
    enemy_dy=ey-py
    dist=math.sqrt(enemy_dx**2+enemy_dy**2)
    if dist==0:
        return False
    enemy_dx/=dist
    enemy_dy/=dist

    val=perform_dot_product(gx,enemy_dx,gy,enemy_dy)    
    saw=max(-1.0,min(1.0,val))
    rad_ang=math.degrees(math.acos(saw))
    return abs(rad_ang)<=3


def start_auto_firing():

    global fire_delay,last_fire_time,enemy_count,bullets,player_life,bullets_missed,game_state,cheat_mode,player_rotation,enemy_info,player_x,player_y,bullet_counter,bullet_velocity
    current_time=time.time()

    player_rotation-=3
    if current_time-last_fire_time<fire_delay:
        return 
    for item in enemy_info.items():
        key,value=item

        ex,ey,ez=value["pos"]
        if check_enemy(player_x,player_y,player_rotation,value["pos"]):
            bullet_counter+=1
            direct=math.radians(-player_rotation)
            delx=bullet_velocity*math.sin(direct)
            dely=bullet_velocity*math.cos(direct)
            bullets[bullet_counter]=(player_x,player_y,delx,dely)
            last_fire_time=current_time
            break 
    
    render_enemy()
    player_enemy_interaction()

    glutPostRedisplay()


def animate():

    global enemy_count,bullets,player_life,bullets_missed,game_state,cheat_mode,player_rotation,enemy_info

    if bullets_missed>=10 or player_life<=0:
        game_state="over"

    elif game_state=="play":
        if cheat_mode=="on":
            start_auto_firing()

        render_bullet()
        render_enemy()
        player_enemy_interaction()            
    glutPostRedisplay()


def display():
    
    global game_state,player_life,game_score,bullets_missed
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset modelview matrix
    glViewport(0, 0, 1000, 800)  # Set viewport size
    setup_camera()  
    draw_floor()
    draw_boundary()

    if game_state=="play":
        draw_player()
        generate_enemy()
        draw_bullet()
        draw_text(10, 670, f"Player Life Remaining: {player_life}")
        draw_text(10, 640, f"Game Score: {game_score}")
        draw_text(10,610,f"Bullets Remaining: {bullets_missed}")
        
        
    elif game_state=="over":
        draw_text(10,640,f"Game is Over. Your Score is {game_score}", GLUT_BITMAP_TIMES_ROMAN_24)
        draw_text(10,610,f"Press R to RESTART the Game ", GLUT_BITMAP_TIMES_ROMAN_24)
        draw_lying_player()
    
    glutSwapBuffers()


# Main function to set up OpenGL window and loop
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Double buffering, RGB color, depth test
    glutInitWindowSize(1000, 700)  # Window size
    glutInitWindowPosition(200, 0)  # Window position
    window= glutCreateWindow(b"3D Firing Game ")  # Create the window

    glutDisplayFunc(display)  # Register display function
    glutKeyboardFunc(keyboardListener)  # Register keyboard listener
    glutSpecialFunc(handlecamera)
    glutMouseFunc(mouseListener)
    glutIdleFunc(animate)  # Register the idle function to move the bullet automatically
    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()


