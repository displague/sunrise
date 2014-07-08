import pygame

class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()
        
        image = pygame.image.load('player.png')
        x = 100 
        y = 100
        
        while 1:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    return
            x = x % 640 + 1
            y = y % 480 + 1
            screen.fill((y%240,200,200))
            screen.blit(image, (320,240))
            screen.blit(image, (x,y))
            pygame.display.flip()

if __name__ == '__main__':
        pygame.init()
        screen = pygame.display.set_mode((640,480))
        Game().main(screen)
