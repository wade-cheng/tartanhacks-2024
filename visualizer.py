from constants import *
import pygame
from map import *
from gamestate import *
import time


  
def notesstream( gamestate: GameState):
    """modifies gamestate.rendered_hitcircle_locs to contain the x positions of all visible hitcircles on screen at the current timestep

    Args:
        m (Map):  the map at this timestep
        gamestate (GameState): the gamestate at this timestep
    """
    m : Map = gamestate.map
    notes : list[Note | None] = m.notes.notes_arr
    t : float = time.time() - gamestate.startTime 

    pixels_between_beat : int = (SCREEN_WIDTH - SQUASHER_BAR_X) / BEATS_ON_SCREEN 

    pixels_per_timestep : int = m.bpm * (SCREEN_WIDTH - SQUASHER_BAR_X) / (BEATS_ON_SCREEN * 60 * FPS) 

    offset : float = (t * 60) * pixels_per_timestep

    gamestate.rendered_hitcircle_locs = []
    for i in range (len(notes)):
        start_loc = (i * pixels_between_beat) + SQUASHER_BAR_X # assumes first note starts ON squasher bar
        curr_loc = start_loc - offset
        if ((notes[i] is not None) and curr_loc >= -50 and curr_loc <= SCREEN_WIDTH + 50): # if visible (with margin of error) TODO: change 50 to width of hit_circle
            gamestate.rendered_hitcircle_locs.append(curr_loc) 



