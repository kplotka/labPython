import pygame
from puzzle import load_puzzle
from grid import Grid

level_files = [f"levels/level{i}.json" for i in range(1, 4)]
level_buttons = [pygame.Rect(300, 200 + i * 80, 150, 50) for i in range(len(level_files))]
back_button_rect = pygame.Rect(20, 20, 100, 40)

def draw_level_select(screen, font):
    screen.blit(font.render("Wybierz poziom", True, (0, 0, 0)), (300, 100))
    for i, rect in enumerate(level_buttons):
        pygame.draw.rect(screen, (200, 200, 200), rect)
        screen.blit(font.render(f"Poziom {i+1}", True, (0, 0, 0)), (rect.x + 20, rect.y + 10))
    pygame.draw.rect(screen, (200, 200, 200), back_button_rect)
    screen.blit(font.render("Powrót", True, (0, 0, 0)), (back_button_rect.x + 5, back_button_rect.y + 5))

def handle_level_select_events(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        for i, rect in enumerate(level_buttons):
            if rect.collidepoint(x, y):
                selected_level = level_files[i]
                row_hints, col_hints, solution, rows, cols = load_puzzle(selected_level)
                grid = Grid(rows, cols, row_hints, col_hints)
                return "game", selected_level, grid, row_hints, col_hints, solution, ""
        if back_button_rect.collidepoint(x, y):
            return "main_menu", None, None, None, None, None, ""
    return "level_select", None, None, None, None, None, ""