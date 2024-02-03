from constants import *
import pygame
from gamestate import *
"""
    # class Note:
#     def __init__(self, count: int):
#         # duration in counts
#         self.count = count
	
class Notes:
   data structure for efficient Note operations

    def __init__(self, notes_filepath: str):
        self.notes_arr: list[bool] = ...

    def other methods idk
"""
class Map:
    def __init__(self, mapfolder_filepath: str):
        file = open(mapfolder_filepath, "r")
        file.readLine()
        self.author: str = file.readLine()
        file.readLine()
        file.readLine()
        self.bpm: int = file.readLine()
        self.audio: pygame.mixer.Sound = pygame.mixer.Sound(file.readLine())
        self.notes: list[bool] = []
        

        file.close()


def notesstream(m : Map, gamestate : GameState):
    notes : list[bool] = m.notes.notes_arr 

    time : float = 0 # in seconds 

    pixels_between_beat : int = (SCREEN_WIDTH - SQUASHER_BAR_X) / BEATS_ON_SCREEN 

    pixels_per_timestep : int = m.bpm * (SCREEN_WIDTH - SQUASHER_BAR_X) / (BEATS_ON_SCREEN * 3600) 

    offset : float = (time * 60) * pixels_per_timestep

    gamestate.rendered_hitcircle_locs = []
    for i in range (len(notes)):
        start_loc = (i * pixels_between_beat) + SQUASHER_BAR_X # assumes first note starts ON squasher bar
        curr_loc = start_loc - offset
        if (curr_loc >= -50 and curr_loc <= SCREEN_WIDTH + 50): # if visible (with margin of error) TODO: change 50 to width of hit_circle
            gamestate.rendered_hitcircle_locs.append(curr_loc) 



