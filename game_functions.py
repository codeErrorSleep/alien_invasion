import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #键盘按下
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullte(ai_settings, screen, ship, bullets)
    elif event.key==pygame.K_q:
        sys.exit()




def check_keyup_events(event, ship):
        #键盘放开
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False


def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def fire_bullte(ai_settings,screen,ship,bullets):
    """发射子弹函数"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)




def update_bullets(bullets):
    """子弹位置,删除"""

    bullets.update()

    # 删除子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)






def get_number_aliens_x(ai_settings,alien_width):
    """每行外星人人数"""
    available_spac_x = ai_settings.screen_width - alien_width * 2
    number_alien_x = int(available_spac_x / (2 * alien_width))
    return number_alien_x

def create_alien(ai_settings,screen,aliens,alien_number):
    """创建一个外星人"""
    alien = Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width + 2*alien_width*alien_number
    alien.rect.x=alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens):
    """创建外星人群"""
    alien = Alien(ai_settings,screen)
    number_alien_x=get_number_aliens_x(ai_settings,alien.rect.width)


    """第一行外星人群"""
    for alien_number in range(number_alien_x):
        create_alien(ai_settings,screen,aliens,alien_number)
     
        
        






def update_screen(ai_settings,screen,ship,aliens,bullets):

    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()
