import sys, time
import pygame
import Scripts.Player, Scripts.Level
from pygame.locals import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

player = Scripts.Player.Player()

# Game loop.
intro = True

pygame.mixer.init() 
pygame.mixer.Channel(0).play(pygame.mixer.Sound('music.mp3'),-1)
pygame.mixer.Channel(0).set_volume(0.2)
pygame.mixer.Channel(1).play(pygame.mixer.Sound('heartbeat.mp3'),-1)
pygame.mixer.Channel(1).set_volume(1000)
pygame.mixer.Channel(1).pause()

rendered_text = pygame.font.Font('freesansbold.ttf', 32).render("Welcome the game that doesnt have a name bc the creator dont have imagination", True, (250, 250, 250), (0, 0, 0))
text_rect = rendered_text.get_rect()
text_rect.center = (600, 100)
screen.blit(rendered_text, text_rect)

while True:
  screen.fill((0, 0, 0))
  #Scripts.Level.level.draw(screen)

  player.move(screen)
  player.cast_rays(screen)
  #player.write(screen) 

  pygame.display.flip()
  pygame.display.update()
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  fpsClock.tick(fps)