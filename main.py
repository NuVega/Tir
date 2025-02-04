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
target_pos = [random.randint(target_radius, WIDTH - target_radius),
              random.randint(target_radius, HEIGHT - target_radius)]

score = 0
font = pygame.font.SysFont("Arial", 24)

# Переменные для расчёта времени реакции (в миллисекундах)
last_target_spawn_time = pygame.time.get_ticks()
reaction_times = []  # список, в который будем добавлять время реакции

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
                # Вычисляем время реакции (текущее время - время появления мишени)
                current_time = pygame.time.get_ticks()
                reaction_time = current_time - last_target_spawn_time
                # После попадания
                reaction_times.append(reaction_time)
                # Ограничим список последними 10 значениями
                window_size = 10
                if len(reaction_times) > window_size:
                    recent_reactions = reaction_times[-window_size:]
                else:
                    recent_reactions = reaction_times
                avg_reaction = sum(recent_reactions) / len(recent_reactions)
                # Перемещаем мишень в случайное место
                target_pos = [random.randint(target_radius, WIDTH - target_radius),
                              random.randint(target_radius, HEIGHT - target_radius)]

    # Отрисовка
    screen.fill(WHITE)
    draw_target(screen, target_pos, target_radius)
    score_text = font.render("Общий счёт: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))
    # Отрисовка среднего времени реакции, если есть данные
    if reaction_times:
        avg_reaction = sum(reaction_times) / len(reaction_times)
        avg_text = font.render("Средняя скорость: " + str(int(avg_reaction)) + " мс", True, BLACK)
        screen.blit(avg_text, (10, 40))

    pygame.display.flip()

pygame.quit()
sys.exit()