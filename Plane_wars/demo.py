from random import randrange

import pygame

screen_rect = pygame.Rect(0, 0, 480, 700)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img_path, speed=0):
        super().__init__()
        # 加载图像
        self.image = pygame.image.load(img_path)
        # 设置尺寸
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__('./background.png', 1)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        super().update()
        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height


class Hero(GameSprite):
    def __init__(self):
        super().__init__('./hero.png')
        self.rect.centerx = screen_rect.centerx
        self.rect.bottom = screen_rect.bottom - 100
        self.bullet_group = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_rect.right:
            self.rect.right = screen_rect.right

    def fire(self):
        for i in range(1):
            hero_bullet = Bullet()
            hero_bullet.rect.centerx = self.rect.centerx
            hero_bullet.rect.bottom = self.rect.y - i * 20
            self.bullet_group.add(hero_bullet)


class Enemy(GameSprite):
    def __init__(self):
        super().__init__('./enemy.png')
        self.speed = randrange(2,3)
        self.rect.bottom = 0
        self.rect.x = randrange(0, screen_rect.right - self.rect.right)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y > screen_rect.height:
            self.kill()


class Bullet(GameSprite):
    def __init__(self):
        super().__init__('./bullet.png', -3)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


pygame.init()
screen = pygame.display.set_mode((480, 700))

# 创建精灵和精灵组
bg = Background()
bg2 = Background(is_alt=True)
hero = Hero()

bg_group = pygame.sprite.Group(bg, bg2)
hero_group = pygame.sprite.Group(hero)
enemy_group = pygame.sprite.Group(*[Enemy() for i in range(3)])

clock = pygame.time.Clock()

CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(pygame.USEREVENT, 500)

while 1:
    # 事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == CREATE_ENEMY_EVENT:
            enemy_group.add(Enemy())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero.speed = 3
            elif event.key == pygame.K_LEFT:
                hero.speed = -3
        elif event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
            hero.speed = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            hero.fire()

    c = pygame.sprite.groupcollide(hero.bullet_group, enemy_group, True, True)
    res = pygame.sprite.spritecollide(hero, enemy_group, True)
    if res:
        hero.kill()
        pygame.quit()
        exit()

    clock.tick(165)
    bg_group.update()
    bg_group.draw(screen)
    hero_group.update()
    hero_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    hero.bullet_group.update()
    hero.bullet_group.draw(screen)
    # 更新屏幕显示
    pygame.display.update()
