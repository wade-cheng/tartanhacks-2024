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
        
        self.screen = "title"
        self.playing = True
        self.score = 0
        self.combo = 0

        self.hitstate = 0
        self.hitEffectCounter = 0

        self.background = pygame.image.load("assets/windows.png")
        
        # rendered_hitcircle_locs: a list of the x-positions of all the hitcircles to be rendered. can be off screen.
        self.rendered_hitcircles: list[Note] = []
        
        self.startTime = time.time()

        self.maps: MapHolder = MapHolder()
        self.entered_map = False

        self.font = pygame.font.Font("assets/hero-speak.ttf", 42)


class MapHolder:
    def __init__(self):
        print(f"discovered maps {os.listdir('maps/')}")
        self.__map_idx = 0
        self.__map_list: list[Map] = []
        for map in os.listdir("maps"):
            self.__map_list.append(Map(f"maps/{map}"))
    
    def get_selected_map(self) -> Map:
        return self.__map_list[self.__map_idx]
    
    def select_next(self):
        self.__map_idx = (self.__map_idx + 1) % len(self.__map_list)
    
    def select_last(self):
        self.__map_idx = (self.__map_idx - 1) % len(self.__map_list)

if __name__ == "__main__":
    GameState()