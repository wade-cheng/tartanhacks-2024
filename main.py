from gamestate import GameState
from constants import *
import pygame
from pygame.locals import *
from visualizer import *


def get_closest_note(gamestate : GameState) -> Note :
    minim = gamestate.rendered_hitcircles[0]
    for i in range (len(gamestate.rendered_hitcircles)):
        if (abs(SQUASHER_BAR_X - gamestate.rendered_hitcircles[i].x) < abs(SQUASHER_BAR_X - minim.x)):
            minim = gamestate.rendered_hitcircles[i]
    return minim


def update(dt, gamestate: GameState):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    notesstream(gamestate)

    for event in pygame.event.get():
        if event.type == QUIT:
            gamestate.playing = False
        elif event.type == -1: # a constant like PLAYER_MOVE_EVENT = pygame.USEREVENT + 1
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                closest = get_closest_note(gamestate)
                closest.squashed = True
    
    closest = get_closest_note(gamestate)
    closest.squashed = True


def draw(screen: pygame.Surface, gamestate: GameState):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill(BG_COLOR)
    screen.blit(gamestate.background, (0, 0))

    for hitcircle in gamestate.rendered_hitcircles:
        if hitcircle.squashed:
            screen.blit(gamestate.squashed_hitcircle, (hitcircle.x, NOTESTREAM_Y))
        else:
            screen.blit(gamestate.hitcircle, (hitcircle.x, NOTESTREAM_Y))


    drawGoose(screen, gamestate)
    pygame.display.update()
    
def drawGoose(screen: pygame.Surface, gamestate: GameState): # draws the goose in frames and includes user input
    gamestate.gooseIndex = (gamestate.gooseIndex + 1) % len(gamestate.gooseArray)   

    if gamestate.gooseSquashedBad:
        imageToDisplay = "bad.png"
    elif gamestate.gooseSquashedGood:
        imageToDisplay = "bad.png"
    else:
        imageToDisplay = gamestate.gooseArray[gamestate.gooseIndex]
    screen.blit(imageToDisplay, (10, 10))  

def main():
    gamestate = GameState()
    print(gamestate)

    pygame.init()

    fps = FPS
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, vsync=1)
    pygame.display.set_caption("Goose Rhythm Game")
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED, vsync=1)
    screen.fill(BG_COLOR)
    pygame.display.update()

    #goose = pygame.image.load(), upload goose images to repo to pull

    dt = 1 / fps
    while gamestate.playing:
        update(dt, gamestate)
        draw(screen, gamestate)
        dt = fpsClock.tick(fps)



if __name__ == "__main__":
    main()
