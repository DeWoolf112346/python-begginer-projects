import random
import time

import pygame

pygame.init()
WIDTH = 700
HEIGHT = 400

score = 0

fon_speed = 4

clock = pygame.time.Clock()

pygame.display.set_caption('Google Dino')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

sprite = 0
ptero_sprite = 0
running_sprites = [pygame.image.load('pic/dino2.png'), pygame.image.load('pic/dino3.png')]

cactus_sprites = [pygame.image.load('cactus/LargeCactus1.png'),
                  pygame.image.load('cactus/LargeCactus2.png'),
                  pygame.image.load('cactus/LargeCactus3.png'),
                  pygame.image.load('cactus/SmallCactus1.png'),
                  pygame.image.load('cactus/SmallCactus2.png'),
                  pygame.image.load('cactus/SmallCactus3.png')]

fon = pygame.image.load('pic/ground.png')
fon_rect = fon.get_rect()
fon_rect.centerx = WIDTH//2
fon_rect.centery = HEIGHT//2 + 25

font_s = pygame.font.Font(None, 50)
text_game_over = font_s.render(f'Конец игры', True, 'white')
text_game_over_rect = text_game_over.get_rect()
text_game_over_rect.centerx = WIDTH//2
text_game_over_rect.centery = HEIGHT//2

yf = HEIGHT//2
ptero_speed = 6

dino_pic = pygame.image.load('pic/dino2.png')
dino_pic_rect = dino_pic.get_rect()
dino_pic_rect.centerx = WIDTH/2
dino_pic_rect.centery = yf
c_sprite = 0
jump = False
jumpc = 5.2
cactus_x = WIDTH
cactus_y = HEIGHT - 175

ptero_sprites = [pygame.image.load('pic/voador1.png'),
                 pygame.image.load('pic/voador2.png')]

x_ptero = WIDTH
ptero_height = [110, 170]
y_ptero = random.choice(ptero_height)

cactus_pic = cactus_sprites[random.randint(0, 5)]

def move_ptero():
    if score > 10:
        global x_ptero, y_ptero, ptero_sprites, ptero_sprite, ptero_speed
        x_ptero -= ptero_speed
        ptero_sprite += 0.05
        if x_ptero < random.randint(-500, -200):
            x_ptero = WIDTH
            y_ptero = random.choice(ptero_height)
        if ptero_sprite >= 2:
            ptero_sprite = 0
        image = ptero_sprites[int(ptero_sprite)]
        rect = image.get_rect()
        rect.center = x_ptero, y_ptero
        screen.blit(image, rect)
        return rect

def dance_cactus():
    global cactus_sprites, c_sprite
    c_sprite += 0.2
    if c_sprite >=6:
        c_sprite = 0
    cactus = cactus_sprites[int(c_sprite)]
    cactus_rect = cactus.get_rect()
    cactus_rect.bottom = HEIGHT - 175
    screen.blit(cactus, cactus_rect)

def move_cactus():
    global dino_pic_rect, cactus_x, cactus_pic, cactus_y, cactus_sprites
    cactus_x -= fon_speed
    if cactus_x < -100:
        cactus_x = WIDTH
        cactus_pic = cactus_sprites[random.randint(0, 5)]
    cactus_pic_rect = cactus_pic.get_rect()
    cactus_pic_rect.bottomleft = cactus_x, cactus_y
    screen.blit(cactus_pic, cactus_pic_rect)
    return cactus_pic_rect

def score_count():
    global score
    score += 1
    font = pygame.font.Font(None, 20)
    text_score = font.render('Счёт: ' + str(score), True, 'black')
    # text_score = font.render(f'Счёт: {score}', True, 'black')
    screen.blit(text_score, (600, 10))

def move_ground():
    global score, fon_speed
    if score > 500:
        fon_speed = 5
    elif score > 1000:
        fon_speed = 6
    fon_rect.x -= fon_speed
    if fon_rect.x <= -560:
        fon_rect.x = 0

def animate():
    global sprite, jumpc, jump, yf
    sprite += 0.05
    if sprite >= 2:
        sprite = 0
    image = running_sprites[int(sprite)]
    rect = image.get_rect()
    rect.centery = yf
    rect.centerx = 50
    screen.blit(image, rect)
    if jump == True:
        if jumpc >= -5.2:
            if jumpc <= 0:
                yf += jumpc ** 2 / 2
            else:
                yf -= jumpc ** 2 / 2
            jumpc -= 0.2
        else:
            jump = False
            jumpc = 5.2
            yf = HEIGHT - 195
        screen.blit(image, rect)
    return rect


right_button = False
left_button = False
start = False

GO = True
while GO:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GO = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_button = True
                start = True
                jump = True
            if event.button == 3:
                dino_pic_rect = 500
                start = True
                right_button = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_button = False
            if event.button == 3:
                right_button = False
    if start:
        if animate().colliderect(move_cactus()):
            screen.fill('black')
            screen.blit(text_game_over, text_game_over_rect)
            time.sleep(10000)

        if score > 500:
            move_ptero()
        # if animate().colliderect(move_ptero()):
            # screen.fill('black')
        # move_ptero()
        score_count()
        # move_cactus()
        # dance_cactus()
        move_ground()
        screen.blit(fon, fon_rect)
        # animate()
    pygame.display.flip()
    clock.tick(100)
pygame.display.flip()
# pygame.quit()