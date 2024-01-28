from time import time

import pygame, sys
from pygame import mixer

from GameLogic.dumb_computer import DumbComputerPlayer
from GameLogic.medium_ai import MediumComputerPlayer
from UI.GUI.button import Button
from GameLogic.data_model import Board

from game_exception import GameException

pygame.init()

# Set up the drawing window
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode([screen_width, screen_height])

background = pygame.image.load("/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/start menu.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

mixer.init()


def difficulty(human, computer, board):
    pygame.display.set_caption("Connect Four Difficulty")
    while True:
        screen.fill("black")
        screen.blit(background, (0, 0))

        difficulty_mouse_pos = pygame.mouse.get_pos()

        difficulty_text = pygame.font.Font(
            "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/Frutiger_bold.ttf", 100).render(
            "Choose Difficulty", True, ("white"))
        difficulty_rect = difficulty_text.get_rect(center=(screen_width / 2, screen_height / 2 - 150))

        dumb_button = Button(None, (screen_width / 2, screen_height / 2), "Dumb Computer",
                             pygame.font.Font(
                                 "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/Frutiger_bold.ttf",
                                 50), (208, 252, 229), "white")

        smart_button = Button(None, (screen_width / 2, screen_height / 2 + 100), "Smart Computer",
                              pygame.font.Font(
                                  "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/Frutiger_bold.ttf",
                                  50), (208, 252, 229), "white")

        screen.blit(difficulty_text, difficulty_rect)

        for button in [dumb_button, smart_button]:
            button.change_color(difficulty_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dumb_button.check_for_input(difficulty_mouse_pos):
                    computer_engine = "dumb"
                    play(human, computer, board, DumbComputerPlayer(board, human, computer))
                elif smart_button.check_for_input(difficulty_mouse_pos):
                    computer_engine = "smart"
                    play(human, computer, board, MediumComputerPlayer(board, human, computer))
        pygame.display.update()


def draw_disc(board, human, computer):
    x = [256, 367, 480, 592, 705, 817, 930]
    x.reverse()
    y = [630, 530, 430, 330, 230, 130]

    for row in range(6):
        for col in range(7):
            if board.board[row][col] == human:
                image = pygame.image.load(
                    "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/blue_bubble.png")
                screen.blit(image, (x[6 - col], y[5 - row]))
            elif board.board[row][col] == computer:
                image = pygame.image.load(
                    "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/red_bubble.png")
                screen.blit(image, (x[6 - col], y[5 - row]))


def play(human, computer, board, computer_engine):
    pygame.display.set_caption("Play Connect Four")
    game_over = False
    win_text = None
    mixer.music.load("/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/play_music.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)
    while True:
        # play the play_music.mp3
        play_mouse_pos = pygame.mouse.get_pos()
        screen.fill("black")
        play_background = pygame.image.load(
            "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/play_background.png")
        screen.blit(play_background, (0, 0))

        exit_button = Button(None, (1185, 50), "Exit", pygame.font.Font(
            "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/Frutiger_bold.ttf", 50),
                             (208, 252, 229), "white")
        exit_button.change_color(play_mouse_pos)
        exit_button.update(screen)

        draw_disc(board, human, computer)

        if win_text and game_over:
            # display winning message up
            if win_text == "human":
                human_win_text = pygame.font.Font(
                    "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/Frutiger_bold.ttf",
                    50).render("Congratulations Human, You Won!", True, "white")
                human_win_rect = human_win_text.get_rect(center=(screen_width / 2, screen_height / 2 - 300))
                screen.blit(human_win_text, human_win_rect)
                game_over = True
            elif win_text == "computer":
                computer_win_text = pygame.font.Font(
                    "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/Frutiger_bold.ttf",
                    50).render("Sorry Human, I Won.", True, "white")
                computer_win_rect = computer_win_text.get_rect(center=(screen_width / 2, screen_height / 2 - 300))
                screen.blit(computer_win_text, computer_win_rect)
                game_over = True

        image = pygame.image.load(
            "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/blue_bubble.png")

        current_position = pygame.mouse.get_pos()
        if board.current_player == human and game_over == False and 240 <= current_position[0] <= 1025:
            screen.blit(image, (current_position[0] - 42.5, 30))
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.check_for_input(play_mouse_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if board.current_player == computer and not game_over:
                # wait a bit before the computer makes a move
                pygame.display.update()
                # pygame.time.delay(1000)
                col = int(computer_engine.get_move()) - 1
                print(col)
                start = time()
                while time() - start <= 0.5:
                    pass
                try:
                    row = board.make_move(col)
                    win = board.check_win((row, col))
                    if win:
                        win_text = "computer"
                        game_over = True
                except GameException:
                    continue
                pygame.display.update()
            elif board.current_player == human:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not game_over:
                        # get user's input
                        if board.is_board_full() is True:
                            game_over = True
                        elif 240 <= event.pos[0] <= 1025:
                            col = -1
                            pos_x = event.pos[0]
                            if 240 <= pos_x <= 350:
                                col = 0
                            elif 351 <= pos_x <= 465:
                                col = 1
                            elif 466 <= pos_x <= 580:
                                col = 2
                            elif 581 <= pos_x <= 690:
                                col = 3
                            elif 691 <= pos_x <= 805:
                                col = 4
                            elif 806 <= pos_x <= 915:
                                col = 5
                            elif 916 <= pos_x <= 1025:
                                col = 6
                            try:
                                row = board.make_move(col)
                                win = board.check_win((row, col))
                                if win:
                                    win_text = "human"
                                    game_over = True
                            except GameException:
                                continue
                pygame.display.update()

        pygame.display.update()


def main_menu(human, computer, board):
    mixer.music.load("/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/main_menu.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)

    while True:
        pygame.display.set_caption("Welcome to Connect 4!")
        screen.blit(background, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = pygame.font.Font(
            "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/Frutiger_bold.ttf", 100).render(
            "Welcome to Connect 4!", True, ("white"))
        menu_rect = menu_text.get_rect(center=(screen_width / 2, screen_height / 2 - 150))

        play_button = Button(None, (screen_width / 2, screen_height / 2), "Play",
                             pygame.font.Font(
                                 "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/Frutiger_bold.ttf",
                                 50), (208, 252, 229), "white")

        quit_button = Button(None, (screen_width / 2, screen_height / 2 + 100), "Quit",
                             pygame.font.Font(
                                 "/Users/Alex/Documents/GitHub/a9-915-Mindrila-Mihail/UI/GUI/GUI data/Frutiger_bold.ttf",
                                 50), (208, 252, 229), "white")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    difficulty(human, computer, board)
                elif quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


class GUI:
    def __init__(self, board: Board()):
        self._board = board

    def start(self, human, computer):
        main_menu(human, computer, self._board)
