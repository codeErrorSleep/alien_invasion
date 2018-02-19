import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats




def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #键盘按下
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullte(ai_settings, screen, ship, bullets)
    elif event.key==pygame.K_q:
        fp = open("high_score.txt",'w')
        fp.write(GameStats.high_score)
        fp.close
        sys.exit()




def check_keyup_events(event, ship):
        #键盘放开
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False


def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    #检测操作反应
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)



def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    #开始游戏
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏设置
        stats.reset_stats()
        stats.game_active = True
        ai_settings.initialize_dynamic_settings()
        
        
        #清空记录
        aliens.empty()
        bullets.empty()

        #创建新外星人 
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        #影藏光标
        pygame.mouse.set_visible(False)

        sb.prep_ships()
        



'''子弹'''

def fire_bullte(ai_settings,screen,ship,bullets):
    """发射子弹函数"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """子弹位置,删除"""

    bullets.update()

    # 删除子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

    


def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):

    #子弹是否击中
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)


    if len(aliens)==0:
        #新外星人
        bullets.empty()
        ai_settings.increse_speed()
        create_fleet(ai_settings,screen,ship,aliens)

        stats.level +=1
        sb.prep_level()



'''外星人'''

def get_number_rows(ai_settings,ship_height,alien_height):
    '''行'''
    available_spac_y = (ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_spac_y/(2*alien_height))
    return number_rows


def get_number_aliens_x(ai_settings,alien_width):
    """每行外星人人数"""
    available_spac_x = ai_settings.screen_width - alien_width * 2
    number_alien_x = int(available_spac_x / (2 * alien_width))
    return number_alien_x


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人"""
    alien = Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width + 2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)



def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    alien = Alien(ai_settings,screen)
    number_alien_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    """外形人群"""
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
     
      


def check_fleet_edges(ai_settings,aliens):
    #当外星人在边缘时
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    #下移外星人,改变方向
    for alien in  aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1





def ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets):
    #飞船撞到外星人
    if stats.ships_left > 0:
        stats.ships_left -=1

        #删除子弹外星人
        aliens.empty()
        bullets.empty()

        #新外星人,飞机归位
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        sb.prep_ships()

        #暂停
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets):
    #外乡人飞到下面
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #好像撞飞船一样
            ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
            break 


def update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets):
    
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets)

    #外星人飞船碰转
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)







def check_high_score(stats,sb):
    #检查最高分
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()







'''画面更新'''


def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):

    screen.fill(ai_settings.bg_color)
    #显示分数
    sb.show_score()


    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if not stats.game_active:
        play_button.draw_button()


    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()
