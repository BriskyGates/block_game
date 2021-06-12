# 游戏参数设置类
class Settings():
    def __init__(self):
        # 屏幕宽度
        self.screen_width = 800
        # 屏幕高度
        self.screen_height = 800
        # 屏幕背景
        self.screen_bg = (20, 20, 82)

        # 控制器的速度
        self.controler_speed =2
        # 控制器的宽度
        self.controller_width = 180
        # 控制器的高度
        self.controller_height =20
        # self.controler_x=600


        # 球的速度
        self.ball_speed = 0.8
        # 球得宽度
        self.ball_width = 15
        self.ball_width = 15

        # 球的高度
        self.ball_height =20
        self.ball_height =15

        # 球的颜色
        self.ball_color = (255, 255, 255)

        # 砖块的宽度
        self.block_width = 15
        # 砖块的高度
        self.block_height = 15

        # 不能损坏砖块出现比例(最大99)
        self.destory_occurrence_rate = 15

        # 砖块数量
        self.block_count = 300

        # 奖励出现比例
        self.aware_occurrence_rate = 3
        self.aware_down_speed = 1