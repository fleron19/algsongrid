import pygame
from pygame.locals import *

COLORS = {'empty': (255, 255, 255),
          'wall': (122, 122, 122),
          'path': (58, 168, 50),
          'outline':  (0, 0, 0)
          }
class Cell():
    def __init__(self, state='empty', pos=(200, 200), size=10):
        self.state = state
        self.pos = pos
        self.size = size
        self.cell_rect = Rect(self.pos, (self.size, self.size))
        self.outline_rect = Rect(self.pos, (self.size, self.size))
    def render(self, win):
        pygame.draw.rect(win, COLORS[self.state], self.cell_rect)
        pygame.draw.rect(win, COLORS['outline'], self.outline_rect, 1)
    def clicked(self):
        if self.state == 'wall':
            self.state = 'empty'
        elif self.state == 'empty':
            self.state = 'wall'
class Field():
    def __init__(self, width=10, height=10, cell_size=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size + 1 # adding 1 to compensate outlines
        self.cells = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                position = (x * self.cell_size - 1 * x, y * self.cell_size - 1 * y) # making equal grid width
                row.append(Cell(pos=position, size=self.cell_size))
            self.cells.append(row)
    def render_cells(self, win):
        for row in self.cells:
            for cell in row:
                cell.render(win)

if __name__ == "__main__":
    window = pygame.display.set_mode((1920, 1080))
    window.fill(COLORS['empty'])
    pygame.init()
    field = Field(cell_size=120, width=16, height=9)
    field.render_cells(window)
    run = True
    simulation = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for row in field.cells:
                    for cell in row:
                        if cell.cell_rect.collidepoint(event.pos):
                            cell.clicked()
            field.render_cells(window)
        pygame.display.update()




pygame.quit()