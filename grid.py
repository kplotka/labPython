import pygame

class Grid:
    def __init__(self, rows, cols, row_hints, col_hints):
        self.rows = rows
        self.cols = cols
        self.row_hints = row_hints
        self.col_hints = col_hints
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        self.cell_size = min(
            (900 - 200) // cols,
            (700 - 200) // rows,
        )
        self.cell_size = max(15, min(self.cell_size, 40))

        self.offset_x = 100 + max(len(h) for h in row_hints) * 20
        self.offset_y = 100 + max(len(h) for h in col_hints) * 20

    def draw(self, screen):
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(
                    self.offset_x + x * self.cell_size,
                    self.offset_y + y * self.cell_size,
                    self.cell_size, self.cell_size
                )

                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, (0, 0, 0), rect)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), rect)
                    if self.grid[y][x] == 2:
                        pygame.draw.line(screen, (255, 0, 0),
                                         (rect.left + 5, rect.top + 5),
                                         (rect.right - 5, rect.bottom - 5), 2)
                        pygame.draw.line(screen, (255, 0, 0),
                                         (rect.right - 5, rect.top + 5),
                                         (rect.left + 5, rect.bottom - 5), 2)

                pygame.draw.rect(screen, (0, 0, 0), rect, 1)

        self.draw_hints(screen)

    def draw_hints(self, screen):
        font = pygame.font.SysFont("arial", 18)
        for i, hints in enumerate(self.row_hints):
            for j, hint in enumerate(reversed(hints)):
                screen.blit(font.render(str(hint), True, (0, 0, 0)), (
                    self.offset_x - (j + 1) * 20,
                    self.offset_y + i * self.cell_size + self.cell_size // 4
                ))

        for i, hints in enumerate(self.col_hints):
            for j, hint in enumerate(reversed(hints)):
                screen.blit(font.render(str(hint), True, (0, 0, 0)), (
                    self.offset_x + i * self.cell_size + self.cell_size // 4,
                    self.offset_y - (j + 1) * 20
                ))

    def toggle_cell(self, row, col, right_click=False):
        if right_click:
            self.grid[row][col] = 2 if self.grid[row][col] != 2 else 0
        else:
            self.grid[row][col] = (self.grid[row][col] + 1) % 2

    def is_correct(self, solution):
        return all(
            (cell == 1 if sol == 1 else cell != 1)
            for row, sol_row in zip(self.grid, solution)
            for cell, sol in zip(row, sol_row)
        )