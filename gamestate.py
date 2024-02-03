import pygame
from pygame.locals import *

class Notes:
    """data structure for efficient Note operations"""

    def __init__(self, notes_filepath: str):
        self.notes_arr: list[bool] = None


class Map:
    def __init__(self, mapfolder_filepath: str):
        # pass in file args
        self.author: str = "temp"
        self.audio: pygame.mixer.Sound = None
        self.notes: Notes = None
        self.bpm: int = None


class GameState:
    """holds the state of the game.
    when adding parameters, include a default value
    so previous code doesn't break"""
    def __init__(self, example_param: int=0) -> None:
        self.example_param = example_param
        self.playing = True
        self.hitcircle = pygame.image.load('assets/hit_circle_basic.png')
        # rendered_hitcircle_locs: a list of the x-positions of all the hitcircles to be rendered. can be off screen.
        self.rendered_hitcircle_locs: list[float] = []


