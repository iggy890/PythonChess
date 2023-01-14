import pygame, images
from colordefs import *

pygame.init()
letters = ("a", "b", "c", "d", "e", "f", "g", "h")

print("Creating classes")
class BoardPosition:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_picture_coordinates(self):
        return ((self.x * 76) + self.x, (self.y * 76) + self.y)

    def string(self):
        return f"{letters[self.x]}{self.y}"

class Pawn:
    def __init__(self, startX: int, startY: int, color: str) -> None:
        self.startX = startX
        self.startY = startY

        self.type = "Pawn"
        self.points = 1

        self.sprite = pygame.sprite.Sprite()

        if color == "white":
            self.sprite.image = images.white_pawn
        elif color == "black":
            self.sprite.image = images.black_pawn

    def sprite(self):
        return self.sprite

    def rect(self):
        sprite = self.sprite
        return sprite.rect()

class Knight:
    def __init__(self, startX: int, startY: int, color: str) -> None:
        self.startX = startX
        self.startY = startY

        self.type = "Knight"
        self.points = 3

        self.sprite = pygame.sprite.Sprite()

        if color == "white":
            self.sprite.image = images.white_knight
        elif color == "black":
            self.sprite.image = images.black_knight

    def sprite(self):
        return self.sprite

    def rect(self):
        return self.sprite.rect

class Bishop:
    def __init__(self, startX: int, startY: int, color: str) -> None:
        self.startX = startX
        self.startY = startY

        self.type = "Bishop"
        self.points = 3

        self.sprite = pygame.sprite.Sprite()

        if color == "white":
            self.sprite.image = images.white_bishop
        elif color == "black":
            self.sprite.image = images.black_bishop

    def sprite(self):
        return self.sprite

    def rect(self):
        return self.sprite.rect

class Rook:
    def __init__(self, startX: int, startY: int, color: str) -> None:
        self.startX = startX
        self.startY = startY

        self.type = "Rook"
        self.points = 3

        self.sprite = pygame.sprite.Sprite()

        if color == "white":
            self.sprite.image = images.white_bishop
        elif color == "black":
            self.sprite.image = images.black_bishop

    def sprite(self):
        return self.sprite

    def rect(self):
        return self.sprite.rect

__white_dir__ = "Images/White/"
__black_dir__ = "Images/Black/"

print("Loading Images")
chessboard = pygame.image.load("Images/chessboard.png").convert()

white_bishop = pygame.image.load(__white_dir__+"bishop.png").convert() 
white_king = pygame.image.load(__white_dir__+"king.png").convert()
white_knight = pygame.image.load(__white_dir__+"knight.png").convert()
white_pawn = pygame.image.load(__white_dir__+"pawn.png").convert()
white_queen = pygame.image.load(__white_dir__+"queen.png").convert()
white_rook = pygame.image.load(__white_dir__+"rook.png").convert() 

black_bishop = pygame.image.load(__black_dir__+"bishop.png").convert() 
black_king = pygame.image.load(__black_dir__+"king.png").convert() 
black_knight = pygame.image.load(__black_dir__+"knight.png").convert() 
black_pawn = pygame.image.load(__black_dir__+"pawn.png").convert() 
black_queen = pygame.image.load(__black_dir__+"queen.png").convert() 
black_rook = pygame.image.load(__black_dir__+"rook.png").convert()

print()
screen_size = width, height = 612, 612

screen = pygame.display.set_mode(screen_size)

chess_board = images.chessboard

screen.blit(chess_board, (0, 0))

a1 = BoardPosition(1, 1)
a1coords = a1.get_picture_coordinates()

pawn = Pawn(a1coords[0], a1coords[1], "white")
rect = pawn.rect()
pygame.draw.rect(screen, white, rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()