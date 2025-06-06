import pygame

def draw_menu(screen, font):
    title = font.render("NONOGRAM", True, (0, 0, 0))
    screen.blit(title, (screen.get_width() // 2 - 80, 100))

    buttons = {
        "new_game": pygame.Rect(screen.get_width() // 2 - 100, 200, 200, 60),
        "load_game": pygame.Rect(screen.get_width() // 2 - 100, 300, 200, 60)
    }

    for key, rect in buttons.items():
        pygame.draw.rect(screen, (200, 200, 200), rect)
        label = "Nowa gra" if key == "new_game" else "Zapisane gry"
        screen.blit(font.render(label, True, (0, 0, 0)), (rect.x + 20, rect.y + 10))

def handle_menu_events(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        new_game_btn = pygame.Rect(400, 200, 200, 60)
        load_game_btn = pygame.Rect(400, 300, 200, 60)
        if new_game_btn.collidepoint(x, y):
            return "level_select"
        elif load_game_btn.collidepoint(x, y):
            return "save_level_select"
    return "main_menu"