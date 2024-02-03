import pygame
from pygame.locals import *

pygame.mixer.init()

class Note:
    def __init__(self):
        self.squashed = False

class Notes:
    """data structure for efficient Note operations"""
    def __init__(self, notes: list[Note | None]):
        self.notes_arr: list[Note | None] = notes


class Map:
    def __init__(self, maps_folderpath: str):
        print("loading map.")
        if maps_folderpath[-1] == "/":
            maps_folderpath = maps_folderpath[:-1]

        with open(f"{maps_folderpath}/map.cfg") as f:
            lines = f.readlines()
            lines = [i.strip() for i in lines if (i.strip() != "" and i[0] != "#")]

        # explicit notes arr is a list with the int values of where all the notes are 
        explicit_notes_arr: list[int] = []
        initing_notes = False
        for line in lines:
            if initing_notes:
                explicit_notes_arr.append(int(line))
                continue

            print(f"processing line: {line}")
            if line.strip() == "notes:":
                initing_notes = True
                continue

            key, value = line.split(": ")
            match key:
                case "author":
                    self.author: str = value
                case "audio path":
                    self.audio: pygame.mixer.Sound = pygame.mixer.Sound(f"{maps_folderpath}/{value}")
                case "first note offset":
                    self.offset: float = float(value)
                case "bpm":
                    self.bpm: int = int(value)
        
        # populate self.notes
        notes_arr_len = max(explicit_notes_arr)
        notes_arr: list[Note | None] = [None] * (notes_arr_len + 1)
        for note_idx in explicit_notes_arr:
            notes_arr[note_idx] = Note()
        self.notes: Notes = Notes(notes_arr)
        print(f"created note arr: {notes_arr}")

# this is a test case
if __name__ == "__main__":
    map = Map("maps/testcase_small")