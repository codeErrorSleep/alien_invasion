import pygame
import game_functions as gf


from settings import Settings
from  ship import Ship
from  pygame.sprite import Group
from alien import Alien


def run_game():

    pygame.init()
    #设置
    ai_settings=Settings()
    #场景
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #名字
    pygame.display.set_caption("Alien Invasion")
    #一个外星人,一个子弹,一个船
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens=Group()

  	#外星人群
    gf.create_fleet(ai_settings,screen,aliens)



    while True:
        gf.check_events(ai_settings,screen,ship,bullets)

        ship.update()

        gf.update_bullets(bullets)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)





run_game()
