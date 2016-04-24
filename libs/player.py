import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, location, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('assets/images/player.png')
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.resting = False
        self.dy = 300

    def _handle_key(self, key, dt):
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * dt
        if key[pygame.K_UP]:
            self.rect.y -= 300 * dt
        if key[pygame.K_DOWN]:
            self.rect.y += 300 * dt

    def _handle_blockers(self, last, new, game):
        self.resting = False
        for cell in game.tilemap.layers['triggers'].collide(new, 'blockers'):
            blockers = cell['blockers']
            if 'l' in blockers and last.right <= cell.left < new.right:
                new.right = cell.left
            if 'r' in blockers and last.left >= cell.right > new.left:
                new.left = cell.right
            if 't' in blockers and last.bottom <= cell.top < new.bottom:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if 'b' in blockers and last.top >= cell.bottom > new.top:
                new.top = cell.bottom
                self.dy = 0

    def update(self, dt, game):
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        self._handle_key(key, dt)
        new = self.rect
        self._handle_blockers(last, new, game)
        # if self.resting and key[pygame.K_SPACE]:
        #    self.dy = -500
        #self.dy = min(400, self.dy + 40)

        #self.rect.y += self.dy * dt

        game.tilemap.set_focus(new.x, new.y)

        self.groups()[0].camera_x = self.rect.x - 320
