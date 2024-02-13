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


# player position and declarations (velocity & gravity for jumping)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ground = 400
player_pos.y = ground
player_pos.x = 50
player_velocity = pygame.Vector2(0,0)
gravity = pygame.Vector2(0,300)
playerStop = False


# obstacle definitions
# random intervall for when smth spawns
intervall = random.randint(6,8)
spawn_timer = 0
rand_obstacle_numb = 0
obstacle_x = [1280,1280,1280,1280]
obstacle_y = [500,500,500,500]
chosen_obstacle = [0,0,0,0]
count = 1

# array_exception is for not respawning an obstacle, that is still in the view
array_exception = [1,2,3]
which_obstacle = [0,0,0,0]


for var in range(4):
    rand_obstacle_numb = random.randint(0,3)
    if obs.obstacles[rand_obstacle_numb] == obs.gull:
        obstacle_y[var] = 320
    else:
        obstacle_y[var] = 500
    chosen_obstacle[var] = obs.obstacles[rand_obstacle_numb]
    which_obstacle[var] = var

curr_spawn = 0

# jumping & sliding declarations
player_jumping = False
player_slide = False
slider_timer = 0
slide_duration = 1.2

#making the floor loop
floor_velocity = 5
floor_x1 = 0
floor_x2 = 1250



while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # import for moving with pressing keys
    keys = pygame.key.get_pressed()

    # jumping
    if keys[pygame.K_UP] and player_pos.y == ground:
        player_velocity.y = -400
        player_jumping = True
        player_slide = False
        ground = 400

    # sliding
    if keys[pygame.K_DOWN] and player_pos.y == ground:
        player_slide = True
        floor_velocity = 7
        slider_timer = 0
        ground = 500

    # sliding when player is jumping
    if keys[pygame.K_DOWN] and player_pos.y < ground:
        player_slide = True
        player_jumping = False
        floor_velocity = 7
        slider_timer = 0
        player_velocity += gravity * dt*5
        ground = 500

    #stopping the slide
    if player_slide:
        slider_timer += dt
        if slider_timer > slide_duration:
            player_slide = False
            floor_velocity = 5
            ground = 400
            player_pos.y = ground


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
        
    for var in range(4):
        if obstacle_x[var] < -500:
            obstacle_x[var] = 1290
            rand_obstacle_numb = random.randint(0,3)
            if obs.obstacles[rand_obstacle_numb] == obs.gull:
               obstacle_y[var] = 320
            else:
                obstacle_y[var] = random.randint(510,530)
            chosen_obstacle[var] = obs.obstacles[rand_obstacle_numb]
            array_exception.append(var)

            #saving the variable, so i can adjust the hitbox later
            which_obstacle[var] = var

    if spawn_timer >= intervall:
        intervall = random.randint(2,4)
        spawn_timer = 0
        #if there is an open spot for the next spawn
        if count in array_exception:
            array_exception.remove(count)

            if count < 3:
                count += 1
            else:
                count = 0

    #making the spawned obstacles move
    for var in range(4):
        if var not in array_exception:
            obstacle_x[var] = scene_moving(obstacle_x[var], floor_velocity)

    spawn_timer += dt


    # cute litle layout with looping floor & switching pictures for player & snow
    if not playerStop:
        player.update_sprite( player_jumping, player_slide)
    bg.update_Snow()

    floor_x1, floor_x2 = floor_moving(floor_x1, floor_x2, floor_velocity)


    screen.blit(bg.background, (0,0))
    screen.blit(bg.floor1, (floor_x1,490))
    screen.blit(bg.floor2, (floor_x2, 490))
    screen.blit(bg.currentSnow, (10,10))
    
    # testing purposes (finding out Hitbox)
    # screen.blit(bg.coordinates, (0,0))

    #obstacles

    screen.blit(chosen_obstacle[0], (obstacle_x[0],obstacle_y[0]))
    screen.blit(chosen_obstacle[1], (obstacle_x[1], obstacle_y[1]))
    screen.blit(chosen_obstacle[2], (obstacle_x[2], obstacle_y[2]))
    screen.blit(chosen_obstacle[3], (obstacle_x[3], obstacle_y[3]))


    screen.blit(player.currentSprite, (player_pos.x,player_pos.y))

    #hitbox activities
    for var in range(3): 
        ob_x = obstacle_x[var] + obs.padding[which_obstacle[var]][0]
        ob_y = obstacle_y[var] + obs.padding[which_obstacle[var]][1]
        ob_x_hitbox = obs.hitbox[which_obstacle[var]][0] + ob_x
        ob_y_hitbox = obs.hitbox[which_obstacle[var]][1] + ob_y

        # Player Hitbox ist smaller when sliding
        if player_slide and player_pos.y is ground:
            player_y_downer = 650
            player_y_upper = 560 
            player_x_left = 100
            player_x_right = 250
        else:
            player_y_downer = player_pos.y + 200
            player_y_upper = player_pos.y + 50        
            player_x_left = 100
            player_x_right = 200
        
        # print(f'{ob_x} <= {player_x_right} + {ob_x_hitbox} >= {player_x_left} + {ob_y} <= {player_y_downer} + {ob_y_hitbox} >= {player_y_upper}')

        if ob_x <= player_x_right and ob_x_hitbox >= player_x_left:
            if ob_y <= player_y_downer and ob_y_hitbox >= player_y_upper:
                print("HITBOX")
                screen.blit(bg.lostGame,(0,0))
                pygame.event.post(pygame.event.Event(pygame.QUIT))



    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

