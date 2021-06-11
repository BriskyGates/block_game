import pygame
import random
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.destory = True
        self.rect = pygame.Rect(random.randint(settings.block_width, settings.screen_width - settings.block_width),
                                random.randint(settings.block_height, settings.screen_height - 200),
                                settings.block_width, settings.block_height)

        # 每个砖块最初都在屏幕左上角附近
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color = (0, 255, 0)
        # 存储砖块的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
