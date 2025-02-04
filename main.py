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


# Загрузка изображения мишени
target_image = pygame.image.load("image/target.png").convert_alpha()
target_width = target_image.get_width()
target_height = target_image.get_height()

# Параметры мишени
target_radius = min(target_width, target_height) // 2

# Начальная позиция мишени
target_pos = [random.randint(target_radius, WIDTH - target_radius),
              random.randint(target_radius, HEIGHT - target_radius)]

score = 0
font = pygame.font.SysFont("Arial", 24)


def draw_target(surface, position):
    # Чтобы центр изображения совпадал с позицией, вычисляем верхний левый угол
    pos_x = position[0] - target_width // 2
    pos_y = position[1] - target_height // 2
    surface.blit(target_image, (pos_x, pos_y))


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
    draw_target(screen, target_pos)
    score_text = font.render("Счёт: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()