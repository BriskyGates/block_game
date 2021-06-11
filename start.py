# -*- coding: utf-8 -*-

import pygame
from pygame import RESIZABLE

from game_relevant.setting import Settings
from game_relevant.Controller import Controller
import game_function as gf
from pygame.sprite import Group
from game_relevant.block import Block
from game_relevant.ball import Ball
import random

import time


def run_game(name, pwd):
    settings = Settings()
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    file = r'resource/tiger.mp3'  # 音乐的路径
    pygame.mixer.init()  # 初始化
    track = pygame.mixer.music.load(file)  # 加载音乐文件
    pygame.mixer.music.play()  # 开始播放音乐流
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height),RESIZABLE)
    controller = Controller(screen, settings)
    # 用于存放所有的砖块
    blocks = Group()

    for x in range(settings.block_count):
        block = Block(settings, screen)
        ran = random.randint(0, 100)
        if ran < settings.destory_occurrence_rate:
            # 15 % 的概率生成无法破坏的砖块
            block.destory = False
            block.color = (120, 120, 120)
        blocks.add(block)
    pygame.display.set_caption("block_game")
    # 用于存放所有的弹球
    group = Group()
    # 存放控制器的iterator
    controllers = Group()
    controllers.add(controller)
    # 用于存放奖励
    awards = Group()
    # 进行循环判断当前的状态
    game_contiune = True
    win = False
    # 导入赢的图
    picture = pygame.image.load('resource/DD.png')
    picture1 = pygame.image.load('resource/FF.png')
    picture = pygame.transform.scale(picture, (settings.screen_width, settings.screen_height))
    picture1 = pygame.transform.scale(picture1, (settings.screen_width, settings.screen_height))

    total = 1
    num = 3
    sss = 0
    # 进行游戏循环
    while game_contiune:
        # 判断事件
        gf.check_event(controller, group, settings, screen)
        # 如果球为0
        if len(group) == 0:

            if total == 0:
                num -= 1
                total = 1

            if total == 1 and num > 0:
                new_bullet = Ball(settings=settings, screen=screen, controller=controller)
                group.add(new_bullet)

                total = 0
            ww = 0
            # 如果生命值没了 则结束游戏
            if num <= 0:
                while True:
                    pygame.display.update()

                    screen.blit(picture1, (0, 0))
                    # with open('usr_info.pickle', 'rb') as usr_file:
                    #     usrs_info = pickle.load(usr_file)
                    if ffff != -1 and ww == 0:
                        with open('resource/score.txt', 'a+', encoding='utf-8') as ilfe:
                            ilfe.write(name + ' ' + str(ffff) + '\n')
                            ww = 1
                    try:
                        with open('resource/score.txt', 'r', encoding='utf-8') as ii:
                            co = ii.read()
                            co = co.split('\n')
                        pp = 0
                        font = pygame.font.SysFont("SimHei.ttf", 70)  # 30:font size
                        text = font.render('name  score', True, (255, 20, 20))  # (0,0,0) color of font
                        screen.blit(text, (300, 250))
                        s2 = {}
                        for i in co:
                            print(i, ' ', len(co))
                            try:
                                i = i.split()
                                name = i[0]
                                score = i[1]
                            except:
                                continue
                            if s2.get(name) != None:
                                if int(score) >= s2[name]:
                                    s2[name] = int(score)
                            else:
                                s2[name] = int(score)

                        d = s2  # 首先建一个字典d

                        # d.items()返回的是： dict_items([('a', 1), ('c', 3), ('b', 2)])

                        d_order = sorted(d.items(), key=lambda x: x[1], reverse=True)  # 按字典集合中，每一个元组的第二个元素排列。
                        d_order = d_order[:5]
                        # x相当于字典集合中遍历出来的一个元组。
                        print('d')
                        print(d_order)  # 得到:  [('a', 1), ('b', 2), ('c', 3)]
                        for i in d_order:
                            i = str(i[0]) + '        ' + str(i[1])
                            print(i)
                            pp += 50
                            font = pygame.font.SysFont("SimHei.ttf", 70)  # 30:font size
                            text = font.render(i, True, (255, 20, 20))  # (0,0,0) color of font
                            screen.blit(text, (300, 300 + pp))
                    except:
                        pass
                    # pygame.quit()
                    pygame.display.update()
                    time.sleep(5)
                    pygame.quit()

                    return ffff
            # else:

        controller.update()
        s = 0
        sss = 0

        # 判断砖块还有多少
        for i in blocks:

            if i.destory == True:
                s += 1

            if i.destory == False:
                sss += 1

        ffff = settings.block_count - sss - s
        # 当砖块为0时胜利

        if s == 0:
            while True:
                pygame.display.update()

                screen.blit(picture, (0, 0))
                # with open('usr_info.pickle', 'rb') as usr_file:
                #     usrs_info = pickle.load(usr_file)
                if ffff != -1 and ww == 0:
                    with open('resource/score.txt', 'a+', encoding='utf-8') as ilfe:
                        ilfe.write(name + ' ' + str(ffff) + '\n')
                        ww = 1
                try:
                    with open('resource/score.txt', 'r', encoding='utf-8') as ii:
                        co = ii.read()
                        co = co.split('\n')
                    pp = 0
                    font = pygame.font.SysFont("SimHei.ttf", 70)  # 30:font size
                    text = font.render('name  score', True, (255, 20, 20))  # (0,0,0) color of font
                    screen.blit(text, (300, 250))
                    s2 = {}
                    for i in co:
                        print(i, ' ', len(co))
                        try:
                            i = i.split()
                            name = i[0]
                            score = i[1]
                        except:
                            continue
                        if s2.get(name) != None:
                            if int(score) >= s2[name]:
                                s2[name] = int(score)
                        else:
                            s2[name] = int(score)

                    d = s2  # 首先建一个字典d

                    # d.items()返回的是： dict_items([('a', 1), ('c', 3), ('b', 2)])

                    d_order = sorted(d.items(), key=lambda x: x[1], reverse=True)  # 按字典集合中，每一个元组的第二个元素排列。
                    d_order = d_order[:5]
                    # x相当于字典集合中遍历出来的一个元组。
                    print('d')
                    print(d_order)  # 得到:  [('a', 1), ('b', 2), ('c', 3)]
                    for i in d_order:
                        i = str(i[0]) + '        ' + str(i[1])
                        print(i)
                        pp += 50
                        font = pygame.font.SysFont("SimHei.ttf", 70)  # 30:font size
                        text = font.render(i, True, (255, 20, 20))  # (0,0,0) color of font
                        screen.blit(text, (300, 300 + pp))
                except:
                    pass
                # pygame.quit()
                pygame.display.update()
                time.sleep(5)
                pygame.quit()

                return ffff

        s = str(s)
        gf.update_screen(settings, screen, controller, group, blocks, awards)
        group.update()
        # awards.update()
        gf.update_block(group=group, blocks=blocks, controllers=controllers, awards=awards,
                        settings=settings,
                        screen=screen, controller=controller, game_contiune=game_contiune)
        font = pygame.font.SysFont("SimHei.ttf", 70)  # 30:font size
        text = font.render(s, True, (255, 255, 255))  # (0,0,0) color of font
        screen.blit(text, (700, 50))

        font = pygame.font.SysFont("SimHei.ttf", 70)  # 30:font size
        ss = f'Life:{num}'
        text = font.render(ss, True, (255, 255, 255))  # (0,0,0) color of font
        screen.blit(text, (400, 50))
        pygame.display.update()


if __name__ == '__main__':
    run_game('123', '345')
