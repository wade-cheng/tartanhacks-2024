from constants import *
import pygame
from map import *
from gamestate import *
import time
from map import *

  
def notesstream( gamestate: GameState):
    """modifies gamestate.rendered_hitcircle_locs to contain the x positions of all visible hitcircles on screen at the current timestep

    Args:
        gamestate (GameState): the gamestate at this timestep
    """
    m : Map = gamestate.maps.get_selected_map()
    notes : list[Note | None] = m.notes.notes_arr
    t : float = time.time() - gamestate.startTime 

    pixels_between_beat : int = (SCREEN_WIDTH - SQUASHER_BAR_X) / BEATS_ON_SCREEN 

    pixels_per_timestep : int = m.bpm * (SCREEN_WIDTH - SQUASHER_BAR_X) / (BEATS_ON_SCREEN * 60 * FPS) 

   
    offset : float = ((t - m.offset)* 60) * pixels_per_timestep 

    gamestate.rendered_hitcircles = []
    for i in range (len(notes)):
        start_loc = (i * pixels_between_beat) + SQUASHER_BAR_X # assumes first note starts ON squasher bar
        curr_loc = start_loc - offset
        if (notes[i] is not None):
            notes[i].x = curr_loc
            if (curr_loc >= -50 and curr_loc <= SCREEN_WIDTH + 50): # if visible (with margin of error) TODO: change 50 to width of hit_circle
                gamestate.rendered_hitcircles.append(notes[i]) 


def get_closest_note(gamestate : GameState) -> Note :
    if (len(gamestate.rendered_hitcircles) < 1):
        return None
    minim = gamestate.rendered_hitcircles[0]
    for i in range (len(gamestate.rendered_hitcircles)):
        if (abs(SQUASHER_BAR_X - gamestate.rendered_hitcircles[i].x) < abs(SQUASHER_BAR_X - minim.x)):
            minim = gamestate.rendered_hitcircles[i]
    return minim