import pygame
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

# Load images
PIECES = {
    'bR': pygame.image.load('images/black_rook.png'),
    'bN': pygame.image.load('images/black_knight.png'),
    'bB': pygame.image.load('images/black_bishop.png'),
    'bQ': pygame.image.load('images/black_queen.png'),
    'bK': pygame.image.load('images/black_king.png'),
    'bP': pygame.image.load('images/black_pawn.png'),
    'wR': pygame.image.load('images/white_rook.png'),
    'wN': pygame.image.load('images/white_knight.png'),
    'wB': pygame.image.load('images/white_bishop.png'),
    'wQ': pygame.image.load('images/white_queen.png'),
    'wK': pygame.image.load('images/white_king.png'),
    'wP': pygame.image.load('images/white_pawn.png')
}

# Resize images
for key in PIECES:
    PIECES[key] = pygame.transform.scale(PIECES[key], (WIDTH // 8, HEIGHT // 8))

# Define the initial board state
board = [
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
]

def draw_board(screen):
    colors = [LIGHT_BROWN, DARK_BROWN]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * WIDTH // 8, row * HEIGHT // 8, WIDTH // 8, HEIGHT // 8))

def draw_pieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '--':
                screen.blit(PIECES[piece], pygame.Rect(col * WIDTH // 8, row * HEIGHT // 8, WIDTH // 8, HEIGHT // 8))

def main():
    clock = pygame.time.Clock()
    screen.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board(screen)
        draw_pieces(screen, board)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
