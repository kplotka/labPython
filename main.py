import pygame
from screens.menu import draw_menu, handle_menu_events
from screens.level_select import draw_level_select, handle_level_select_events
from screens.save_level_select import draw_save_level_select, handle_save_level_select_events
from screens.save_list import draw_save_list, handle_save_list_events
from screens.game import draw_game, handle_game_events
from screens.dialogs import draw_exit_prompt, handle_exit_prompt_events

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Nonogram")
font = pygame.font.SysFont("arial", 28)
small_font = pygame.font.SysFont("arial", 22)

clock = pygame.time.Clock()
running = True

state = {
    "screen_state": "main_menu",
    "selected_level": None,
    "grid": None,
    "row_hints": None,
    "col_hints": None,
    "solution": None,
    "message": "",
    "message_color": (0, 0, 0),
    "asking_for_name": False,
    "typed_name": "",
    "show_overwrite_prompt": False,
    "overwrite_target": "",
    "confirm_exit": False,
}

while running:
    screen.fill((255, 255, 255))

    if state["screen_state"] == "main_menu":
        draw_menu(screen, font)
    elif state["screen_state"] == "level_select":
        draw_level_select(screen, font)
    elif state["screen_state"] == "save_level_select":
        draw_save_level_select(screen, font)
    elif state["screen_state"] == "save_list":
        draw_save_list(screen, font, state["selected_level"])
    elif state["screen_state"] == "game":
        draw_game(screen, font, small_font, state["grid"], state["message"], state["message_color"],
                  state["asking_for_name"], state["typed_name"], state["show_overwrite_prompt"],
                  state["overwrite_target"], state["confirm_exit"])
        if state["confirm_exit"]:
            draw_exit_prompt(screen, font)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT and state["screen_state"] == "game":
            state["confirm_exit"] = True
        elif event.type == pygame.QUIT:
            running = False

        if state["screen_state"] == "main_menu":
            state["screen_state"] = handle_menu_events(event)

        elif state["screen_state"] == "level_select":
            result = handle_level_select_events(event)
            if result[0] != "level_select":
                (state["screen_state"], state["selected_level"], state["grid"],
                 state["row_hints"], state["col_hints"], state["solution"], state["message"]) = result

        elif state["screen_state"] == "save_level_select":
            state["screen_state"], state["selected_level"] = handle_save_level_select_events(event)

        elif state["screen_state"] == "save_list":
            result = handle_save_list_events(event, state["selected_level"])
            if result[0] == "game":
                (state["screen_state"], state["selected_level"], state["grid"],
                 state["row_hints"], state["col_hints"], state["solution"]) = result
                state["message"] = ""
                state["message_color"] = (0, 0, 0)
                state["asking_for_name"] = False
                state["typed_name"] = ""
                state["show_overwrite_prompt"] = False
                state["overwrite_target"] = ""
                state["confirm_exit"] = False
            elif result[0] == "save_level_select":
                state["screen_state"] = result[0]

        elif state["screen_state"] == "game":
            if state["confirm_exit"]:
                running, state["confirm_exit"], state["asking_for_name"] = handle_exit_prompt_events(event)
                if not running:
                    pygame.quit()
                    break
            else:
                result = handle_game_events(
                    event, state["grid"], state["row_hints"], state["col_hints"], state["selected_level"],
                    state["solution"], state["typed_name"], state["message"], state["asking_for_name"],
                    state["show_overwrite_prompt"], state["overwrite_target"]
                )
                (state["screen_state"], state["grid"], state["message"], state["message_color"],
                 state["asking_for_name"], state["typed_name"], state["show_overwrite_prompt"],
                 state["overwrite_target"]) = result

    clock.tick(60)
pygame.quit()