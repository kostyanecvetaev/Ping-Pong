from pygame import *
from random import randint
font.init()
font = font.Font(None, 70)
win_r = font.render('RED WIN!', True, (255, 0, 0))
win_b = font.render('BLUE WIN!', True, (0, 0, 153))
i1 = 0
i2 = 0
s_1 = font.render(str(i1), True, (0, 0, 153))
s_2 = font.render(str(i2), True, (255, 0, 0))


window = display.set_mode((700, 500))
display.set_caption('PING_PONG')
clock = time.Clock()
FPS = 60
background = transform.scale(image.load('stol.png'), (700, 500))
# speed_x = 2
# speed_y = 2

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, lenght):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, lenght))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
        self.lenght = lenght
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, lenght):
        super().__init__(player_image, player_x, player_y, player_speed,width,lenght)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 320:
            self.rect.y += self.speed
    def updaye(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    
        if keys_pressed[K_s] and self.rect.y < 320:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, lenght, speed_y, speed_x):
        super().__init__(player_image, player_x, player_y, player_speed,width,lenght)
        self.speed_y = speed_y
        self.speed_x = speed_x
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y >= 470:
            self.speed_y *= -1
        if self.rect.y <= 0:
            self.speed_y *= -1
        if sprite.collide_rect(myach, player1):
            self.speed_y *= 1
            self.speed_x *= -1
        if sprite.collide_rect(myach, player):
            self.speed_y *= 1
            self.speed_x *= -1



player = Player(('rak.png'), 0, 250, 6, 40, 175)
player1 = Player(('rak2.png'), 660, 250, 6, 40, 175)
myach = Ball(('myac1.png'), 330, 250, 2, 40, 40, 5, 5)



game = True
finish = False
while game:
    
    for e in event.get():   
        if e.type == QUIT:
            game = False

    if finish != True:

        window.blit(background, (0, 0))
    
        clock.tick(FPS)

        player.reset()
        player.updaye()

        player1.reset()
        player1.update()

        myach.reset()
        myach.update()
        
        window.blit(s_1, (630, 25)) 
        window.blit(s_2, (50, 25)) 

        if myach.rect.x >= 750:  
            i2 += 1
        if myach.rect.x <= -50:
            i1 += 1

        display.update()
