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
            
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                    x -= 10
            if key[pygame.K_RIGHT]:
                    x += 10
            if key[pygame.K_UP]:
                    y -= 10
            if key[pygame.K_DOWN]:
                    y += 10

            screen.fill((200,200,200))
            screen.blit(image, (x,y))
            pygame.display.flip()

if __name__ == '__main__':
        pygame.init()
        screen = pygame.display.set_mode((640,480))
        Game().main(screen)
