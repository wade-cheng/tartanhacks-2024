from constants import *
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

class Map:
    def __init__(self, mapfolder_filepath: str):
        # pass in file args
        self.author: str = ...
        self.audio: Sound = pygame.mixer.Sound(...)
        self.notes: Notes = Notes(...)
        self.bpm: int = …
    """

def notesstream(m : Map, gamestate : GameState):
    notestream_width = SCREEN_WIDTH - GOOSE_BUFFER
    notes : list[bool] = m.notes.notes_arr 

    # sync current time to start idx instead of it always zero
    startIdx : int = 0
    #adding an extra 3 beats so notes don't spawn out immediately
    visibleNotes : list[bool] = notes[startIdx: startIdx + BEATS_ON_SCREEN + 3]

    for i in range (len(visibleNotes)):
        if (visibleNotes[i]):
            x : int = (i * BEAT_WIDTH) + GOOSE_BUFFER
            gamestate.rendered_hitcircle_locs.append(x)





