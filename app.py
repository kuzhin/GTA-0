import pygame
import sys

# Инициализация
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Игрок
player = pygame.Rect(400, 300, 40, 40)
player_color = (0, 128, 255)
speed = 5

# Генерация карты (здания, дороги)
buildings = [
    pygame.Rect(100, 100, 200, 15),
    pygame.Rect(400, 200, 180, 12),
    pygame.Rect(200, 400, 220, 160)
]

# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= speed
    if keys[pygame.K_RIGHT]: player.x += speed
    if keys[pygame.K_UP]: player.y -= speed
    if keys[pygame.K_DOWN]: player.y += speed

    # Отрисовка
    screen.fill((30, 30, 30))  # Фон

    # Рисуем здания
    for building in buildings:
        pygame.draw.rect(screen, (120, 120, 120), building)

    # Рисуем игрока (машину)
    pygame.draw.rect(screen, player_color, player)

    pygame.display.flip()
    clock.tick(60)