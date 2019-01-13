"""This example lets you dynamically create static walls and dynamic balls
"""
__docformat__ = "reStructuredText"






#Reading data from file generated
coordinates=[]

with open("file1") as f:
    lines = f.readlines()

for line in open("file1"):
	# print(str(line))

	# coordinates.append(k)
    z=line.split(" ")
    a=z[0][1:]
    b=z[1][:len(z[1])-2]
    k=a,b
    coordinates.append(k)

# print(coordinates)

# coordinates = [line.rstrip('\n') for line in open('file1')]
# coordinates = [coordinates.rstrip('[') for line in open('file1')]
# coordinates = [coordinates.rstrip(']') for line in open('file1')]
# coordinates = [coordinates.rstrip(',') for line in open('file1')]


# print(type(lines[1000][0]))



import pygame
import time

from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d


X,Y = 0,1
### Physics collision types
COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2


def flipy(y):
    """Small hack to convert chipmunk physics to pygame coordinates"""
    return -y+600

def mouse_coll_func(arbiter, space, data):
    """Simple callback that increases the radius of circles touching the mouse"""
    s1,s2 = arbiter.shapes
    s2.unsafe_set_radius(s2.radius + 0.15)
    return False

def main():
            
    pygame.init()
    screen = pygame.display.set_mode((1336, 720))
    clock = pygame.time.Clock()

    running = True
    gravx=10 
    ### Physics stuff
    space = pymunk.Space()
    space.gravity = gravx, -900.0
    pygame.mixer.music.load("Sans.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    ## Balls
    balls = []
    
    ### Mouse
    mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    mouse_shape = pymunk.Circle(mouse_body, 3, (0,0))
    mouse_shape.collision_type = COLLTYPE_MOUSE
    space.add(mouse_shape)

    space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_BALL).pre_solve=mouse_coll_func   
    
    ### Static line
    line_point1 = None
    static_lines = []
    run_physics = True
    dic={}
    
    lone=1
    baka=False

    while running:

        gravx+=1
        #stop loop if its at the second last instant
        if lone==len(coordinates)-1:
            break;
        # Reading data from file and using coords for it [BALLS]
        # time.sleep(0.1)

        if lone%1336==0:
            lonex=2
            baka=True
            k.position=(20,50)

        # if baka:
            # space.remove(dic[lonex].body=N)
            # space.add_post_step_callback(space.remove, ball)
    # space.add_post_step_callback(space.remove, ball.body)

        
            for i in range(len(dic.keys())-1):
                # if dic
                if i==1334:
                    break;
                print(list(dic.keys()))
                index=list(dic.keys())[i]
                index2=list(dic.keys())[i]
                print(index)
                dic[index]=dic[index2]
        # p=(int(coordinates[lone][0])%1336,50)
        # print(p)
        

        if (lone==1 and gravx==11):
            p2=(20,500)
            body = pymunk.Body(1, 1)
            body.position = p2
            k=body
            firstcircle=body
            shape = pymunk.Circle(body, 1, (0,0))
            # shape.elasticity=1.0
            shape.friction = 0.0




            shape.collision_type = COLLTYPE_BALL
            space.add(body, shape)
            balls.append(shape)

        # print(list(k.position))

        lone+=1


        # z=balls[0].body.position
        # balls[0].body.apply_force_at_world_point((10,0),(z))

        changepath=0

        # Reading data from file and using coords for it [LINES]
        lonex=lone%1337
        if lone%1336==0:
            continue
            baka=True


        line_point1 =  Vec2d((int(lonex)),flipy(10*int(coordinates[lone][0]))-200)

        line_point2 = Vec2d(((int(lonex))),flipy(10*int(coordinates[lone+1][0]))-200)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape= pymunk.Segment(body, line_point1, line_point2, 10.0)
        shape.friction = 0

        space.add(shape)
        static_lines.append(shape)
        dic[lonex]=shape
        poscoords=list(k.position)
        k.apply_force_at_world_point((int(poscoords[0]),int(poscoords[1])),list(k.position))

        



        for event in pygame.event.get():


            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == KEYDOWN and event.key==K_d:
                k.apply_force_at_world_point((1000,0),k.position)
            elif event.type == KEYDOWN and event.key==K_a:
                k.apply_force_at_world_point((-1000,0),k.position)

            elif event.type == KEYDOWN and event.key == K_p:
                pygame.image.save(screen, "balls_and_lines.png")
            elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # print(event.pos[X],flipy(event.pos[Y]))
                p = event.pos[X], flipy(event.pos[Y])
                print("HELPPP")
                relpos=p-(k.position)
                print(relpos)
                k.apply_force_at_world_point((100*(int(relpos[0])),100*(int(relpos[1]))),k.position)
                
                
            # elif event.type == MOUSEBUTTONDOWN and event.button == 3: 
            #     if line_point1 is None:
            #         line_point1 = Vec2d(event.pos[X], flipy(event.pos[Y]))
            elif event.type == MOUSEBUTTONUP and event.button == 3: 
                if line_point1 is not None:
                    
                    line_point2 = Vec2d(event.pos[X], flipy(event.pos[Y]))
                    body = pymunk.Body(body_type=pymunk.Body.STATIC)
                    shape= pymunk.Segment(body, line_point1, line_point2, 1000000000.0)
                    shape.friction = 0.0
                    space.add(shape)
                    static_lines.append(shape)
                    line_point1 = None
            
            elif event.type == KEYDOWN and event.key == K_SPACE:    
                run_physics = not run_physics
        
        p = pygame.mouse.get_pos()
        mouse_pos = Vec2d(p[X],flipy(p[Y]))
        mouse_body.position = mouse_pos
        
        
        if pygame.key.get_mods() & KMOD_SHIFT and pygame.mouse.get_pressed()[0]:
            body = pymunk.Body(10, 10)
            body.position = mouse_pos
            shape = pymunk.Circle(body, 5, (0,0))
            shape.collision_type = COLLTYPE_BALL
            space.add(body, shape)
            balls.append(shape)
       
        ### Update physics
        if run_physics:
            dt = 1.0/60.0
            for x in range(1):
                space.step(dt)
            
        ### Draw stuff
        screen.fill(THECOLORS["red"])

        # Display some text
        font = pygame.font.Font(None, 16)
        text = """LMB: Create ball
LMB + Shift: Create many balls
RMB: Drag to create wall, release to finish
Space: Pause physics simulation"""
        y = 5
        for line in text.splitlines():
            text = font.render(line, 1,THECOLORS["black"])
            screen.blit(text, (5,y))
            y += 10

        for ball in balls:           
            r = ball.radius
            v = ball.body.position
            rot = ball.body.rotation_vector
            p = int(v.x), int(flipy(v.y))
            p2 = Vec2d(rot.x, -rot.y) * r * 0.9
            pygame.draw.circle(screen, THECOLORS["blue"], p, int(r), 1)
            pygame.draw.line(screen, THECOLORS["red"], p, p+p2)

        # if line_point1 is not None:
        #     p1 = line_point1.x, flipy(line_point1.y)
        #     p2 = mouse_pos.x, flipy(mouse_pos.y)
        #     pygame.draw.lines(screen, THECOLORS["black"], False, [p1,p2])

        for i in dic:
            line=dic[i]
            body = line.body
            # print(list(line.a.rotated(body.angle))+["fhfjffjfjh"])            
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = pv1.x, flipy(pv1.y)
            p2 = pv2.x, flipy(pv2.y)
            pygame.draw.lines(screen, THECOLORS["lightgray"], False, [p1,p2])


        ### Flip screen
        pygame.display.flip()
        # clock.tick(50)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))
        # time.sleep(0.1)
        
if __name__ == '__main__':
    doprof = 0
    if not doprof: 
        main()
    else:
        import cProfile, pstats
        
        prof = cProfile.run("main()", "profile.prof")
        stats = pstats.Stats("profile.prof")
        stats.strip_dirs()
        stats.sort_stats('cumulative', 'time', 'calls')
        stats.print_stats(30)