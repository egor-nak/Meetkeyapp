import time
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text, pos, font, bg="black", feedback="bye"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(button.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode()
    size = width, height = screen.get_size()
    running = True
    v = 20
    fps = 60
    clock = pygame.time.Clock()
    # button = Button("hi", (200, 200), 100)
    flag = False
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = True
                coords = event.pos
                size = 20
                pygame.draw.circle(screen, (255, 255, 0), coords, size)
            if event.type == pygame.QUIT:
                running = False
        # button.show()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
