with open("./maps/testcase_small/map.cfg") as f:
  fileAccess = f.readlines()
  # print(fileAccess)
  fileAccess = [i.strip() for i in fileAccess if (i.strip() != "" and i[0] != "#")]
  print(fileAccess)

def createNotesArray(maps_filepath):
    return maps_filepath[7:len(maps_filepath)]

class Notes:
    """data structure for efficient Note operations"""

    def __init__(self, maps_filepath: str):
        self.notes_arr: list[bool] = createNotesArray(maps_filepath)

    # def other methods idk


class Map:
    def __init__(self, maps_filepath: str):
        # pass in file args
        self.author: str = maps_filepath[1]
        self.audio: Sound = pygame.mixer.Sound(maps_filepath[4])
        self.notes: Notes = Notes(maps_filepath)
        self.bpm: int = maps_filepath[7]







