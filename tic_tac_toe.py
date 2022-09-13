import pygame
import sys


def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count("0")
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return "Piece"
    return False


pygame.init()

size_block = 100
margin = 15
width = height = size_block*3 + margin*4

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic Tac Toe")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
massive = [["0"]*3 for _ in range(3)]
query = 0  # 1 2 3 4 5 6 7
game_over = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if massive[row][col] == "0":
                if query % 2 == 0:
                    massive[row][col] = "x"
                else:
                    massive[row][col] = "o"
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            massive = [["0"]*3 for _ in range(3)]
            query = 0
            screen.fill(BLACK)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if massive[row][col] == "x":
                    color = RED
                elif massive[row][col] == "o":
                    color = GREEN
                else:
                    color = WHITE
                x = col*size_block + (col + 1)*margin
                y = row*size_block + (row + 1)*margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == RED:
                    pygame.draw.line(screen, WHITE, (x+5, y+5), (x+size_block-5, y+size_block-5), 5)
                    pygame.draw.line(screen, WHITE, (x+size_block-5, y+5), (x+5, y+size_block-5), 5)
                elif color == GREEN:
                    pygame.draw.circle(screen, WHITE, (x+size_block//2, y+size_block//2), size_block//2-7, 5)

    if (query-1)%2 == 0:   # x
        game_over = check_win(massive, "x")
    else:
        game_over = check_win(massive, "o")
    if game_over:
        screen.fill(BLACK)
        font = pygame.font.SysFont("stxingkai", 80)
        text_1 = font.render(game_over, True, WHITE)
        text_rect = text_1.get_rect()
        text_x = screen.get_width() // 2 - text_rect.width // 2
        text_y = screen.get_height() // 2 - text_rect.height // 2
        screen.blit(text_1, [text_x, text_y])



    pygame.display.update()


















