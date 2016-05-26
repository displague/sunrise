import pygame


class ScrolledGroup(pygame.sprite.Group):

  def draw(self, surface):
    for sprite in self.sprites():
      surface.blit(
          sprite.image, (sprite.rect.x - self.camera_x, sprite.rect.y))
