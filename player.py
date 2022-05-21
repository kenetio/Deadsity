import pygame.sprite
import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagestay = pygame.image.load(r"images/player/run/run1.png")
        self.imagestay = pygame.transform.scale(self.imagestay, (self.imagestay.get_width() * 5, self.imagestay.get_height() * 5))

        self.colideimage = pygame.image.load(r"images/player/colideimage.png")
        self.colideimage = pygame.transform.scale(self.colideimage,
                                                (self.colideimage.get_width() * 5, self.colideimage.get_height() * 5))

        self.imagesrun = []
        p = r"images/player/run/run [].png"
        for i in range (16):
            p = pygame.image.load(f"images/player/run/run{i + 1}.png")
            p = pygame.transform.scale(p, (p.get_width() * 5, p.get_height()*5))
            self.imagesrun.append(p)

        self.imagestaynoarm = pygame.image.load(r"images/player/run/run no arm1.png")
        self.imagestaynoarm = pygame.transform.scale(self.imagestaynoarm,
                                                (self.imagestaynoarm.get_width() * 5, self.imagestaynoarm.get_height() * 5))
        self.noarmrunimages = []
        p = r"images/player/run/run 1 arm 1.png"
        for d in range(16):
            p = pygame.image.load(f"images/player/run/run no arm{d + 1}.png")
            p = pygame.transform.scale(p, (p.get_width() * 5, p.get_height() * 5))
            self.noarmrunimages.append(p)

        self.right = True
        self.image = self.imagestay
        self.rect = self.image.get_rect()
        self.rect2 = self.colideimage.get_rect()
        surface = pygame.display.get_surface()
        self.rect.center = surface.get_rect().center
        self.rect2.midbottom = self.rect.midbottom
        self.rect2.y -= 10
        self.up = False
        self.down = False
        self.righty = False
        self.left = False
        self.flip = False
        self.cadr = 1
        self.runimage = 1
        self.arm = None
        self.hp = 100
        self.eat = 100
        self.trink = 100
        self.eatcadr = 0
        self.trinkcadr = 0
        self.l = False
        self.r = False
        self.u = False
        self.d = False
        self.upf = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, move=None):
        if move != None:
            if move == "right":
                self.righty = True
            if move == "rightn":
                self.righty = False
                self.r = False
            if move == "left":
                self.left = True
            if move == "leftn":
                self.left = False
                self.l = False

            if move == "up":
                self.up = True
            if move == "upn":
                self.up = False
                self.u = False
            if move == "down":
                self.down = True
            if move == "downn":
                self.down = False
                self.d = False




    def uaap(self, arm, boxes):
        if self.righty == True:
            if self.eat and self.trink >= 40:
                self.rect.x += 5
                self.rect2.x += 5
                for box in boxes:
                    if not pygame.Rect.colliderect(self.rect2, box.rect2):
                        self.r = True
                    else:
                        self.r = False
                self.rect.x -= 5
                self.rect2.x -= 5
            else:
                self.rect.x += 3
                self.rect2.x += 3
                for box in boxes:
                    if not pygame.Rect.colliderect(self.rect2, box.rect2):
                        self.r = True
                    else:
                        self.r = False
                self.rect.x -= 3
                self.rect2.x -= 3
            self.right = True
        if self.left == True:
            if self.eat and self.trink >= 40:
                self.rect.x -= 5
                self.rect2.x -= 5
                for box in boxes:
                    if not pygame.Rect.colliderect(self.rect2, box.rect2):
                        self.l = True
                    else:
                        self.l = False
                self.rect.x += 5
                self.rect2.x += 5
            else:
                self.rect.x -= 3
                self.rect2.x -= 3
                for box in boxes:
                    if not pygame.Rect.colliderect(self.rect2, box.rect2):
                        self.l = True
                    else:
                        self.l = False
                self.rect.x += 3
                self.rect2.x += 3
            self.right = False
        if self.up == True:
            if self.eat and self.trink >= 40:
                self.rect.y -= 5
                self.rect2.y -= 5
                for box in boxes:
                    if not pygame.Rect.colliderect(self.rect2, box.rect2):
                        self.u = True
                    else:
                        self.u = False
                self.rect.y += 5
                self.rect2.y += 5
            else:
                self.rect.y -= 3
                self.rect2.y -= 3
                for box in boxes:
                    if not pygame.Rect.colliderect(self.rect2, box.rect2):
                        self.u = True
                    else:
                        self.u = False
                self.rect.y += 3
                self.rect2.y += 3
        if self.down == True:
            if self.eat and self.trink >= 40:
                self.rect.y += 5
                self.rect2.y += 5
                for box in boxes:
                    if not pygame.Rect.colliderect(self.rect2, box.rect2):
                        self.d = True
                    else:
                        self.d = False
                self.rect.y -= 5
                self.rect2.y -= 5
            else:
                self.rect.y += 3
                self.rect2.y += 3
                for box in boxes:
                    if not pygame.Rect.colliderect(self.rect2, box.rect2):
                        self.d = True
                    else:
                        self.d = False
                self.rect.y -= 3
                self.rect2.y -= 3

        if self.righty == True or self.left == True or self.up == True or self.down == True:
            self.eatcadr += 1
            self.trinkcadr += 1
            if self.eatcadr >= 300:
                self.eat -= 1
                self.eatcadr = 0
            if self.trinkcadr >= 300:
                self.trink -= 1
                self.trinkcadr = 0

        self.arm = arm


        if self.righty == False and self.left == False and self.up == False and self.down == False:
            if self.arm != None:
                self.image = self.imagestaynoarm
            else:
                self.image = self.imagestay
            self.runimage = 1
            mousex, mousey = pygame.mouse.get_pos()
            if mousex >= self.rect.centerx:
                self.right = True
            else:
                self.right = False

            if self.right == False:
                self.image = pygame.transform.flip(self.image, True, False)

        else:
            self.cadr += 1
            if self.cadr >= 5:

                if self.arm != None:
                    self.image = self.noarmrunimages[self.runimage]
                    self.runimage += 1
                    if self.runimage >= 16:
                        self.runimage = 1
                else:
                    self.image = self.imagesrun[self.runimage]
                    self.runimage += 1
                    if self.runimage >= 16:
                        self.runimage = 1

                self.cadr = 0
                if self.right == False:
                    self.image = pygame.transform.flip(self.image, True, False)


        if self.eat and self.trink >= 40:
            self.upf = True
        else:
            self.upf = False


class Arm(pygame.sprite.Sprite):
    def __init__(self, image, coords, id):
        super().__init__()
        self.image = pygame.transform.scale(image,
                                                (image.get_width() * 5, image.get_height() * 5))
        self.newimage = pygame.transform.scale(image,
                                            (image.get_width() * 5, image.get_height() * 5))
        self.rect = self.newimage.get_rect()
        self.rect.center = coords
        self.id = id
        self.right = False
        self.oldr = False
        self.angle = 90

    def draw(self, surface):
        surface.blit(self.newimage, self.rect)

    def update(self):

        mousex, mousey = pygame.mouse.get_pos()
        if mousex >= self.rect.centerx:
            self.right = True
        else:
            self.right = False

        if self.right == False and self.oldr == True:
            #self.newimage = pygame.transform.flip(self.newimage, True, False)
            self.oldr = False
        elif self.right == True and self.oldr == False:
            #self.newimage = pygame.transform.flip(self.newimage, True, False)
            self.oldr = True

        rel_x, rel_y = mousex - self.rect.x, mousey - self.rect.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.angle -= angle
        if self.angle >= 360:
            self.angle -= 360
        if self.angle >= -360:
            self.angle -= -360
        self.newimage = pygame.transform.rotate(self.image, angle-180)











