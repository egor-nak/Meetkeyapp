# Когда будешь форматировать в приложение замени все пути в приложении вместо абсолютных на пути из Content Root!!!!!!!

import time
import pygame
import easygui
import os
from threading import Thread
import imageio


class Title(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height=50, writ=''):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text = font.render(writ, False, (0, 0, 0))
        self.recttext = text.get_rect()
        self.recttext.x = 0
        self.recttext.y = 0
        self.image.blit(text, self.recttext)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_initial = x
        self.y_initial = y

    def show(self):
        self.rect.x = self.x_initial
        self.rect.y = self.y_initial

    def hide(self):
        self.rect.x = -100000


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
        self.x_initial = x
        self.y_initial = y

    def show(self):
        self.rect.x = self.x_initial
        self.rect.y = self.y_initial

    def hide(self):
        self.rect.x = -10000




class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text):
        pygame.sprite.Sprite.__init__(self)

        # создаём поверхность для кнопки чтобы она была как спрайт
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))

        # рисуем на этой поверхности текст и кнопку !!!! учти что когда мы рисуем на поверхности
        # кординаты учитываются относительно аоверхности а не относительно всего экрана !!!!!
        pygame.draw.rect(self.image, (0, 179, 255), [0, 0, width, height], border_radius=50)
        # рисуем текст
        font = pygame.font.Font(None, 36)
        text = font.render(text, True, (255, 255, 255))
        self.recttext = text.get_rect()
        self.recttext.x = width // 2 - (self.recttext.width // 2)
        self.recttext.y = height // 2 - (self.recttext.height // 2)
        self.image.blit(text, self.recttext)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.x_initial = x
        self.y_initial = y

    def show(self):
        self.rect.x = self.x_initial
        self.rect.y = self.y_initial

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
        self.x_initial = x
        self.y_initial = y

    def show(self):
        self.rect.x = self.x_initial
        self.rect.y = self.y_initial

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


class InputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font_size, text=''):
        pygame.sprite.Sprite.__init__(self)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.color_inactive
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.image = self.font.render(text, True, self.color)
        self.active = False
        self.x_initial = x
        self.y_initial = y

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # with open("checkword.txt", 'w') as file:
                    #     file.write(self.text)
                    print(self.text)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.image = self.font.render(self.text, True, self.color)

    def size_correction(self):
        # Resize the box if the text is too long.
        width = max(200, self.image.get_width() + 10)
        self.rect.w = width

    def special_show(self, screen):
        # Blit the text.
        screen.blit(self.image, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def show(self):
        self.rect.x = self.x_initial
        self.rect.y = self.y_initial

    def hide(self):
        self.rect.x = -100000




pygame.init()
sprite = []
sprite_with_special_show = []
sprite_group = pygame.sprite.Group()

# делает экран во всё окно
screen = pygame.display.set_mode()
W, H = screen.get_size()
size = width, height = screen.get_size()
running = True
fps = 60
clock = pygame.time.Clock()

# создаём все спрайты
start = Button(W // 2 - int(W * 0.12), H - int(H * 0.3), int(W * 0.24), int(H * 0.1), 'Start')
logowidth = 300
logoheight = 200
logo = Logo(W // 2 - int(logowidth * 0.4), logoheight * 0.6, logowidth, logoheight)
motto = Title(W // 2 - int(760 // 2), H - int(H * 0.4), 760, height=40, writ='We are like a Swiss knife for any online meeting')
widthvideochange = 225
videochangetitle = Title(W // 3 // 2 - int(225 / 2), 20, widthvideochange, writ='Video change')
videochangetitle.hide()
widthword = 185
checkwordtitle = Title(W // 3 // 2 - int(widthword / 2) + (W // 3), 20, widthword, writ='Check word')
checkwordtitle.hide()
widthfilters = 100
filterstitle = Title(W // 3 // 2 - int(widthword / 2) + (W // 3 * 2), 20, widthfilters, writ='Filters')
filterstitle.hide()

recordbuttonwidth = int(W // 3 * 0.6)
recordbuttonheight = int(H * 0.1)
recordbutton = Button(W // 3 // 2 - recordbuttonwidth // 2, H * 0.1, recordbuttonwidth, recordbuttonheight, 'Record now')
recordbutton.hide()

selectbuttonwidth = int(W // 3 * 0.6)
selectbuttonheight = int(H * 0.1)
selectbutton = Button(W // 3 // 2 - selectbuttonwidth // 2, H * 0.3, selectbuttonwidth,
                                 selectbuttonheight, 'Select video')
selectbutton.hide()

filaenamedisplay = Filename(10, H * 0.4, W // 3 - 10)
filaenamedisplay.hide()


checkword_input_width = int(W // 3 * 0.6)
checkword_input_height = int(H * 0.05)
checkword_input = InputBox(W // 3 // 2 - checkword_input_width // 2 + (W // 3), H * 0.1, checkword_input_width, checkword_input_height, 32)
checkword_input.hide()


applybuttonwidth = int(W // 3 * 0.6)
applybuttonheight = int(H * 0.1)
applybutton = Button(W // 3 // 2 - applybuttonwidth // 2 + W // 3, H * 0.3, applybuttonwidth,
                                 applybuttonheight, 'Apply checkword')
applybutton.hide()

filter_input_width = int(W // 3 * 0.6)
filter_input_height = int(H * 0.05)
filter_input = InputBox(W // 3 // 2 - checkword_input_width // 2 + (W // 3 * 2), H * 0.1, filter_input_width, filter_input_height, 32)
filter_input.hide()

applybuttonwidth_filter = int(W // 3 * 0.6)
applybuttonheight_filter = int(H * 0.1)
applybutton_filter = Button(W // 3 // 2 - applybuttonwidth // 2 + (W // 3 * 2), H * 0.3, applybuttonwidth_filter,
                                 applybuttonheight_filter, 'Apply filter')
applybutton_filter.hide()


startdetectionbuttonwidth = int(W // 3 * 0.6)
startdetectionbuttonheight = int(H * 0.1)
startdetectionbutton = Button(W // 3 // 2 - applybuttonwidth // 2 + W // 3, H * 0.5, startdetectionbuttonwidth,
                                 startdetectionbuttonheight, 'Start detection')
startdetectionbutton.hide()


enddetectionbuttonwidth = int(W // 3 * 0.6)
enddetectionbuttonheight = int(H * 0.1)
enddetectionbutton = Button(W // 3 // 2 - applybuttonwidth // 2 + W // 3, H * 0.7, enddetectionbuttonwidth,
                                 enddetectionbuttonheight, 'End detection')
enddetectionbutton.hide()




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
sprite_group.add(checkword_input)
sprite_with_special_show.append(checkword_input)
sprite_group.add(applybutton)
sprite.append(applybutton)
sprite_group.add(filter_input)
sprite_with_special_show.append(filter_input)
sprite_group.add(applybutton_filter)
sprite.append(applybutton_filter)
sprite_group.add(startdetectionbutton)
sprite.append(startdetectionbutton)
sprite_group.add(enddetectionbutton)
sprite.append(enddetectionbutton)



flag_not_main_window = False
while running:
    with open('stopall.txt', 'r') as file:
        if file.read() == 'Yes':
            pygame.quit()
            exit()
    screen.fill((255, 255, 255))
    # обновление статуса выбора файла
    filaenamedisplay.update()
    checkword_input.size_correction()
    for event in pygame.event.get():
        checkword_input.check_event(event)
        filter_input.check_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if start.click_detection(pos[0], pos[1]):
                with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/canstart.txt',
                          'w') as file:
                    file.write('Yes')
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
                checkword_input.show()
                applybutton.show()
                filter_input.show()
                applybutton_filter.show()
                startdetectionbutton.show()
                enddetectionbutton.show()
            if recordbutton.click_detection(pos[0], pos[1]):
                os.system(
                    'python /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/video_recording.py')
                with open("path.txt", 'w') as file:
                    file.write(
                        f"/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/cam_video_meetkey.avi")
            if selectbutton.click_detection(pos[0], pos[1]):
                os.system('python file_selection.py')
                with open("path.txt", 'r') as pat:
                    text = pat.read()
                while text == 'Nothing':
                    with open("path.txt", 'r') as pat:
                        text = pat.read()
            if applybutton.click_detection(pos[0], pos[1]):
                with open("checkword.txt", 'w') as pat:
                    if checkword_input.text != '':
                        pat.write(checkword_input.text)
                    else:
                        pat.write('Nothing223')
            if applybutton_filter.click_detection(pos[0], pos[1]):
                with open("/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/filtername.txt", 'w') as pat:
                    if filter_input.text != '':
                        pat.write(filter_input.text)
                    else:
                        pat.write('Nothing223')
            if startdetectionbutton.click_detection(pos[0], pos[1]):
                with open("/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/canfindcheckword.txt", 'w') as pat:
                    pat.write('Yes')
            if enddetectionbutton.click_detection(pos[0], pos[1]):
                with open("/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/canfindcheckword.txt", 'w') as pat:
                    pat.write('No')
        if event.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    sprite_group.update()
    # sprite_group.draw(screen)
    for sp in sprite:
        screen.blit(sp.image, sp.rect)
    for sp in sprite_with_special_show:
        sp.special_show(screen)
    if flag_not_main_window:
        pygame.draw.line(screen, (0, 0, 0), (W // 3, 0), (W // 3, H))
        pygame.draw.line(screen, (0, 0, 0), (W // 3 * 2, 0), (W // 3 * 2, H))
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
with open('stopall.txt', 'w') as file:
    file.write('Yes')