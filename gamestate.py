import pygame
from pygame.locals import *
from map import Map
import time

class GameState:
    """holds the state of the game.
    when adding parameters, include a default value
    so previous code doesn't break"""
    
    def __init__(self) -> None:
        self.playing = True
        self.score = 0
        self.hitcircle = pygame.image.load('assets/hit_circle_basic.png')
        # rendered_hitcircle_locs: a list of the x-positions of all the hitcircles to be rendered. can be off screen.
        self.rendered_hitcircle_locs: list[float] = [10.8, 20.5,40.5,80.1]
        self.map: Map = Map("maps/testcase_small")
        self.startTime = time.time()


if __name__ == "__main__":
    GameState()