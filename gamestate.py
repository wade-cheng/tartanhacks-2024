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
        self.pressNext = False
        self.pressBack = False

        self.hitstate = 0
        self.hitEffectCounter = 0
        self.nextComboVal = 100
        self.comboCounter = COMBO_EFFECT_TIMER + 1

        self.background = pygame.image.load("assets/windows.png")
        self.titlebackground = pygame.image.load("assets/title.png")
        self.leftarrow = pygame.image.load("assets/left_arrow_93x70.png")
        self.rightarrow = pygame.image.load("assets/right_arrow_93x70.png")
        self.ARROW_Y = 650
        self.LARROW_X = 300
        self.RARROW_X = 500
        self.LARROW_RECT = self.leftarrow.get_rect()
        self.LARROW_RECT.left = self.LARROW_X
        self.LARROW_RECT.top = self.ARROW_Y
        self.RARROW_RECT = self.rightarrow.get_rect()
        self.RARROW_RECT.left = self.RARROW_X
        self.RARROW_RECT.top = self.ARROW_Y
        
        # rendered_hitcircle_locs: a list of the x-positions of all the hitcircles to be rendered. can be off screen.
        self.rendered_hitcircles: list[Note] = []
        
        self.startTime = None

        self.maps: MapHolder = MapHolder()
        self.entered_map = False
        pygame.font.init()
        self.font = pygame.font.Font("assets/hero-speak.ttf", 42)
        self.titlefont = pygame.font.Font("assets/title-font.ttf", 72)

    def reset_map_gamestate(self):
        self.startTime = time.time()

        self.gooseIndex = 0
        self.gooseSquashedState = 0
        self.gooseSquashedCounter = 0

        self.score = 0
        self.combo = 0

        self.hitstate = 0
        self.hitEffectCounter = 0
        self.nextComboVal = 100
        self.comboCounter = COMBO_EFFECT_TIMER + 1

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