import sys
import pygame
from game_relevant.ball import Ball
import random
from game_relevant.award import Award


def check_event(controller, group, settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                controller.moving_right = True
            elif event.key == pygame.K_LEFT:
                controller.moving_left = True
            elif event.key == pygame.K_SPACE:
                # 如果按下了空格键,说明是要发射球了
                if len(group) == 0:  # 通过group 来监控窗口到底有几个小球
                    # 说明当前没有球.可以进行发射
                    new_bullet = Ball(settings=settings, screen=screen, controller=controller)
                    group.add(new_bullet)
            elif event.key == pygame.K_f:
                temp_list = []
                for ball in group:
                    for index in range(3):  # index 为下标,始终从0开始
                        new_ball = Ball(settings=settings, screen=screen, controller=controller)
                        new_ball.setX_Y(ball.x, ball.y, index)
                        temp_list.append(new_ball)

                # 完成分裂之后.再添加到group当中
                for ball in temp_list:
                    group.add(ball)
                print(temp_list)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                controller.moving_right = False
            elif event.key == pygame.K_LEFT:
                controller.moving_left = False


# 用于更新屏幕
def update_screen(settings, screen, controller, group, blocks, awards):
    """

    :param settings:
    :param screen: 屏幕对象相关参数
    :param controller:  控制器对象相关参数
    :param group: 小球列表相关参数, 列表中的每个参数都是小球对象
    :param blocks: 砖块对象参数
    :param awards: 奖励对象参数
    :return:
    """
    screen.fill(settings.screen_bg)
    controller.blitme()
    for ball in group:
        # 小球的范围超过屏幕的边界, 则自动移除
        # 两个条件是小球没有碰到挡板,死翘翘
        if ball.rect.bottom <= 0 or ball.rect.top >= settings.screen_height:
            group.remove(ball)
        # todo have no idea
        # 为什么要把小球的x 和小球的速度比对
        # 答: 因为小球每秒0.8米,
        # 为什么会有负数的速度
        # 为什么要把小球的x +小球的宽度相加  和屏幕宽度-小球的速度 互相对比
        if ball.rect.x <= settings.ball_speed or (
                    ball.rect.x + settings.ball_width) >= (settings.screen_width - settings.ball_speed):
            ball.make_turn(True)

        # 小球碰到上边界, 往反方向运动
        if ball.rect.top <= 0:
            ball.make_turn(2)

        ball.draw_ball()

    for block in blocks:
        block.blitme()

    for award in awards:
        award.blitme(screen)
        award.update()
    # pygame 开始渲染整个界面
    pygame.display.flip()


# 消除砖块
def update_block(group, blocks, controllers, awards, settings, screen, controller, game_contiune):
    """

    :param group:
    :param blocks: 可消除砖块和不可消除
    :param controllers:
    :param awards:
    :param settings:
    :param screen:
    :param controller:
    :param game_contiune:
    :return:
    """
    # 判断当前的球是否与砖块发生碰撞,如果发生碰撞.进行角度的转换
    dic = pygame.sprite.groupcollide(group, blocks, False, False)
    # 返回的是字典.进行遍历操作
    # {<Ball sprite(in 1 groups)>: [<Block sprite(in 1 groups)>]}
    for key, value in dic.items():
        """key是小球, value 是每个块"""
        if (key.rect.top < value[0].rect.top) or (key.rect.bottom > value[0].rect.bottom):
            # 说明接触面在上面或下面
            key.make_turn(2)
        else:
            key.make_turn(True)
        # 移除砖块
        for v in value:
            # 如果是不能损毁的砖块移除
            if v.destory == False:
                value.remove(v)
            # 如果你消除了砖块, 有百分之3的概率会有奖励的砖块出来
            else:
                if random.randint(0, 100) <= settings.aware_occurrence_rate:
                    new_award = Award(settings, screen, v)
                    awards.add(new_award)

        blocks.remove(value)
    # 判断当前的球是否与控制器发生碰撞,如果发生碰撞.进行角度的转换

    dic2 = pygame.sprite.groupcollide(group, controllers, False, False)
    for key, value in dic2.items():
        key.make_turn(2)
        # ball.make_turn(2)
    # 判断当前的奖励方块是否与控制器发生碰撞,如果发生碰撞.进行角度的转换

    dic3 = pygame.sprite.groupcollide(controllers, awards, False, False)
    for key, value in dic3.items():
        """value 代表的是每个奖励方块
        key代表控制器
        """
        for v in value:
            if v.flag:  # 如果是随机生成的颜色, 说明场上已经有小球了
                # 红色分裂
                temp_list = []
                for ball in group:
                    for index in range(3):
                        new_ball = Ball(settings=settings, screen=screen, controller=controller)
                        new_ball.setX_Y(ball.x, ball.y, index)
                        temp_list.append(new_ball)

                # 完成分裂之后.再添加到group当中
                for ball in temp_list:
                    group.add(ball)
            else:
                # 黄色发射三个
                for index in range(3):
                    new_ball = Ball(settings=settings, screen=screen, controller=controller)
                    new_ball.setX_Y(controller.rect.centerx, controller.rect.centery, index)
                    group.add(new_ball)
                print("send three")
        awards.remove(value)  # 移除游戏buff 加成效果, 防止重复执行
