import pygame
import random

import game_functions
from game_functions import *

# Initialize the game
pygame.init()

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./assets/spaceship.png')  # Spaceship icon
pygame.display.set_icon(icon)

# Player
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('./assets/enemy.png'))  # Enemy image
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)

# Score
score_value = 0

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))  # RGB

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_x_change = -5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if game_functions.bullet_state == "ready":
                    fire_bullet(player_x, game_functions.bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                player_x_change = 0

    # Checking for boundaries of spaceship
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 4
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -4
            enemy_y[i] += enemy_y_change[i]

        # Collision
        collision = is_collision(enemy_x[i], enemy_y[i], game_functions.bullet_x, game_functions.bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        screen.blit(enemy_img[i], (enemy_x[i], enemy_y[i]))

    # Bullet Movement
    update_bullet()

    player(player_x, player_y)
    show_score(text_x, text_y, score_value)
    pygame.display.update()
