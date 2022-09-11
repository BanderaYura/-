#створи гру "Лабіринт"!
from pygame import*

mixer.init

WIDTH = 700
HEIGHT = 500
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Лабіринт")
clock = time.Clock()

#mixer.music.load("jungels.ogg")
#mixer.music.set_volume(0.5)
#mixer.music.play()

class GameSpirite (spirit.Sprite)
def __init__(self,image_name,x,y,width, height):
    super().__init__()
    self.img = transform.scale(image.load )(image_name), (width,height))
    self.rect = self.img.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = width
    self.height = height
    
class Player(GameSprite):
    def __init__(self):
        super().__init__("hero.png",200,200,75,75)
        self.speed = 5
        self.hp = 100

    def update (self):
        keys = key.get_pressed()
            if keys[K_LEFT]: and self.rect.x > 0 :
                self.rect.x -= self.speed
             if keys[K_RIGHT] and self.rect.x < WIDTH - self.width:
                self.rect.x += self.speed
             if keys[K_UP]: and self.rect.y > 0 :
                self.rect.y -= self.speed
             if keys[K_DOWN] and self.rect.y < HEIGHT - self.height:
                self.rect.y += self.speed
    def update(self):
        pass



bg_image = transform.scale(image.load("background.jpg"), (WIDTH, HEIGHT))
run = True
FPS = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    bg_image = transform.scale(image.load("background.jpg"),(WIDTH))
    player.update()

    player.draw
    window.blit(bg_image,(0,0))
    display.update()
    clock.tick(FPS)