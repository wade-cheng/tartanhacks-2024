import pygame
from pygame.locals import *

TILE_SIZE = 50
MAP_TILEWIDTH, MAP_TILEHEIGHT = 10, 10
MAP_WIDTH, MAP_HEIGHT = TILE_SIZE * MAP_TILEWIDTH, TILE_SIZE * MAP_TILEHEIGHT
BG_COLOR = (255, 255, 255)
PLAYER_WIGGLE_EVENT = pygame.USEREVENT + 1
PLAYER_MOVE_EVENT = pygame.USEREVENT + 2

class GameState:
    """holds the state of the game.
    when adding parameters, include a default value
    
    so previous code doesn't break"""
    def __init__(self, example_param: int=0) -> None:
        self.example_param = example_param
        self.playing = True

