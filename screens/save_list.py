import pygame
from puzzle import load_puzzle
from grid import Grid
from screens.utils import level_key_from_path, load_all_saves, load_save_by_name

back_button_rect = pygame.Rect(20, 20, 100, 40)

def draw_save_list(screen, font, selected_level):
    if selected_level is None:
        return
    screen.blit(font.render(f"Zapisy – {level_key_from_path(selected_level)}", True, (0, 0, 0)), (250, 40))
    save_data = load_all_saves().get(level_key_from_path(selected_level), {})
    for i, name in enumerate(save_data):
        rect = pygame.Rect(300, 100 + i * 60, 150, 40)
        pygame.draw.rect(screen, (200, 200, 200), rect)
        screen.blit(font.render(name, True, (0, 0, 0)), (rect.x + 10, rect.y + 5))
    pygame.draw.rect(screen, (200, 200, 200), back_button_rect)
    screen.blit(font.render("Powrót", True, (0, 0, 0)), (back_button_rect.x + 5, back_button_rect.y + 5))

def handle_save_list_events(event, selected_level):
    if selected_level is None:
        return "save_level_select", selected_level, None, None, None, None

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        key = level_key_from_path(selected_level)
        save_data = load_all_saves().get(key, {})
        for i, name in enumerate(save_data):
            rect = pygame.Rect(300, 100 + i * 60, 150, 40)
            if rect.collidepoint(x, y):
                data = load_save_by_name(selected_level, name)
                if data:
                    row_hints, col_hints, solution, rows, cols = load_puzzle(selected_level)
                    grid = Grid(rows, cols, row_hints, col_hints)
                    grid.grid = data["grid"]
                    return "game", selected_level, grid, row_hints, col_hints, solution
        if back_button_rect.collidepoint(x, y):
            return "save_level_select", selected_level, None, None, None, None

    return "save_list", selected_level, None, None, None, None