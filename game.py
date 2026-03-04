import pygame
import random
import sys

pygame.init()


WIDTH = 600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
RED = (255, 0, 0,)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)


player_width = 50
player_height = 60
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 80
player_speed = 7


bullets = []



enemies = []
enemy_speed = 3

score = 0

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

def draw_bullet(x, y):
    pygame.draw.rect(screen, RED, (x, y, 5, 15))

def draw_enemy(x, y):
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 40, 40))

def show_score():
    text = font.render(f"score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH//2 - 100, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()


running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
            bullets.append([player_x + player_width//2, player_y])


    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)


    if random.randint(1, 30) == 1:
        enemy_x = random.randint(0, WIDTH - 40)
        enemies.append([enemy_x, 0])


    for enemy in enemies[:]:
        enemy[1] > HEIGHT:
        if enemy[1] > HEIGHT:
            game_over()


        for bullet in bullets:
            if (enemy[0] < bullet[0] < enemy[0] + 40 and
                enemy[1] < bullet[1] < enemy[1] + 40):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                enemy_speed += 0.1
                break


    draw_player(player_x, player_y)

    for bullet in enemies:
        draw_bullet(bullet[0], bullet[1])

        for enemy in enemies:
            draw_enemy(enemy[0], enemy[1])

        show_score()
        pygame.display.update()

pygame.quit()
