import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Параметры мишени
target_radius = 30
target_width = target_radius * 2
target_height = target_radius * 2

# Прямоугольник для текста
text_rect = pygame.Rect(0, 0, 150, 50)

def generate_target_position():
    #Генерирует позицию центра мишени, так чтобы её изображение не попадало в text_rect
    while True:
        pos = [
            random.randint(target_radius, WIDTH - target_radius),
            random.randint(target_radius, HEIGHT - target_radius)
        ]
        # Вычисляем прямоугольник мишени
        target_rect = pygame.Rect(
            pos[0] - target_radius,
            pos[1] - target_radius,
            target_width,
            target_height
        )
        if not target_rect.colliderect(text_rect):
            return pos

# Начальная позиция мишени
target_pos = generate_target_position()

score = 0
font = pygame.font.SysFont("Arial", 24)


def draw_target(surface, position, radius):
    pygame.draw.circle(surface, RED, position, radius)
    pygame.draw.circle(surface, BLACK, position, radius, 3)  # окантовка


running = True
while running:
    clock.tick(60)  # 60 кадров в секунду
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # При клике проверяем, попал ли пользователь по мишени
            mx, my = event.pos
            distance = ((mx - target_pos[0]) ** 2 + (my - target_pos[1]) ** 2) ** 0.5
            if distance <= target_radius:
                score += 1
                # Перемещаем мишень в случайное место
                target_pos = generate_target_position()

    # Отрисовка
    screen.fill(WHITE)
    draw_target(screen, target_pos, target_radius)
    score_text = font.render("Счёт: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()