import pygame

exit_prompt_rects = {}

def draw_exit_prompt(screen, font):
    dialog = pygame.Rect(screen.get_width() // 2 - 150, 200, 300, 150)
    pygame.draw.rect(screen, (255, 255, 200), dialog)
    small_font = pygame.font.SysFont("arial", 22)
    screen.blit(small_font.render("Czy chcesz zapisać grę", True, (0, 0, 0)), (dialog.x + 30, dialog.y + 20))
    screen.blit(small_font.render("przed wyjściem?", True, (0, 0, 0)), (dialog.x + 30, dialog.y + 50))

    yes_btn = pygame.Rect(dialog.x + 30, dialog.y + 80, 100, 40)
    no_btn = pygame.Rect(dialog.x + 170, dialog.y + 80, 100, 40)
    pygame.draw.rect(screen, (200, 200, 200), yes_btn)
    pygame.draw.rect(screen, (200, 200, 200), no_btn)
    screen.blit(font.render("Tak", True, (0, 0, 0)), (yes_btn.x + 20, yes_btn.y + 5))
    screen.blit(font.render("Nie", True, (0, 0, 0)), (no_btn.x + 20, no_btn.y + 5))

    exit_prompt_rects["yes"] = yes_btn
    exit_prompt_rects["no"] = no_btn

def handle_exit_prompt_events(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if exit_prompt_rects["yes"].collidepoint(x, y):
            return True, False, True
        elif exit_prompt_rects["no"].collidepoint(x, y):
            return False, False, False
    return True, True, False