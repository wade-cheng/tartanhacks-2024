from constants import *
from gamestate import GameState
import pygame
from map import Map


def notesstream(m: Map, gamestate: GameState):
    notes : list[bool] = m.notes.notes_arr
    # sync current time to start idx instead of it always zero
    startIdx : int = 0
    #adding an extra 3 beats so notes don't spawn out immediately
    visibleNotes : list[bool] = notes[startIdx: startIdx + BEATS_ON_SCREEN + 3]

    for i in range (len(visibleNotes)):
        if (visibleNotes[i]):
            x : int = (i * BEAT_WIDTH) + GOOSE_BUFFER
            gamestate.rendered_hitcircle_locs.append(x)





