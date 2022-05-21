import pygame.sprite


class Box(pygame.sprite.Sprite):
    def __init__(self, image, coords, id):
        super().__init__()
        self.colideimage = pygame.image.load(r"images/colision box.png")
        self.colideimage = pygame.transform.scale(self.colideimage,
                                                (self.colideimage.get_width() * 5, self.colideimage.get_height() * 5))

        self.image = image
        self.image = pygame.transform.scale(self.image,
                                                (self.image.get_width() * 5, self.image.get_height() * 5))
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.id = id
        self.sloi = None


        self.rect2 = self.colideimage.get_rect()
        self.rect2.midbottom = self.rect.midbottom

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, r, l, u, d, ur):
        if ur == False:
            t = -3
        else:
            t = -5

        if r:
            self.rect.x += t
            self.rect2.x += t
        if l:
            self.rect.x -= t
            self.rect2.x -= t
        if u:
            self.rect.y -= t
            self.rect2.y -= t
        if d:
            self.rect.y += t
            self.rect2.y += t