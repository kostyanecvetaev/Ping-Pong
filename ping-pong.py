#Создай собственный Шутер!

from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('PING_PONG')
clock = time.Clock()
FPS = 60
background = transform.scale(image.load('stol.png'), (700, 500))

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
    def __init__(self, player_image, player_x, player_y, player_speed, width, lenght):
        super().__init__(player_image, player_x, player_y, player_speed,width,lenght)
    def update(myach):
        if myach.rect.y != 0:
            myach.rect.y -= speed_y
            if myach.rect.x != 690:
                myach.rect.x += speed_x


player = Player(('rak.png'), 0, 250, 6, 40, 175)
player1 = Player(('rak2.png'), 660, 250, 6, 40, 175)
myach = Ball(('myac1.png'), 330, 250, 2, 40, 40)

speed_x = 2
speed_y = 2

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
        
        
        display.update()
