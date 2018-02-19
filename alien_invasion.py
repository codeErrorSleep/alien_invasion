import pygame
import game_functions as gf
pygame.mixer.init()

from settings import Settings
from  ship import Ship
from  pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard





def run_game():

    pygame.init()
    
    #设置
    ai_settings=Settings()
    
    #场景 
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    
    #名字
    pygame.display.set_caption("Alien Invasion")
    
    #按钮
    play_button = Button(ai_settings,screen,"play")

    #游戏信息统计
    stats=GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    
    #一个外星人,一个子弹,一个船
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens=Group()

  	#外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #bgm
    pygame.mixer.music.load('sounds/bgm.mp3') 
    pygame.mixer.music.play(-1, 1) 
    


    while True:

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)



        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


        if stats.game_active:
	        ship.update()
	        gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
	        gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)

			 






run_game()
