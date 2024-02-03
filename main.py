from gamestate import GameState
from constants import *
import pygame
from pygame.locals import *
from visualizer import *
from PIL import Image
import numpy 


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
                # if the user misses completely
                if (abs(closest.x - SQUASHER_BAR_X) > ACCURACY_BUFFER):
                    gamestate.combo = 0
                else:
                    scaled_error = (closest.x - SQUASHER_BAR_X)/ACCURACY_BUFFER * numpy.pi # to fit the domain of cosine
                    score_scaling = 0.5 * (numpy.cos(scaled_error) + 1)
                    gamestate.score += score_scaling * (gamestate.combo + 1) * 1
                    gamestate.combo += score_scaling
                    closest.squashed = True
    

def draw(screen: pygame.Surface, gamestate: GameState):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill(BG_COLOR)
    screen.blit(gamestate.background, (0, 0))

    for hitcircle in gamestate.rendered_hitcircles:
        hitcircle.draw(screen)

    drawGoose(screen, gamestate)

    pygame.draw.line(screen, color=(0,0,0), start_pos=(SQUASHER_BAR_X, NOTESTREAM_Y - 20), end_pos=(SQUASHER_BAR_X, NOTESTREAM_Y + 60), width=10)

    pygame.display.update()
    
def drawGoose(screen: pygame.Surface, gamestate: GameState): # draws the goose in frames and includes user input
    gamestate.gooseIndex = (gamestate.gooseIndex + 1) % len(gamestate.gooseArray)   

    if gamestate.gooseSquashedBad:
        imageToDisplay = "assets/bad.png"
    elif gamestate.gooseSquashedGood:
        imageToDisplay = "assets/good.png"
    else:
        imageToDisplay = gamestate.gooseArray[gamestate.gooseIndex]

    GOOSE_Y = NOTESTREAM_Y-Image.open("assets/Waddle1.png").height
    screen.blit(imageToDisplay, (10, GOOSE_Y))  

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
