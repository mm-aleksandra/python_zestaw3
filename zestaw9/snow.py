import pygame
import sys
import random

pygame.init()

screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Topienie śniegu")

font = pygame.font.Font(None, 36)
white = (255, 255, 255)
snowflakes = []
snowflake_speed = 2  
snowflake_radius = 10
lives = 10
score = 0


def draw_snowflake(x, y):
    pygame.draw.circle(screen, white, (x, y), snowflake_radius)


def draw_text(text, x, y):
    text_surface = font.render(text, True, white)
    screen.blit(text_surface, (x, y))


def restart_game():
    global lives, score, snowflakes
    lives = 10
    score = 0
    snowflakes = []


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # wciśnięcie myszy
            for snowflake in snowflakes[:]:
                distance = ((mouse_x - snowflake[0])**2 + (mouse_y - snowflake[1])**2)**0.5
                if distance < snowflake_radius:
                    snowflakes.remove(snowflake)
                    score += 1

    # dodanie nowego płatka śniegu
    if random.randint(0, 10) < 1 and len(snowflakes) < 10:  
        snowflakes.append([random.randint(0, screen_width), 0])

    # ruch płatków śniegu
    for snowflake in snowflakes:
        snowflake[1] += snowflake_speed

    # usunięcie płatków poza ekranem
    for snowflake in snowflakes:
        if snowflake[1] >= screen_height:
            snowflakes.remove(snowflake)
            lives -= 1

    screen.fill((0, 0, 0))

    for snowflake in snowflakes:
        draw_snowflake(snowflake[0], snowflake[1])

    draw_text(f"Lives: {lives}", 10, 10)
    draw_text(f"Score: {score}", 10, 50)

    pygame.display.flip()

    if lives <= 0:
        draw_text("Game Over!", screen_width // 4, screen_height // 2 - 40)
        draw_text("Press R to restart.", screen_width // 4, screen_height // 2)
        pygame.display.flip()
        
        # oczekiwanie na naciśnięcie klawisza R
        wait_for_key = True
        while wait_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart_game()
                        wait_for_key = False

    clock.tick(30)


