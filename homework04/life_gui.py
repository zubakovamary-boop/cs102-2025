import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)

    def draw_lines(self) -> None:
        """нарисовать сетку поля"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (x, 0), (x, self.height)
            )
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (0, y), (self.width, y)
            )

    def draw_grid(self) -> None:
        """нарисовать сетку с закрашенными клетками относительно их состояния"""
        alive = pygame.Color("green")
        dead = pygame.Color("black")
        for y in range(self.cell_height):
            for x in range(self.cell_width):
                left = x * self.cell_size
                top = y * self.cell_size
                size = self.cell_size
                rect = (left, top, size, size)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, alive, rect)
                else:
                    pygame.draw.rect(self.screen, dead, rect)

    def run(self) -> None:
        """запуск игры"""
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == 256:
                    running = False
                elif event.type == 768:
                    if event.key == 32:
                        self.paused = not self.paused
                elif event.type == 1025 and self.paused:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    grid_x = x // self.cell_size
                    grid_y = y // self.cell_size
                    if 0 <= grid_x < self.cell_width and 0 <= grid_y < self.cell_height:
                        current = self.grid[grid_y][grid_x]
                        self.grid[grid_y][grid_x] = 1 - current
            self.screen.fill(pygame.Color("white"))
            self.draw_grid()
            self.draw_lines()
            if not self.paused:
                self.life.step()
                self.grid = self.life.curr_generation
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
