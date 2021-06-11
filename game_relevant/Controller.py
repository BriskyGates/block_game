import pygame
from pygame.sprite import Sprite


# 最主要的控制器.也就是我们控制的那个方块
class Controller(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        # self.image = pygame.image.load("images/Controller.png")
        # self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(self.screen_rect.centerx, self.screen_rect.bottom, settings.controller_width,
                                settings.controller_height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.color = (255, 255, 255)

    def blitme(self):
        # self.screen.blit(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        # 判断是否到达边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.controler_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.controler_speed
