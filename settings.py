class Settings():

    def __init__(self):

        #显示窗口设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color=(230,230,230)

        #飞船设置
        self.ship_speed_factor=1.5

        #子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed = 10

        #外星人
        self.alien_speed_facoor=1
        self.fleet_drop_speed = 10
        #fleet_direction  1向右移,-1向左移
        self.fleet_direction = 1 

    