import math
import random
import sys
import time
import webbrowser

import pygame

from constants import Baba_Main_Data, Screen_limit, Screen_Height, Screen_Width

class ScreenSaverMain:
    def __init__(self, show_fps= False):
        self.show_fps = show_fps
        self.running = True
        self.screen_state = 0
        
        self.font = pygame.font.SysFont(None, 30)
        
        self.Baba = Baba(*Baba_Main_Data)

    def loop(self, screen, screen_witdh, screen_height):
        clock = pygame.time.Clock()
        while self.running:
            screen.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_SPACE, pygame.K_ESCAPE]:
                        pygame.quit()
                    
                    elif event.key == pygame.K_KP_ENTER:
                        webbrowser.open("steam://rungameid/736260")
            
            self.Baba.move(screen_witdh, screen_height, Screen_limit)
            #self.Baba.turn(random.random() * 90)
            self.Baba.img_change()
            self.Baba.draw(screen)
            
            

            if self.show_fps:
                fps = clock.get_fps()
                fps_text = self.font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
                screen.blit(fps_text, (10, 10))
            
            pygame.display.flip()




class Characters:
    def __init__(self, size: int, speed: list, imgs: list, imgs_rate: int, location: list):
        self.size = size
        self.speed = speed
        self.angle = 0
        
        self.imgs = imgs
        self.img_origin_number, self.img_use_number, self.img_change_rate = 0, 0, imgs_rate
        self.imgs_length = len(imgs)
        
        self.now_img = self.imgs[self.img_use_number]
        
        self.location = location
        
    def move(self, width, height, limit):
        edge = [width, height]
        for i in range(2):
            self.location[i] += self.speed[i]
        
            if self.location[i] <= limit or self.location[i] >= edge[i] - limit:
                self.speed[i] *= -1
        
    def img_change(self):
        self.img_origin_number += 1
        self.img_origin_number %= self.imgs_length * self.img_change_rate
        self.img_use_number = self.img_origin_number // self.img_change_rate
        
        self.now_img = self.imgs[self.img_use_number]
        
    def turn(self, delta_angle):
        self.angle += delta_angle
        self.now_img = pygame.transform.rotate(self.imgs[self.img_use_number], self.angle)
        
    def draw(self, screen):
        screen.blit(self.now_img, self.location)
        


class Baba(Characters):
    def __init__(self, size: int, speed: list, imgs: list, imgs_rate: int, location: list):
        super().__init__(size, speed, imgs, imgs_rate, location)
        self.auto = True
        
    def move(self, width, height, limit):
        if self.auto:
            super().move(width, height, limit)
        else:
            pass




if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((Screen_Width, Screen_Height))
    main = ScreenSaverMain(show_fps=True)
    
    main.loop(screen, Screen_Width, Screen_Height)