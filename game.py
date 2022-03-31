import math
import random
from time import sleep
import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

health =3
time=60





# Background
background = pygame.image.load('bg.jpeg')


# Caption and Icon
pygame.display.set_caption("beta lolinder")

# Player
playerImg = pygame.image.load('spaceship.png')
playerImg=pygame.transform.scale(playerImg, (100, 100))
playerX = 350
playerY = 500
playerX_change = 0

player2Img = pygame.image.load('spaceship2.png')
player2Img=pygame.transform.scale(player2Img, (100, 100))
player2X = 350
player2Y = 0
player2X_change = 0
bullet2_state = "ready"

bulletImg = pygame.image.load('bullet2.png')
bulletImg=pygame.transform.scale(bulletImg, (100,100))
bulletX = playerX
bulletY = playerY
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))

def player2(x, y):
    screen.blit(player2Img, (x, y))

font = pygame.font.Font('Roboto-Medium.ttf', 32)

textX = 10
testY = 10

def show_health(x, y):
    score = font.render("Health : " + str(health), True, (255, 255, 255))
    screen.blit(score, (x, y))

text2X=750
text2y=10
time=time-1
pygame.time.delay(1000)

def timer(x, y):
    score = font.render(str(time), True, (255, 255, 255))
    screen.blit(score, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(player2X, player2Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(player2X - bulletX, 2) + (math.pow(player2Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Music
mixer.music.load("mus2.mp3")
mixer.music.play(-1)

# Game Loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or time==0:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and playerX_change>-120 :
                playerX_change = -5
            if event.key == pygame.K_RIGHT and playerX<800:
                playerX_change = 5
            if event.key == pygame.K_UP:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("zap.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and player2X>0 :
                player2X_change = -2
            if event.key == pygame.K_d and player2X<800:
                player2X_change = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player2X_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 736:
        playerY = 736

    player2X += player2X_change
    if player2Y <= 0:
        player2Y = 0
    elif player2Y >= 736:
        player2Y = 736

    # Bullet Movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = isCollision(player2X, player2Y, bulletX, bulletY)
    if collision:
        explosionSound = mixer.Sound("muslim.wav")
        explosionSound.play()
        bulletY = 480
        bullet_state = "ready"
        health=health-1

        player2(player2X, player2Y)

    if health == 0:
        running=False

    player(playerX, playerY)
    player2(player2X, player2Y)
    show_health(textX, testY)
    timer(text2X, text2y)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
