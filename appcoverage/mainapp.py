import time
import pygame
import easygui
import os


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


# этот класс отвечает за надпись девиза
class Motto(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((760, 40))
        self.image.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text = font.render('We are like a Swiss knife for any online meeting', False, (0, 0, 0))
        self.recttext = text.get_rect()
        self.recttext.x = 0
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


# этот класс отвечает за надпись функции замены видео
class Videochangetitle(pygame.sprite.Sprite):
    def __init__(self, x, y, widthsurf):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, 50))
        self.image.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text = font.render('Video change', False, (0, 0, 0))
        self.recttext = text.get_rect()
        self.recttext.x = 0
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


# этот класс отвечает за надпись функции поиска контрольного слова
class Wordtitle(pygame.sprite.Sprite):
    def __init__(self, x, y, widthsurf):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((widthsurf, 50))
        self.image.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text = font.render('Сheckword', False, (0, 0, 0))
        self.recttext = text.get_rect()
        self.recttext.x = 0
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


# этот класс отвечает за надпись функции выбора фильтров
class Filterstitle(pygame.sprite.Sprite):
    def __init__(self, x, y, widthsurf):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((widthsurf, 50))
        self.image.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text = font.render('Filters', False, (0, 0, 0))
        self.recttext = text.get_rect()
        self.recttext.x = 0
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


class Recordnowbutton(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        # создаём поверхность для кнопки чтобы она была как спрайт
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))

        # рисуем на этой поверхности текст и кнопку !!!! учти что когда мы рисуем на поверхности
        # кординаты учитываются относительно аоверхности а не относительно всего экрана !!!!!
        pygame.draw.rect(self.image, (0, 179, 255), [0, 0, width, height], border_radius=50)
        # рисуем текст
        font = pygame.font.Font(None, 36)
        text = font.render('Record now', True, (255, 255, 255))
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


class Selectvideobutton(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        # создаём поверхность для кнопки чтобы она была как спрайт
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))

        # рисуем на этой поверхности текст и кнопку !!!! учти что когда мы рисуем на поверхности
        # кординаты учитываются относительно аоверхности а не относительно всего экрана !!!!!
        pygame.draw.rect(self.image, (0, 179, 255), [0, 0, width, height], border_radius=50)
        # рисуем текст
        font = pygame.font.Font(None, 36)
        text = font.render('Select video', True, (255, 255, 255))
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


class Filename(pygame.sprite.Sprite):
    def __init__(self, x, y, widthsurf):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((widthsurf, 50))
        self.image.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        with open("path.txt", 'r') as file:
            road = file.read()
        text = font.render(road, False, (0, 0, 0))
        self.recttext = text.get_rect()
        self.recttext.x = 0
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

    def update(self):
        self.image.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        with open("path.txt", 'r') as file:
            road = file.read().split('/')
        if road[-1] == 'Nothing2':
            road[-1] = 'Nothing'
        text = font.render(road[-1], False, (0, 0, 0))
        self.recttext = text.get_rect()
        self.recttext.x = 0
        self.recttext.y = 0
        self.image.blit(text, self.recttext)


if __name__ == '__main__':
    pygame.init()
    sprite = []
    sprite_group = pygame.sprite.Group()

    # делает экран во всё окно
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
    motto = Motto(W // 2 - int(760 // 2), H - int(H * 0.4))
    widthvideochange = 225
    videochangetitle = Videochangetitle(W // 3 // 2 - int(225 / 2), 20, widthvideochange)
    videochangetitle.hide()
    widthword = 185
    checkwordtitle = Wordtitle(W // 3 // 2 - int(widthword / 2) + (W // 3), 20, widthword)
    checkwordtitle.hide()
    widthfilters = 100
    filterstitle = Filterstitle(W // 3 // 2 - int(widthword / 2) + (W // 3 * 2), 20, widthfilters)
    filterstitle.hide()

    recordbuttonwidth = int(W // 3 * 0.6)
    recordbuttonheight = int(H * 0.1)
    recordbutton = Recordnowbutton(W // 3 // 2 - recordbuttonwidth // 2, H * 0.1, recordbuttonwidth, recordbuttonheight)
    recordbutton.hide()

    selectbuttonwidth = int(W // 3 * 0.6)
    selectbuttonheight = int(H * 0.1)
    selectbutton = Selectvideobutton(W // 3 // 2 - selectbuttonwidth // 2, H * 0.3, selectbuttonwidth,
                                     selectbuttonheight)
    selectbutton.hide()

    filaenamedisplay = Filename(10, H * 0.4, W//3 - 10)
    filaenamedisplay.hide()

    # добавляем все спрайты в группу чтобы с ними было удобнее работать
    sprite.append(start)
    sprite_group.add(start)
    sprite.append(logo)
    sprite_group.add(logo)
    sprite.append(motto)
    sprite_group.add(motto)
    sprite.append(videochangetitle)
    sprite_group.add(videochangetitle)
    sprite.append(checkwordtitle)
    sprite_group.add(checkwordtitle)
    sprite.append(filterstitle)
    sprite_group.add(filterstitle)
    sprite.append(recordbutton)
    sprite_group.add(recordbutton)
    sprite.append(selectbutton)
    sprite_group.add(selectbutton)
    sprite.append(filaenamedisplay)
    sprite_group.add(filaenamedisplay)

    flag_not_main_window = False
    while running:
        screen.fill((255, 255, 255))
        # обновление статуса выбора файла
        filaenamedisplay.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if start.click_detection(pos[0], pos[1]):
                    start.hide()
                    logo.hide()
                    motto.hide()
                    videochangetitle.show()
                    checkwordtitle.show()
                    filterstitle.show()
                    flag_not_main_window = True
                    recordbutton.show()
                    selectbutton.show()
                    filaenamedisplay.show()
                if recordbutton.click_detection(pos[0], pos[1]):
                    os.system('python file_selection.py')
                if selectbutton.click_detection(pos[0], pos[1]):
                    os.system('python file_selection.py')
                    with open("path.txt", 'r') as pat:
                        text = pat.read()
                    while text == 'Nothing':
                        with open("path.txt", 'r') as pat:
                            text = pat.read()
            if event.type == pygame.QUIT:
                running = False
        clock.tick(fps)
        sprite_group.update()
        sprite_group.draw(screen)
        for sp in sprite:
            screen.blit(sp.image, sp.rect)
        if flag_not_main_window:
            pygame.draw.line(screen, (0, 0, 0), (W // 3, 0), (W // 3, H))
            pygame.draw.line(screen, (0, 0, 0), (W // 3 * 2, 0), (W // 3 * 2, H))
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
