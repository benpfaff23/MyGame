# File created by Ben Pfaff

''' 
My Goal: New Platforms
Reach Goal: Collide with enemies
'''
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)

        self.platforms.add(self.plat1)
        
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # for i in range(0,10):
        #     m = Mob(20,20,(0,255,0))
        #     self.all_sprites.add(m)
        #     self.enemies.add(m)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                # if the player hits this specific platform, the player will receive a boost into the air
                if hits[0].variant == "boost":
                    self.player.vel.y *= -1.5
                    self.player.image.fill((50,200,50))
                    # once the player hits this platforrm it will disappear 
                # if the player hits this specific platform, the player will be shot to the ground
                elif hits[0].variant == "fake":
                    self.player.vel.y *= 6
                    self.player.image.fill(RED)
                    # once the player hits this platforrm it will disappear 
                    hits[0].kill()
                elif hits[0].variant == "fake2":
                    self.player.vel.y *= 6
                    self.player.image.fill(RED)
                    # once the player hits this platforrm it will disappear 
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                    self.player.image.fill(BLACK)
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        # is this a method or a function?
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
    # def mob_collide(self):
    #         hits = pg.sprite.spritecollide(self, self.enemies, True)
    #         if hits:
    #             self.enemies.remove()
    #             print("you collided with an enemy...")
    #             self.game.score += 1
    #             print(SCORE)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()