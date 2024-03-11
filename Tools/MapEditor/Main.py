import pygame,sys, time
from pygame.locals import *

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

class Level:
    def __init__(self):
        self.talk2 = False
        self.m = 1
        self.newLevel = False
        self.talk = False
        self.stealth = False
        self.wall = False
        self.erase = False
        self.tp = False
        self.tile_size = screen.get_width() // 20
        print(self.tile_size)
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.map1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 6, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 2, 2, 2, 2, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 2, 0, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 3, 2, 2, 2, 2, 2, 0, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.map2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 
0, 0, 0, 1, 0, 1, 3, 3, 3, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        
    def drawMap(self, screen):
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                tile_type = self.map[row][col]
                if tile_type == 1:  # Wall
                    tile_rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(screen, (0, 250, 0), tile_rect)
                if tile_type == 2:  # end lvl
                    tile_rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(screen, (250, 0, 0), tile_rect)
                if tile_type == 3:  # stealth tp
                    tile_rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(screen, (0, 0, 250), tile_rect)
                if tile_type == 4:  # Talk
                    tile_rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(screen, (0, 250, 250), tile_rect)
                if tile_type == 5:  # newLevel
                    tile_rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(screen, (100, 100, 100), tile_rect)
                if tile_type == 6:  # talk2
                    tile_rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(screen, (0, 100, 0), tile_rect)

    def write(self,text,police,screen, coordonate):
        font = pygame.font.Font('freesansbold.ttf', police)
        text = font.render(text, True, (250,250,250),(0,0,0))
        textRect = text.get_rect()
        textRect.center = coordonate
        screen.blit(text, textRect)

    def update(self, sizebtwn):
        x, y = pygame.mouse.get_pos()
        ix = x // sizebtwn
        iy = y // sizebtwn
        self.cx, self.cy = ix * sizebtwn, iy * sizebtwn
        self.square = pygame.Rect(self.cx, self.cy, sizebtwn, sizebtwn)
    def draw(self, surface):
        click = pygame.mouse.get_pressed()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.write('WALL',20,screen,(600 // 2-80, 600 // 2-280))
            self.wall = True
            self.erase = False
            self.tp = False
            self.stealth = False
            self.talk = False
            self.newLevel = False
            self.talk2 = False

        if keys[pygame.K_e]:
            self.write('ERASE',20,screen,(600 // 2-80, 600 // 2-280))
            self.wall = False
            self.erase = True
            self.tp = False
            self.stealth = False
            self.talk = False
            self.newLevel = False
            self.talk2 = False

        if keys[pygame.K_f]:
            self.write('TP',20,screen,(600 // 2-80, 600 // 2-280))
            self.wall = False
            self.erase = False
            self.tp = True
            self.stealth = False
            self.talk = False
            self.newLevel = False
            self.talk2 = False

        if keys[pygame.K_s]:
            self.write('STEALTH TP',20,screen,(600 // 2-80, 600 // 2-280))
            self.wall = False
            self.erase = False
            self.tp = False
            self.stealth = True
            self.talk = False
            self.newLevel = False
            self.talk2 = False

        if keys[pygame.K_t]:
            self.write('Talk',20,screen,(600 // 2-80, 600 // 2-280))
            self.wall = False
            self.erase = False
            self.tp = False
            self.stealth = False
            self.talk = True
            self.newLevel = False
            self.talk2 = False

        if keys[pygame.K_y]:
            self.write('Talk2',20,screen,(600 // 2-80, 600 // 2-280))
            self.wall = False
            self.erase = False
            self.tp = False
            self.stealth = False
            self.talk = False
            self.newLevel = False
            self.talk2 = True

        if keys[pygame.K_l]:
            self.write('Talk',20,screen,(600 // 2-80, 600 // 2-280))
            self.wall = False
            self.erase = False
            self.tp = False
            self.stealth = False
            self.talk = False
            self.newLevel = True
            self.talk2 = False

        if keys[pygame.K_m]:
            if self.m == 1:
                self.m = 0
                time.sleep(0.5)
            else:
                self.m = 1
                time.sleep(0.5)

        if click[0]:
            if self.wall == True:
                self.map[int(self.cy/self.tile_size)][int(self.cx/self.tile_size)] = 1
                pygame.draw.rect(surface, (255, 255, 255), self.square)
            if self.erase == True:
                self.map[int(self.cy/self.tile_size)][int(self.cx/self.tile_size)] = 0
                pygame.draw.rect(surface, (0, 0, 0), self.square)
            if self.tp == True:
                self.map[int(self.cy/self.tile_size)][int(self.cx/self.tile_size)] = 2
                pygame.draw.rect(surface, (0, 0, 0), self.square)
            if self.stealth == True:
                self.map[int(self.cy/self.tile_size)][int(self.cx/self.tile_size)] = 3
                pygame.draw.rect(surface, (0, 0, 0), self.square)
            if self.talk == True:
                self.map[int(self.cy/self.tile_size)][int(self.cx/self.tile_size)] = 4
                pygame.draw.rect(surface, (0, 0, 0), self.square)
            if self.talk2 == True:
                self.map[int(self.cy/self.tile_size)][int(self.cx/self.tile_size)] = 6
                pygame.draw.rect(surface, (0, 0, 0), self.square)
            if self.newLevel == True:
                self.map[int(self.cy/self.tile_size)][int(self.cx/self.tile_size)] = 5
                pygame.draw.rect(surface, (0, 0, 0), self.square)

level = Level()

while True:
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(str(level.m), True, (250,250,250),(0,0,0))
    textRect = text.get_rect()
    textRect.center = (600 // 2-80, 600 // 2-200)
    screen.fill((0,0,0))
    screen.blit(text, textRect)

    if level.m == 0:
        level.map = level.map2
    if level.m == 1:
        level.map = level.map1


    level.draw(screen)
    level.drawMap(screen)
    level.update(screen.get_width() // 20)

    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            print(level.map1)
            print(level.map2)
            pygame.quit()
            sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
         pos=pygame.mouse.get_pos()
         btn=pygame.mouse
         print ("x = {}, y = {}".format(pos[0], pos[1]))

    fpsClock.tick(fps)