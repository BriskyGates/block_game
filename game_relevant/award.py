# 用于奖励的掉落
import pygame
from pygame.sprite import Sprite
import random


class Award(Sprite):
    def __init__(self, settings, screen, block):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.flag = False
        # 奖励颜色的随机生成
        if random.randint(0, 1) == 0:
            # self.image = pygame.image.load('./pic1.png')
            self.color = (255, 0, 0)
            self.flag = True
        else:
            # self.image = pygame.image.load('./pic2.png')
            self.color = (255, 255, 0)
            self.flag = False
        self.rect = pygame.Rect(block.rect.left,
                                block.rect.top,
                                settings.block_width, settings.block_height)
        # self.rect = self.image.get_rect()
        self.screen = screen.get_rect()
        self.x = float(block.rect.left)
        self.y = float(block.rect.top)
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self, screen):
        # screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, *args):
        # 更新奖励的实时位置
        self.rect.y = self.rect.y + self.settings.aware_down_speed

