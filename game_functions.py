import pygame
import math

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Load images
player_img = pygame.image.load('./assets/player.png')  # Player image
bullet_img = pygame.image.load('./assets/bullet.png')  # Bullet image

# Score
font = pygame.font.Font('./assets/pixel.ttf', 32)
text_x = 10
text_y = 10

# Game Over
over_font = pygame.font.Font('./assets/pixel.ttf', 64)

# Global bullet state and bullet position
bullet_state = "ready"
bullet_x = 0
bullet_y = 480
bulletY_change = 10


def show_score(x, y, score_value):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(player_img, (x, y))


def fire_bullet(x, y):
    global bullet_state, bullet_x, bullet_y
    bullet_state = "fire"
    bullet_x = x
    bullet_y = y
    screen.blit(bullet_img, (bullet_x + 16, bullet_y + 10))


def is_collision(_enemy_x, _enemy_y, _bullet_x, _bullet_y):
    distance = math.sqrt(math.pow(_enemy_x - _bullet_x, 2) + math.pow(_enemy_y - _bullet_y, 2))
    return distance < 27


def update_bullet():
    global bullet_y, bullet_state
    if bullet_state == "fire":
        screen.blit(bullet_img, (bullet_x + 16, bullet_y + 10))
        bullet_y -= bulletY_change
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
