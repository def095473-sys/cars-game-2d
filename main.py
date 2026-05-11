import pygame

import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Машини - 2D Гонка")

clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Игрок - машина
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 50
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Ограничения экрана
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

# Группы спрайтов
all_sprites = pygame.sprite.Group()
player = Car()
all_sprites.add(player)

# Основной цикл
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Рисование
    screen.fill((0, 100, 0))  # Зеленая дорога
    # Рисуем дорожную разметку
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE, (WIDTH//2 - 5, i, 10, 20))

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
