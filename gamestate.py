import pygame
from pygame.locals import *
from map import *
import time

class GameState:
    """holds the state of the game.
    when adding parameters, include a default value
    so previous code doesn't break"""
    
    def __init__(self) -> None:
        self.gooseIndex = 0
        self.playing = True
        self.score = 0
        self.combo = 0

        self.background = pygame.image.load("windows.png")
        self.gooseArray = [pygame.image.load("Sprite1.png"), pygame.image.load("Sprite2.png"), pygame.image.load("Sprite3.png"), pygame.image.load("Sprite4.png")]
        self.hitcircle = pygame.image.load('assets/hit_circle_basic.png')
        self.squashed_hitcircle = pygame.image.load('assets/hit_circle_basic_squashed.png')
        # rendered_hitcircle_locs: a list of the x-positions of all the hitcircles to be rendered. can be off screen.
        self.rendered_hitcircles: list[Note] = []
        self.map: Map = Map("maps/testcase_small")
        self.startTime = time.time()



if __name__ == "__main__":
    GameState()