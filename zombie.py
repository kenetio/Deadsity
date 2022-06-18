import pygame.sprite


class Zombie(pygame.sprite.Sprite):
    def __init__(self, coords, type = None):
        super().__init__()

        self.imagesrun = []
        if type == "polzun":

            self.imagestay = pygame.image.load(r"images/zombies/zombie 2/run1.png")
            self.imagestay = pygame.transform.scale(self.imagestay,
                                                    (self.imagestay.get_width() * 5, self.imagestay.get_height() * 5))

            self.colideimage = pygame.image.load(r"images/zombies/zombie 2/collideimage.png")
            self.colideimage = pygame.transform.scale(self.colideimage,
                                                      (self.colideimage.get_width() * 5,
                                                       self.colideimage.get_height() * 5))

            for i in range(5):
                p = pygame.image.load(f"images/zombies/zombie 2/run{i + 1}.png")
                p = pygame.transform.scale(p, (p.get_width() * 5, p.get_height() * 5))
                self.imagesrun.append(p)
        else:

            self.imagestay = pygame.image.load(r"images/zombies/zombie 1/idle.png")
            self.imagestay = pygame.transform.scale(self.imagestay,
                                                    (self.imagestay.get_width() * 5, self.imagestay.get_height() * 5))

            self.colideimage = pygame.image.load(r"images/player/colideimage.png")
            self.colideimage = pygame.transform.scale(self.colideimage,
                                                      (self.colideimage.get_width() * 5,
                                                       self.colideimage.get_height() * 5))

            for i in range(12):
                p = pygame.image.load(f"images/zombies/zombie 1/run/run{i + 1}.png")
                p = pygame.transform.scale(p, (p.get_width() * 5, p.get_height() * 5))
                self.imagesrun.append(p)

        self.image = self.imagestay
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.rect2 = self.colideimage.get_rect()
        self.rect2.midbottom = self.rect.midbottom
        self.up = False
        self.down = False
        self.righty = False
        self.left = False
        self.flip = False
        self.cadr = 1
        self.runimage = 1
        self.right = True
        if type != "polzun":
            self.rect2.y -= 10
        self.sloi = None
        self.hpcadr = 0
        self.type = type
        if type == None:
            self.speed = 2
        elif type == "runer":
            self.speed = 4
        else:
            self.speed = 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def uaap(self, playerx, playery, boxes):
        if not (
                playerx - self.rect2.x <= 20 and playerx - self.rect2.x >= -20) or (
                playerx - self.rect2.x <= 20 and playerx - self.rect2.x >= -20):

            if self.rect2.centerx > playerx:
                self.left = True
            else:
                self.left = False

            if self.rect2.centerx < playerx:
                self.righty = True
            else:
                self.righty = False

        if self.rect2.centery >= playery:
            self.up = True
        else:
            self.up = False
        if self.rect2.centery <= playery:
            self.down = True
        else:
            self.down = False

        if self.righty == True:
            self.rect.x += self.speed
            self.rect2.x += self.speed
            for box in boxes:
                if pygame.Rect.colliderect(self.rect2, box.rect2):
                    self.rect.x -= self.speed
                    self.rect2.x -= self.speed

            self.right = True
        if self.left == True:
            self.rect.x -= self.speed
            self.rect2.x -= self.speed
            self.right = False
            for box in boxes:
                if pygame.Rect.colliderect(self.rect2, box.rect2):
                    self.rect.x += self.speed
                    self.rect2.x += self.speed


        if self.up == True:
            self.rect.y -= self.speed
            self.rect2.y -= self.speed

            for box in boxes:
                if pygame.Rect.colliderect(self.rect2, box.rect2):
                    self.rect.y += self.speed
                    self.rect2.y += self.speed

        if self.down == True:
            self.rect.y += self.speed
            self.rect2.y += self.speed

            for box in boxes:
                if pygame.Rect.colliderect(self.rect, box.rect2):
                    self.rect.y -= self.speed
                    self.rect2.y -= self.speed


        if self.righty == False and self.left == False and self.up == False and self.down == False:
            self.image = self.imagestay
            self.runimage = 1

            if self.right == False:
                self.image = pygame.transform.flip(self.image, True, False)

        else:
            self.cadr += 1
            if self.cadr >= 8:
                self.image = self.imagesrun[self.runimage]
                self.runimage += 1
                if self.type != "polzun":
                    if self.runimage >= 12:
                        self.runimage = 1
                else:
                    if self.runimage >= 5:
                        self.runimage = 1
                self.cadr = 0
                if self.right == False:
                    self.image = pygame.transform.flip(self.image, True, False)

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