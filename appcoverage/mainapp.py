import time
import pygame


# класс который отвечает за кнопку начала
class Startbutton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        height = int(H * 0.1)
        width = int(W * 0.24)

        # создаём поверхность для кнопки чтобы она была как спрайт
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))

        # рисуем на этой поверхности текст и кнопку !!!! учти что когда мы рисуем на поверхности
        # кординаты учитываются относительно аоверхности а не относительно всего экрана !!!!!
        pygame.draw.rect(self.image, (0, 179, 255), [0, 0, width, height], border_radius=50)
        # рисуем текст
        font = pygame.font.Font(None, 36)
        text = font.render('Start', True, (255, 255, 255))
        self.recttext = text.get_rect()
        self.recttext.x = width // 2 - (self.recttext.width // 2)
        self.recttext.y = height // 2 - (self.recttext.height // 2)
        self.image.blit(text, self.recttext)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def show(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def hide(self):
        self.rect.x = -1000
        self.rect.y = -1000

    #  проверка нажатия
    def click_detection(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.width) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.height):
            return True
        else:
            return False


# класс который отвечает за логотип
class Logo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'images/logo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def show(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def hide(self):
        self.rect.x = -10000


class Motto(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1000, 50))
        self.image.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text = font.render('We are like a Swiss knife for any online meeting', False, (0, 0, 0))
        self.recttext = text.get_rect()
        self.recttext.x = 200
        self.recttext.y = 0
        self.image.blit(text, self.recttext)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def show(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def hide(self):
        self.rect.x = -100000


if __name__ == '__main__':
    pygame.init()
    sprite = []
    sprite_group = pygame.sprite.Group()
    screen = pygame.display.set_mode()
    W, H = screen.get_size()
    size = width, height = screen.get_size()
    running = True
    fps = 60
    clock = pygame.time.Clock()

    # создаём все спрайты
    start = Startbutton(W // 2 - int(W * 0.12), H - int(H * 0.3))
    logowidth = 300
    logoheight = 200
    logo = Logo(W // 2 - int(logowidth * 0.4), logoheight * 0.6, logowidth, logoheight)
    motto = Motto(W // 2 - int(560), H - int(H * 0.4))

    # добавляем все спрайты в группу чтобы с ними было удобнее работать
    sprite.append(start)
    sprite_group.add(start)
    sprite.append(logo)
    sprite_group.add(logo)
    sprite.append(motto)
    sprite_group.add(motto)

    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if start.click_detection(pos[0], pos[1]):
                    start.hide()
                    logo.hide()
                    motto.hide()
            if event.type == pygame.QUIT:
                running = False
        clock.tick(fps)
        sprite_group.update()
        sprite_group.draw(screen)
        for sp in sprite:
            screen.blit(sp.image, sp.rect)
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
