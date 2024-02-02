from constants import *

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

def notesstream(m : Map):
    notes : list[bool] = m.notes.notes_arr 

    # sync current time to start idx instead of it always zero
    startIdx : int = 0
    visibleNotes : list[bool] = notes[startIdx: startIdx + BEATS_ON_SCREEN]

    for i in range (len(visibleNotes)):
        # y position = NOTESTREAM_Y
        # x position = (i * )





