#start_time is the start time of the game
import pygame
from constants import *

def score_from_hit(start_time: float, hit_time: float, score_multiplier: float) -> float | None:
    hit_diff = abs(hit_time-start_time) #finds time object was "hit" by space
    if (hit_diff > 1): #will have to do the math to find time
        return None
    
    '''
        scoring and how that is split can be changed, just want to have something for now
        but can be handled through 'switch statement' here

    '''
    if (hit_diff < .1):
        return 1000*score_multiplier
    elif (hit_diff < .25):
        return 750*score_multiplier
    elif (hit_diff < .5):
        return 500*score_multiplier
    elif (hit_diff < .75):
        return 250*score_multiplier
    else:
        return 100*score_multiplier
    

    
    


