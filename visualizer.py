from constants import *
from gamestate import GameState
import pygame
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
        self.notes: list[bool] = file.readLine()
        

        file.close()

# def notes_arr (notes: list[bool]):
#     leng = len(notes)
#     for i in range(notes):
        



def notesstream(m : Map, gamestate: GameState):
    notes : list[bool] = m.notes.notes_arr
    # sync current time to start idx instead of it always zero
    startIdx : int = 0
    #adding an extra 3 beats so notes don't spawn out immediately
    visibleNotes : list[bool] = notes[startIdx: startIdx + BEATS_ON_SCREEN + 3]

    for i in range (len(visibleNotes)):
        if (visibleNotes[i]):
            x : int = (i * BEAT_WIDTH) + GOOSE_BUFFER
            gamestate.rendered_hitcircle_locs.append(x)





