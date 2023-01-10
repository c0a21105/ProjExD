import pygame
from pygame.locals import *
import os

def load_image(dir, filename, colorkey=None):
    file = os.path.join(dir, filename)
    image = pygame.image.load(file)
    image = image.convert()
    if not colorkey == None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

def split_image(image, n, m):
    image_list = [] # 空のimage_listを作成
    w = image.get_width() #imageのwidthを取得
    h = image.get_height() #imageのheightを取得
    w1 = int(w / n) # 一枚あたりのwidth
    h1 = int(h / m) # 一枚あたりのheight
    for i in range(0, h, h1):
        for j in range(0, w, w1):
            surface = pygame.Surface((w1, h1))
            surface.blit(image, (0, 0), (j, i, w1, h1))
            surface.set_colorkey(surface.get_at((0, 0)), RLEACCEL)
            surface.convert()
            image_list.append(surface)
    return image_list # image_listを返す
