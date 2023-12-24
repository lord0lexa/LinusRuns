import pygame, sys, random
from player import Player
from bg import background
from func import floor_moving, scene_moving
from obstacles import obstacle

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# instances of my classes <3
bg = background()
player = Player()
obs = obstacle()

#obstacle definitions
#random intervall for when smth spawns
intervall = random.randint(6,8)
spawn_timer = 0
rand_obstacle_numb = 0
obstacle_x = [1280,1280,1280,1280]
obstacle_y = [500,500,500,500]
chosen_obstacle = [0,0,0,0]
count = 1
array_exception = []
array_exception.append(1)
array_exception.append(2)
array_exception.append(3)


for x in range(4):
    rand_obstacle_numb = random.randint(0,3)
    if obs.obstacles[rand_obstacle_numb] == obs.gull:
        obstacle_y[x] = 400
    else:
        obstacle_y[x] = 550
    chosen_obstacle[x] = obs.obstacles[rand_obstacle_numb]

curr_spawn = 0



# player position and declarations (velocity & gravity for jumping)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ground = 400
player_pos.y = ground
player_velocity = pygame.Vector2(0,0)
gravity = pygame.Vector2(0,300)

# jumping & sliding sdeclarations
player_jumping = False
player_slide = False
slider_timer = 0
slide_duration = 1.2

#making the floor loop
floor_velocity = 3
floor_x1 = 0
floor_x2 = 1250

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    # jumping
    if keys[pygame.K_UP] and player_pos.y == ground:
        player_velocity.y = -400
        player_jumping = True

    # sliding
    if keys[pygame.K_DOWN] and player_pos.y == ground:
        player_slide = True
        floor_velocity = 6
        slider_timer = 0
        ground = 500

    # sliding when player is jumping
    if keys[pygame.K_DOWN] and player_pos.y < ground:
        player_slide = True
        player_jumping = False
        floor_velocity = 6
        slider_timer = 0
        player_velocity += gravity * dt*5
        ground = 500


    #stopping the slide
    if player_slide:
        slider_timer += dt
        if slider_timer > slide_duration:
            player_slide = False
            floor_velocity = 3
            ground = 400

    # falling when you jump
    player_pos.y += player_velocity.y * dt*1.5
    player_velocity += gravity * dt

    if player_pos.y >= ground:
        player_pos.y = ground
        player_velocity.y = 0

    # penguin is on the floor again
    if player_pos.y == ground:
        player_jumping = False

    # spawning the obstacle.
    # when the random intervall is reached, a random obstacle spawns & the intervall gets chosen again
    # there are 3 obstacles possibles 
        
    for x in range(4):
        if obstacle_x[x] < -1240:
            obstacle_x[x] = 1280
            rand_obstacle_numb = random.randint(0,3)
            if obs.obstacles[rand_obstacle_numb] == obs.gull:
               obstacle_y[curr_spawn] = 400
            else:
                obstacle_y[curr_spawn] = 550
            chosen_obstacle[curr_spawn] = obs.obstacles[rand_obstacle_numb]
            if curr_spawn < 2:
                curr_spawn += 1
            else:
                curr_spawn = 0
            array_exception.append(x)


    if spawn_timer >= intervall:
        intervall = random.randint(5,7)
        spawn_timer = 0
        print(count)
        print(array_exception)
        array_exception.remove(count)

        if count < 3:
            count += 1
        else:
            count = 0

    for x in range(4):
        if x not in array_exception:
            obstacle_x[x] = scene_moving(obstacle_x[x], floor_velocity)

    spawn_timer += dt


    # cute litle layout with looping floor & switching pictures for player & snow
    player.update_sprite( player_jumping, player_slide)
    bg.update_Snow()

    floor_x1, floor_x2 = floor_moving(floor_x1, floor_x2, floor_velocity)


    screen.blit(bg.background, (0,0))
    screen.blit(bg.floor1, (floor_x1,490))
    screen.blit(bg.floor2, (floor_x2, 490))
    screen.blit(bg.currentSnow, (10,10))

    #obstacles

    screen.blit(chosen_obstacle[0], (obstacle_x[0],obstacle_y[0]))
    screen.blit(chosen_obstacle[1], (obstacle_x[1], obstacle_y[1]))
    screen.blit(chosen_obstacle[2], (obstacle_x[2], obstacle_y[2]))
    screen.blit(chosen_obstacle[3], (obstacle_x[3], obstacle_y[3]))



    screen.blit(player.currentSprite, (50,player_pos.y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

