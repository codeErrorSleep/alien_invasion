class Settings():

    def __init__(self):
        #初始化设置
        #显示窗口设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color=(230,230,230)

        #飞船设置
        self.ship_limit=3

        #子弹设置
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(255,0,0)
        self.bullets_allowed = 10

        #外星人
        self.fleet_drop_speed = 20

        #游戏加速
        self.speed_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        #难度改变
        
        self.ship_speed_factor = 2
        self.bullet_speed_factor=5
        self.alien_speed_facoor=2

         #fleet_direction  1向右移,-1向左移
        self.fleet_direction = 1 

        #记分
        self.alien_points = 50





    def increse_speed(self):
        #加速
       self.ship_speed_factor *=self.speed_scale
       self.alien_speed_facoor  *=self.speed_scale 
       self.fleet_direction *=self.speed_scale 

       self.alien_points = int(self.alien_points * self.score_scale)
