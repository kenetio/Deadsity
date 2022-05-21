import pygame.sprite
from random import randint


class Tile(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.image.load(f"images/tiles/Tile{randint(1, 9)}.png")
        self.image = pygame.transform.scale(self.image,
                                                (self.image.get_width() * 5, self.image.get_height() * 5))
        self.rect = self.image.get_rect()
        self.rect.topleft = coords

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, r, l, u, d, ur):
        if ur == False:
            t = -3
        else:
            t = -5

        if r:
           self.rect.x += t
        if l:
            self.rect.x -= t
        if u:
            self.rect.y -= t
        if d:
            self.rect.y += t