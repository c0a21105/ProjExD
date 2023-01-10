#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys

import cursor, tools, player, enemy

SCR_RECT = Rect(0, 0, 640, 480)

class Main():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("sample")
        screen = pygame.display.set_mode(SCR_RECT.size)

        self.all = pygame.sprite.RenderUpdates()
        self.enemies = pygame.sprite.Group()
        player.Player.containers = self.all
        enemy.Enemy.containers = self.all, self.enemies

        self.enemy_1 = enemy.Enemy((150, 80))
        self.enemy_2 = enemy.Enemy((330, 400))
        self.player = player.Player((288, 200))

        self.bg = tools.load_image("data", "bg.png")
        # スクロール用のx座標
        self.bgx = 0
        # スクロールスピード
        self.scroll_speed = 3

        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()

    def update(self):
        # スクロール用x座標の更新
        self.bgx = (self.bgx - self.scroll_speed) % SCR_RECT.width
        self.all.update()
        self.collision_detection()

    def draw(self, screen):
        # 背景画像を2枚描画する
        screen.blit(self.bg, (self.bgx, 0))
        screen.blit(self.bg, (self.bgx - SCR_RECT.width, 0))
        self.all.draw(screen)

    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def collision_detection(self):
        enemy_collided = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if enemy_collided:
            print("敵と当たっています")

if __name__ == "__main__":
    Main()
