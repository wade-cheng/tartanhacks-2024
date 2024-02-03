import pygame
from pygame.locals import *

class Notes:
    """data structure for efficient Note operations"""

    def __init__(self, notes_filepath: str):
        self.notes_arr: list[bool] = ...


class Map:
    def __init__(self, mapfolder_filepath: str):
        # pass in file args
        self.author: str = ...
        self.audio: pygame.mixer.Sound = pygame.mixer.Sound(...)
        self.notes: Notes = Notes(...)
        self.bpm: int = ...


class GameState:
    """holds the state of the game.
    when adding parameters, include a default value
    so previous code doesn't break"""
    def __init__(self, example_param: int=0) -> None:
        self.example_param = example_param
        self.playing = True


