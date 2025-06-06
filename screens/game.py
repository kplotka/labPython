import pygame
from screens.utils import save_game
from grid import Grid

overwrite_yes_rect = pygame.Rect(400, 400, 100, 40)
overwrite_no_rect = pygame.Rect(520, 400, 100, 40)

def draw_game(screen, font, small_font, grid, message, message_color,
              asking_for_name, typed_name, show_overwrite_prompt, overwrite_target,
              confirm_exit):
    grid.draw(screen)

    buttons = {
        "Sprawdź": pygame.Rect(700, 100, 150, 40),
        "Nowa gra": pygame.Rect(700, 160, 150, 40),
        "Menu": pygame.Rect(700, 220, 150, 40),
        "Zapisz grę": pygame.Rect(700, 280, 150, 40)
    }

    for label, rect in buttons.items():
        pygame.draw.rect(screen, (200, 200, 200), rect)
        screen.blit(font.render(label, True, (0, 0, 0)), (rect.x + 10, rect.y + 5))

    if message:
        screen.blit(font.render(message, True, message_color),
                    (700, 340))

    if asking_for_name:
        pygame.draw.rect(screen, (240, 240, 240), (300, 350, 400, 100))
        screen.blit(small_font.render("Podaj nazwę zapisu:", True, (0, 0, 0)), (320, 360))
        screen.blit(font.render(typed_name + "_", True, (0, 100, 200)), (320, 390))

    if show_overwrite_prompt:
        pygame.draw.rect(screen, (255, 255, 200), (300, 350, 400, 100))
        screen.blit(small_font.render(f"Nadpisać zapis \"{overwrite_target}\"?", True, (0, 0, 0)), (320, 360))
        pygame.draw.rect(screen, (180, 255, 180), overwrite_yes_rect)
        pygame.draw.rect(screen, (255, 180, 180), overwrite_no_rect)
        screen.blit(font.render("Tak", True, (0, 0, 0)), (overwrite_yes_rect.x + 20, overwrite_yes_rect.y + 5))
        screen.blit(font.render("Nie", True, (0, 0, 0)), (overwrite_no_rect.x + 20, overwrite_no_rect.y + 5))

def handle_game_events(event, grid, row_hints, col_hints, selected_level, solution,
                       typed_name, message, asking_for_name, show_overwrite_prompt, overwrite_target):
    screen_state = "game"
    message_color = (0, 0, 0)

    if event.type == pygame.KEYDOWN and asking_for_name:
        if event.key == pygame.K_BACKSPACE:
            typed_name = typed_name[:-1]
        elif event.key == pygame.K_RETURN and typed_name.strip():
            from screens.utils import load_all_saves, level_key_from_path
            level_key = level_key_from_path(selected_level)
            saves = load_all_saves()
            if typed_name in saves.get(level_key, {}):
                show_overwrite_prompt = True
                overwrite_target = typed_name
            else:
                save_game(typed_name, selected_level, grid.grid)
                message = f"Zapisano jako {typed_name}"
                message_color = (0, 100, 0)
                asking_for_name = False
        else:
            typed_name += event.unicode

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if show_overwrite_prompt:
            if overwrite_yes_rect.collidepoint(x, y):
                save_game(overwrite_target, selected_level, grid.grid)
                message = f"Nadpisano zapis {overwrite_target}"
                message_color = (0, 100, 0)
                show_overwrite_prompt = False
                asking_for_name = False
                typed_name = ""
            elif overwrite_no_rect.collidepoint(x, y):
                show_overwrite_prompt = False
                asking_for_name = True
            return screen_state, grid, message, message_color, asking_for_name, typed_name, show_overwrite_prompt, overwrite_target

        if 700 <= x <= 850:
            if 100 <= y <= 140:
                if grid.is_correct(solution):
                    message = "Poprawnie!"
                    message_color = (0, 150, 0)
                else:
                    message = "Spróbuj jeszcze raz"
                    message_color = (200, 0, 0)
            elif 160 <= y <= 200:
                grid = Grid(grid.rows, grid.cols, row_hints, col_hints)
                message = ""
            elif 220 <= y <= 260:
                return "main_menu", None, "", (0, 0, 0), False, "", False, ""
            elif 280 <= y <= 320:
                asking_for_name = True
                typed_name = ""
                message = ""

        if not asking_for_name and not show_overwrite_prompt:
            col = (x - grid.offset_x) // grid.cell_size
            row = (y - grid.offset_y) // grid.cell_size
            if 0 <= row < grid.rows and 0 <= col < grid.cols:
                right_click = (event.button == 3)
                grid.toggle_cell(row, col, right_click=right_click)
                message = ""

    return screen_state, grid, message, message_color, asking_for_name, typed_name, show_overwrite_prompt, overwrite_target