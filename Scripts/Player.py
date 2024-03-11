import pygame, math, Scripts.Level
import random

class Player:
    def __init__(self):
        self.textCoordonate = ()
        self.writeText = False
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.tile_size = Scripts.Level.level.tile_size
        self.textOnScreen = False
        self.isMoving = False
        self.level = 1
        self.dimension = 1
        self.stealth_map_number = 0
        self.map_number = 1
        self.quality = 1
        self.map = Scripts.Level.level.map
        self.fov = 120
        self.x = 630
        self.y = 622
        self.rotation = 90
        self.rect = pygame.Surface((10, 20), pygame.SRCALPHA)
        self.speed = 0.5
        self.rect.fill((0,0,250))
        self.finished = 0
        self.hint = 0

    def write(self, screen):
        if self.writeText == True:
            rendered_text = self.font.render(self.text, True, (250, 250, 250), (0, 0, 0))
            text_rect = rendered_text.get_rect()
            text_rect.center = self.textCoordonate
            screen.blit(rendered_text, text_rect)

    def cast_rays(self, screen):
        #print(importlib.import_module(f'Scripts.Level.level.stealth_map{str(self.level)}'))
        for ray_angle in range(self.fov):
            angle = math.radians(self.rotation + ray_angle - self.fov // 2)
            ray_x, ray_y = self.x, self.y
            while True:
                ray_x += self.quality * math.cos(angle)
                ray_y -= self.quality * math.sin(angle)

                dx = ray_x - self.x
                dy = ray_y - self.y
                distance = math.sqrt(dx**2 + dy**2)

                map_y = int(ray_y // self.tile_size)
                map_x = int(ray_x // self.tile_size)

                if self.map[map_y][map_x] == 1:
                    color = 1
                    break
                if self.map[map_y][map_x] == 2:
                    color = 2
                    break
                if self.map[map_y][map_x] == 5:
                    color = 3
                    if distance < 7:
                        print(self.level)
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound('level.mp3'))
                        self.text = 'New Level !'
                        self.textCoordonate = (600, 100)
                        self.writeText = True
                        self.textStealthDimension = 1
                        if self.level == 1:
                            self.map = Scripts.Level.level.map2
                            self.x = 628
                            self.y = 704
                            self.rotation = 90
                            self.level += 1
                            break
                        if self.level == 2:
                            self.map = Scripts.Level.level.map3
                            self.x = 628
                            self.y = 704
                            break
                    else:
                        break
                if self.map[map_y][map_x]  == 3:
                    if distance < 7 :
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound('level.mp3'))
                        if self.dimension == 1:
                            self.dimension = 0
                            if self.level == 1:
                                self.map = Scripts.Level.level.stealth_map
                            elif self.level == 2:
                                self.map = Scripts.Level.level.stealth_map2
                        else:
                            self.dimension = 1
                            if self.level == 1:
                                self.map = Scripts.Level.level.map
                            elif self.level == 2:
                                self.map = Scripts.Level.level.map2
                        randomNumber = random.randint(0,1)
                        print(randomNumber)
                        if randomNumber == 1:
                            pygame.mixer.Channel(0).pause()
                            pygame.mixer.Channel(1).unpause()
                        elif randomNumber == 0:
                            pygame.mixer.Channel(0).unpause()
                            pygame.mixer.Channel(1).pause()
                if self.map[map_y][map_x]  == 4 and distance < 7 and not self.textOnScreen and self.dimension == 1:
                    if self.level == 1:
                        self.text = 'Welcome to the easiest game of all time !'
                        self.textCoordonate = (600, 100)
                        self.writeText = True
                    if self.level == 2:
                        self.text = 'This level looks normal.'
                        self.textCoordonate = (600, 100)
                        self.writeText = True

                if self.map[map_y][map_x]  == 4 and distance < 7 and not self.textOnScreen and self.dimension == 0:
                    if self.level == 1:
                        self.text = '...'
                        self.textCoordonate = (600, 100)
                        self.writeText = True
                    if self.level == 2:
                        self.text = 'I feel a little bit dizzy, I feel like something has changed.'
                        self.textCoordonate = (600, 100)
                        self.writeText = True
                        self.textStealthDimension += 1

                if self.map[map_y][map_x]  == 6 and distance < 7 and not self.textOnScreen and self.dimension == 0:
                    if self.level == 1:
                        self.text = 'I remember that we could turn to the left here, thats weird'
                        self.textCoordonate = (600, 100)
                        self.writeText = True
                    if self.level == 2:
                        self.text = 'I am missing some hours of sleep or i must be dreaming'
                        self.textCoordonate = (600, 100)
                        self.writeText = True
                        self.textStealthDimension += 1
                if self.map[map_y][map_x]  == 6 and distance < 7 and not self.textOnScreen and self.dimension == 1:
                    if self.level == 1:
                        self.text = 'Everything must be normal right ?'
                        self.textCoordonate = (600, 100)
                        self.writeText = True
                    if self.level == 2:
                        self.text = 'Lets do the turn of the red thing.'
                        self.writeText = True
                        self.textStealthDimension += 1

            height = 8000 / (distance)

            y1 = 400 - int(height)
            y2 = 400 + int(height)

            try:
                if color == 1:
                    distance_color = abs(distance)
                    if 255 < distance_color:
                        distance_color = 255
                    pygame.draw.line(screen, (200, distance_color, 200), (ray_angle * 1200 // self.fov, y1), (ray_angle * 1200 // self.fov, y2), 7)
                if color == 2:
                    pygame.draw.line(screen, (250, 0, 0), (ray_angle * 1200 // self.fov, y1), (ray_angle * 1200 // self.fov, y2), 7)

                if color == 3:
                    pygame.draw.line(screen, (100, 0, 50), (ray_angle * 1200 // self.fov, y1), (ray_angle * 1200 // self.fov, y2), 7)

            except:
                pass

    def move(self,screen):  
        rotated_rect = pygame.transform.rotate(self.rect, self.rotation)        
        #screen.blit(rotated_rect, (self.x, self.y))

        if self.map[int(self.y // Scripts.Level.level.tile_size)][int(self.x // Scripts.Level.level.tile_size)] == 1 or self.map[int(self.y // Scripts.Level.level.tile_size)][int(self.x // Scripts.Level.level.tile_size)] == 2 :
            self.x -= self.speed * math.cos(math.radians(self.rotation))
            self.y += self.speed * math.sin(math.radians(self.rotation))
        else:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LSHIFT]:
                self.speed = 1
            else:
                self.speed = 0.5

            if keys[pygame.K_d]:
                self.rotation +=3
                self.isMoving = True

            if keys[pygame.K_q]:
                self.rotation -= 3
                self.isMoving = True

            if keys[pygame.K_z]:
                self.isMoving = True
                self.x += self.speed * math.cos(math.radians(self.rotation))
                self.y -= self.speed * math.sin(math.radians(self.rotation))

            if keys[pygame.K_s]:
                self.isMoving = True
                self.x -= self.speed * math.cos(math.radians(self.rotation))
                self.y += self.speed * math.sin(math.radians(self.rotation))