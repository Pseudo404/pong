import pygame
import random
import time

pygame.init()
pygame.display.set_caption("Pong")
infoObject = pygame.display.Info()

run = True
w = infoObject.current_w
h = infoObject.current_h
elapsed_time = 0
screen = pygame.display.set_mode((w, h))
j1_img = "j1.png"
j2_img = "j2.png"
ball_img = "ball.png"
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 40)
score_0 = 0
score_1 = 0

pygame.mouse.set_visible(True)

class J1:

    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.moving = False
        self.up = False
        self.down = False

class J2:

    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.x = w - 30
        self.moving = False
        self.up = False
        self.down = False

class Ball:

    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.speed_x = 400.  # Vitesse de la balle
        self.speed_y = 400.

j1 = J1(j1_img)
j2 = J2(j2_img)
ball = Ball(ball_img)

start_time = time.time()
move_cooldown = 0.2  # Temps de pause entre les mouvements des raquettes
aug = 0.008

while run:

    screen.fill((0, 0, 0))

    time_passed = clock.tick(260)
    time_sec = time_passed / 1000.0
    current_time = time.time()
    elapsed_time = current_time - start_time
    speed0 = aug*10000000000000
    speed = speed0%10000/10

    score1 = font.render(str(score_0), True, (0, 0, 255))
    score2 = font.render(str(score_1), True, (255, 0, 0))
    timer_text = font.render(f"Temps: {int(elapsed_time)}s", True, (255, 255, 255))
    speed_counter = font.render(f"Ball Speed: {int(speed)}", True, (255, 255, 255))

    screen.blit(timer_text, (w // 2 - 40, 10))
    screen.blit(j1.image, j1.rect)
    screen.blit(j2.image, j2.rect)
    screen.blit(ball.image, ball.rect)
    screen.blit(score1, (w // 2, h // 2))
    screen.blit(score2, (w // 2 + 100, h // 2))
    screen.blit(speed_counter, (10, h//2-10))

    ball.rect.x += ball.speed_x * aug
    ball.rect.y += ball.speed_y * aug
    aug += 0.00000000000001

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                score_0 = 0
                score_1 = 0
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_z:
                j1.up = True
            if event.key == pygame.K_s:
                j1.down = True
            if event.key == pygame.K_UP:
                j2.up = True
            if event.key == pygame.K_DOWN:
                j2.down = True
            if event.key == pygame.K_SPACE:
                ball.speed_x = -ball.speed_x

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                j1.up = False
            if event.key == pygame.K_s:
                j1.down = False
            if event.key == pygame.K_UP:
                j2.up = False
            if event.key == pygame.K_DOWN:
                j2.down = False
    
    if j1.up == True and j1.rect.y > 0:
        j1.rect.y -= 5
    if j1.down == True and j1.rect.y <= h - 80:
        j1.rect.y += 5
    if j2.up == True and j2.rect.y > 0:
        j2.rect.y -= 5
    if j2.down == True and j2.rect.y <= h - 80:
        j2.rect.y += 5

    if not (0 <= ball.rect.y <= h - 50):
        ball.speed_y = -ball.speed_y

    # Ball and wall left
    if ball.rect.x <= 0:
        score_1 += 1
        ball.rect.x = w // 2

    # Ball and wall right
    if ball.rect.x >= w - 50:
        score_0 += 1
        ball.rect.x = w // 2

    if j1.rect.colliderect(ball.rect):
        ball.speed_x = abs(ball.speed_x)
    if j2.rect.colliderect(ball.rect):
        ball.speed_x = -abs(ball.speed_x)

    pygame.display.flip()

pygame.quit()
