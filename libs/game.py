import pygame
import tmx
from scrolledgroup import ScrolledGroup
from player import Player


class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        background = pygame.image.load('assets/images/background.png')
        sprites = ScrolledGroup()
        sprites.camera_x = 0
        self.walls = pygame.sprite.Group()

        self.tilemap = tmx.load('assets/tilesets/desert.tmx', screen.get_size())

        self.sprites = tmx.SpriteLayer()
        start_cell = self.tilemap.layers['triggers'].find('player')[0]
        self.player = Player((start_cell.px, start_cell.py), self.sprites)
        self.tilemap.layers.append(self.sprites)

        while 1:
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                            return


            self.tilemap.update(dt/1000.,self)
            screen.blit(background, (0,0))
            self.tilemap.draw(screen)
            pygame.display.flip()
