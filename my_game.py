import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        #make sure the player can't go off screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
        

#initalize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

player = Player()

background = pygame.Surface(screen.get_size())
background.fill((0,0,0))

#create main loop
running = True
while running:
    for event in pygame.event.get():
        #if a key is pressed
        if event.type == KEYDOWN:
            #and that key happens to be the esc key
            if event.key == K_ESCAPE:
                running = False
        #if the quit event is run, end the game
        elif event.type == QUIT:
            running = False
    screen.blit(background, (0,0))

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    
    #put rectangle on screen
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

#end pygame
pygame.quit()
