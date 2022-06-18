import pygame
import sys
from player import Player, Arm
from item import Item
from zombie import Zombie
from box import Box
from tile import Tile
from random import randint

pygame.init()

# Константы/Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dead city")
clock = pygame.time.Clock()

pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def main():
    # Спрайты/Sprites

    pitems = []
    player = Player()
    items = pygame.sprite.Group()
    zombies = pygame.sprite.Group()
    boxes = pygame.sprite.Group()
    pistol = Item(pygame.image.load("images/predmeti/Uzi.png"), (-100, 100), "pistol")
    items.add(pistol)
    arm = None
    font = pygame.font.Font(r"OutlinePixel7.ttf", 72)
    cadrhp = 0
    cadreat = 0
    cadrtrink = 0
    cursor_shot = pygame.image.load(r"images/cursor.png")
    cursor_shot = pygame.transform.scale(cursor_shot,
                                         (cursor_shot.get_width() * 2, cursor_shot.get_height() * 2))
    cursor_shot_rect = cursor_shot.get_rect()
    box = Box(pygame.image.load(r"images/box3.png"), (1221, 543), "box")
    boxes.add(box)
    zcadr = 0


    running = True
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)

        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update("up")
                if event.key == pygame.K_d:
                    player.update("right")
                if event.key == pygame.K_s:
                    player.update("down")
                if event.key == pygame.K_a:
                    player.update('left')
                if event.key == pygame.K_c:
                    for item in items:
                        if (player.rect2.centerx - item.rect.centerx <= 70 and player.rect2.centerx - item.rect.centerx >= -70) and (player.rect2.centery - item.rect.centery <= 70 and player.rect2.centery - item.rect.centery >= -70):
                            if item.id == "pistol":
                                arm = item.id
                            if item.id == "bread":
                                arm = item.id
                            item.kill()
                if event.key == pygame.K_z and arm != None:
                    arm = None
                    pitems.append(player.arm)



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.update("upn")
                if event.key == pygame.K_d:
                    player.update("rightn")
                if event.key == pygame.K_s:
                    player.update("downn")
                if event.key == pygame.K_a:
                    player.update('leftn')

        for zombie in zombies:
            if (
                    player.rect2.centerx - zombie.rect2.centerx <= 700 and player.rect2.centerx - zombie.rect2.centerx >= -700) and (
                    player.rect2.centery - zombie.rect2.centery <= 700 and player.rect2.centery - zombie.rect2.centery >= -700):

                if zombie.type != "polzun":

                    if pygame.Rect.colliderect(player.rect2, zombie.rect2) and (
                        player.rect2.y - zombie.rect2.y <= 5 and player.rect2.y - zombie.rect2.y >= -5) and (
                        player.rect2.y - zombie.rect2.y <= 5 and player.rect2.y - zombie.rect2.y >= -5):
                        if zombie.hpcadr >= 20:
                            player.hp -= 15
                            zombie.hpcadr = 0
                    else:
                        zombie.uaap(player.rect2.centerx, player.rect2.centery, boxes)

                else:
                    if pygame.Rect.colliderect(player.rect2, zombie.rect2) :
                        if zombie.hpcadr >= 20:
                            player.hp -= 15
                            zombie.hpcadr = 0
                    else:
                        zombie.uaap(player.rect2.centerx, player.rect2.centery, boxes)
            else:
                zombie.image = zombie.imagestay

        if arm != player.arm:
            playerarm = Arm(pygame.image.load(r"images/player/arms/arm with uzi.png"), (960, 520), "Uzi")

        i = 0
        while len(zombies) <= 1000 and i <= 10:
            zx = randint(-5000, 20000)
            zy = randint(-3000, 17000)

            if (
                    abs(player.rect2.centerx - zx) >= 1080 and
                    abs(player.rect2.centery - zy) >= 750):

                type = randint(1, 10)
                if type >= 9:
                    type = "polzun"
                elif type >= 7:
                    type = "runer"
                else:
                    type = None


                zombie = Zombie((zx, zy), type)
                zombies.add(zombie)
                zcadr = 0
                i += 1


        # Рендеринг/Rendering
        screen.fill((167, 201, 176))
        items.draw(screen)
        boxes.draw(screen)
        zombies.draw(screen)
        player.draw(screen)
        if player.arm == "pistol":
            playerarm.draw(screen)
        text = font.render(
            (str(player.hp) + "%"), True, (0, 0, 0))
        screen.blit(text, (1700, 25))
        text = font.render(
            (str(player.eat) + "%"), True, (0, 0, 0))
        screen.blit(text, (1700, 100))
        text = font.render(
            (str(player.trink) + "%"), True, (0, 0, 0))
        screen.blit(text, (1700, 175))
        if player.hp >= 76:
            image = pygame.image.load(r"images/heart/heart 1.png")
            image = pygame.transform.scale(image, (image.get_width()*4, image.get_height()*4))
            screen.blit(image, (1625, 30))
        elif player.hp >= 51:
            image = pygame.image.load(r"images/heart/heart 2.png")
            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            screen.blit(image, (1625, 30))
        elif player.hp >= 26:
            image = pygame.image.load(r"images/heart/heart 3.png")
            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            screen.blit(image, (1625, 30))
        else:
            image = pygame.image.load(r"images/heart/heart 4.png")
            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            screen.blit(image, (1625, 30))


        if player.eat >= 76:
            image = pygame.image.load(r"images/hunger/hunger 1.png")
            image = pygame.transform.scale(image, (image.get_width()*4, image.get_height()*4))
            screen.blit(image, (1625, 105))
        elif player.eat >= 51:
            image = pygame.image.load(r"images/hunger/hunger 2.png")
            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            screen.blit(image, (1625, 105))
        elif player.eat >= 26:
            image = pygame.image.load(r"images/hunger/hunger 3.png")
            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            screen.blit(image, (1625, 105))
        else:
            image = pygame.image.load(r"images/hunger/hunger 4.png")
            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            screen.blit(image, (1625, 105))


        if player.trink >= 76:
            image = pygame.image.load(r"images/drink/drink 1.png")
            image = pygame.transform.scale(image, (image.get_width()*4, image.get_height()*4))
            screen.blit(image, (1625, 180))
        elif player.trink >= 51:
            image = pygame.image.load(r"images/drink/drink 2.png")
            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            screen.blit(image, (1625, 180))
        elif player.trink >= 26:
            image = pygame.image.load(r"images/drink/drink 3.png")
            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            screen.blit(image, (1625, 180))
        else:
            image = pygame.image.load(r"images/drink/drink 4.png")
            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            screen.blit(image, (1625, 180))



        if player.arm == "pistol":
            pygame.mouse.set_visible(False)
            cursor_shot_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor_shot, cursor_shot_rect)
        else:
            pygame.mouse.set_visible(True)

        # Обновление спрайтов/Updating sprites
        if player.arm == "pistol":
            playerarm.update(player.right, player.runimage)

        player.uaap(arm, boxes)
        for item in items:
            item.move(player.r, player.l, player.u, player.d, player.upf)
        for box in boxes:
            box.move(player.r, player.l, player.u, player.d, player.upf)
        for zombie in zombies:
            zombie.move(player.r, player.l, player.u, player.d, player.upf)

        # Обновление экрана/Screen Refresh
        pygame.display.update()

        cadrhp += 1
        for zombie in zombies:
            zombie.hpcadr += 1
        cadreat += 1
        if cadreat >= 1000:
            player.eat -= 1
            cadreat = 0
        cadrtrink += 1
        if cadrtrink >= 1000:
            player.trink -= 1
            cadrtrink = 0

        if player.eat <= 20 or player.trink <= 20:
            if cadrhp >= 1000:
                player.hp -= 2
                cadrhp = 0



        if player.hp <= 0:
            running = False
            gameover()
        if player.eat <= 0:
            running = False
            gameover()
        if player.trink <= 0:
            running = False
            gameover()

def gameover():
    # Спрайты/Sprites

    background = pygame.image.load(r"images/Background.png")
    button = pygame.image.load(r"images/restartb.png")
    rect = button.get_rect()
    rect.topleft = (800, 700)
    pygame.mouse.set_visible(True)

    running = True
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)

        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    main()


        # Рендеринг/Rendering
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(button, (800, 700))


        # Обновление экрана/Screen Refresh
        pygame.display.update()



if __name__ == "__main__":
    main()
