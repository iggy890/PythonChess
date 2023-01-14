letters = ("a", "b", "c", "d", "e", "f", "g", "h")
from pygame import sprite

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

        self.sprite = sprite.Sprite()

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

        self.sprite = sprite.Sprite()

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

        self.sprite = sprite.Sprite()

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

        self.sprite = sprite.Sprite()

        if color == "white":
            self.sprite.image = images.white_bishop
        elif color == "black":
            self.sprite.image = images.black_bishop

    def sprite(self):
        return self.sprite

    def rect(self):
        return self.sprite.rect