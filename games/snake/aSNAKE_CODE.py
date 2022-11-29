import pygame
import random
# POTENTIAL FEATURES
# new buff - reverse controls
# increase snake speed at different thresholds. Either 10 -> 20 -> 30 pxl or change pygame.time.wait
# menu window (start game, highscores, settings, exit game)
# settings (n food, easy/hard mode with set velocities? + separate highscores)
# GAME OVER, play again Y/exit to menu/exit game

# PROBLEMS
# vel dependant on tick rate (moze dodac przy kazdym ticku counter, i vel jest robiona przy konkretnych value count)
# 1 timer for all buffs so if buff time > spawn time then eating a buff refreshes all the currently active buffs
#      temporary fix : require buff time to be lower than spawn time

pygame.init()

# SCREEN
window = pygame.display.set_mode((600, 650))
pygame.display.set_caption('SNAKE')
icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(icon)


# SETTINGS
setting_buff_time = 5
setting_buff_spawn_time = 10  # BUFF SPAWN TIME CANNOT BE LOWER THAN BUFF TIME
setting_vel = 10
snake_start_length = 10
buffs_enabled = True
buff_food_n = 3
setting_walls = True
walls = setting_walls
if walls:
    background = pygame.image.load('snake_bg.png')
else:
    background = pygame.image.load('snake_bg_wall_false.png')

# SNAKE
snake_img = pygame.image.load('snake_dot.png')
snakeX = 300
snakeY = 300
snake_position = []
for i in range(snake_start_length - 1):
    snake_position.insert(0, (snakeX - 10 * i, snakeY))
velX = 10
velY = 0
direction = ''

# FOOD
foodX = []
foodY = []
food_n = 0

# BUFF
buff_img = pygame.image.load('buff_dot.png')
buffX = -10
buffY = -10
buff_state = False
buff_active = False
eat_buff_time = 0
counter_wall = 0

# TIME AND DISPLAY
clock = pygame.time.Clock()
tick_rate = 10
score_value = 0

# FONTS
font_score = pygame.font.Font('retro_computer_personal_use.ttf', 40)
font_buff = pygame.font.Font('retro_computer_personal_use.ttf', 20)


def snake_go(x, y):
    snake_position.append((x, y))
    for coordinates in snake_position:
        window.blit(snake_img, coordinates)
    snake_position.pop(0)


def food_spawn():
    global foodX, foodY, food_n
    if food_n == 0:
        x = snakeX
        y = snakeY
        while (x, y) in snake_position:
            x = 10 * random.randint(1, 58)
            y = 10 * random.randint(1, 58)
        foodX.append(x)
        foodY.append(y)
        food_n = 1
    for food in range(0, len(foodX)):
        window.blit(snake_img, (foodX[food], foodY[food]))


def food_eat(s_x, s_y, f_x, f_y):
    global score_value, food_n, foodX, foodY
    distance_food = ((s_x - f_x) ** 2 + (s_y - f_y) ** 2) ** (1/2)
    if distance_food == 0:
        score_value += 1
        foodX.remove(f_x)
        foodY.remove(f_y)
        food_n -= 1
        snake_position.insert(0, (s_x, s_y))


def buff_food():
    global foodX, foodY
    for n in range(buff_food_n):
        x = 10 * random.randint(1, 58)
        y = 10 * random.randint(1, 58)
        while x in foodX or y in foodY:
            x = 10 * random.randint(1, 58)
            y = 10 * random.randint(1, 58)
        else:
            foodX.append(x)
            foodY.append(y)


def spawn_buff():
    global buff_state, buffX, buffY, eat_buff_time
    if pygame.time.get_ticks() - eat_buff_time >= setting_buff_spawn_time * 1000:
        if not buff_state:
            buffX = snakeX
            buffY = snakeY
            while (buffX, buffY) in snake_position:
                buffX = 10 * random.randint(1, 58)
                buffY = 10 * random.randint(1, 58)
            buff_state = True
    window.blit(buff_img, (buffX, buffY))


def eat_buff(s_x, s_y, b_x, b_y):
    global score_value, buff_state, tick_rate, eat_buff_time, buffX, buffY, buff_active, walls, background, food_n
    distance_buff = ((s_x - b_x) ** 2 + (s_y - b_y) ** 2) ** (1/2)
    if distance_buff == 0:
        eat_buff_time = pygame.time.get_ticks()
        score_value += 5
        buff_state = False
        buffX = -10
        buffY = -10
        buff_active = True

        if food_n == 1:
            buff_rng = random.randint(1, 4)
        else:
            buff_rng = random.randint(2, 4)
        if buff_rng == 1:
            buff_food()
            food_n += buff_food_n
            buff_active = False
        if buff_rng == 2:
            tick_rate = 30
        if buff_rng == 3:
            tick_rate = 20
        if buff_rng == 4:
            background = pygame.image.load('snake_bg_wall_false.png')
            walls = False
    if pygame.time.get_ticks() - eat_buff_time > setting_buff_time * 1000:
        tick_rate = 10
        buff_active = False
        if setting_walls:
            walls = True
            background = pygame.image.load('snake_bg.png')


def collision_self(s_x, s_y):
    global snake_position, running
    for x, y in snake_position[0: -1]:
        distance_self = ((s_x - x) ** 2 + (s_y - y) ** 2) ** (1/2)
        if distance_self == 0:
            running = False


def show_score(x, y):
    score = font_score.render(f'Score: {score_value}', True, (255, 255, 255))
    window.blit(score, (x, y))


def show_buff_time(x, y):
    if buff_active:
        timer_current = setting_buff_time - ((pygame.time.get_ticks() - eat_buff_time) / 1000).__floor__()
        buff_time = font_buff.render(f'Current buff: {timer_current}', True, (255, 255, 255))
    else:
        buff_time = font_buff.render('Current buff:', True, (255, 255, 255))
    window.blit(buff_time, (x, y))


def show_next_buff(x, y):
    if not buff_state and buffs_enabled:
        timer_next = setting_buff_spawn_time - ((pygame.time.get_ticks() - eat_buff_time) / 1000).__floor__()
    else:
        timer_next = ''
    next_buff = font_buff.render(f'Next buff: {timer_next}', True, (255, 255, 255))
    window.blit(next_buff, (x, y))


running = True
while running:
    window.blit(background, (0, 0))
    key_press_state = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 'down' and not key_press_state:
                    velX = 0
                    velY = -setting_vel
                    direction = 'up'
                    key_press_state = True
            if event.key == pygame.K_DOWN:
                if direction != 'up' and not key_press_state:
                    velX = 0
                    velY = setting_vel
                    direction = 'down'
                    key_press_state = True
            if event.key == pygame.K_LEFT:
                if direction != 'right' and not key_press_state:
                    velX = -setting_vel
                    velY = 0
                    direction = 'left'
                    key_press_state = True
            if event.key == pygame.K_RIGHT:
                if direction != 'left' and not key_press_state:
                    velX = setting_vel
                    velY = 0
                    direction = 'right'
                    key_press_state = True

    # SNAKE POSITION AND SELF COLLISION
    snakeX += velX
    snakeY += velY
    collision_self(snakeX, snakeY)

    # WALLS
    if walls:
        if snakeX < 10 or snakeX >= 590:
            running = False
        if snakeY < 10 or snakeY >= 590:
            running = False
    else:
        if snakeX < 10:
            snakeX = 580
        elif snakeX > 580:
            snakeX = 10
        elif snakeY < 10:
            snakeY = 580
        elif snakeY > 580:
            snakeY = 10

    # MOVE
    snake_go(snakeX, snakeY)

    # FOOD AND BUFF
    food_spawn()
    for i in range(0, len(foodX)):
        try:
            food_eat(snakeX, snakeY, foodX[i], foodY[i])
        except IndexError:
            pass
    if buffs_enabled:
        spawn_buff()
        eat_buff(snakeX, snakeY, buffX, buffY)

    # DISPLAYS
    show_score(10, 596)
    show_buff_time(350, 600)
    show_next_buff(401, 622)

    clock.tick(tick_rate)
    pygame.display.update()
