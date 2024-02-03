import os
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
        self.gooseSquashedState = 0
        self.gooseSquashedCounter = 0
        self.gooseArray = [pygame.image.load("assets/Waddle1.png"), pygame.image.load("assets/Waddle2.png"), pygame.image.load("assets/Waddle3.png"), pygame.image.load("assets/Waddle4.png")]
        
        self.title = True
        self.playing = True
        self.score = 0
        self.combo = 0

        self.background = pygame.image.load("assets/windows.png")
        
        # rendered_hitcircle_locs: a list of the x-positions of all the hitcircles to be rendered. can be off screen.
        self.rendered_hitcircles: list[Note] = []
        self.map: Map = Map("maps/testcase_misty_mountains") # TODO CHANGE THIS IF YOU WANT A DIFFERENT MAP. THIS WILL CHANGE TO BE NOT HARDCODED LATER
        self.startTime = time.time()

        self.maps: MapHolder = MapHolder()


class MapHolder:
    def __init__(self):
        print(f"discovered maps {os.listdir('maps/')}")
        self.map_idx = 0
        self.map_list = []
        for map in os.listdir("maps"):
            self.map_list.append(f"maps/{map}")
    
    def get_selected_map(self) -> Map:
        return self.map_list[self.map_idx]
    
    def select_next(self):
        self.map_idx = (self.map_idx + 1) % len(self.map_list)
    
    def select_last(self):
        self.map_idx = (self.map_idx - 1) % len(self.map_list)

if __name__ == "__main__":
    GameState()