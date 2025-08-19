import pygame
import math

pygame.init()



# ==========================
# Screen: Total
# ==========================
Screen_limit = 100
Screen_info = pygame.display.Info()
Screen_Width = Screen_info.current_w
Screen_Height = Screen_info.current_h

# ==========================
# Character 1: Baba
# ==========================

Baba_imgs = [pygame.image.load(f"data/img/Baba/Baba_frame_{i}.png") for i in range(1, 4)]
Baba_img_late = 60
Baba_size = (300, 300)
Baba_speed = [1, 1]
Baba_location = [Screen_Width/2, Screen_Height/2]

Baba_Main_Data = [Baba_size, Baba_speed, Baba_imgs, Baba_img_late, Baba_location]



# ==========================
# Character 2: Keke
# ==========================