from gamestate import GameState
from constants import *
import pygame
from pygame.locals import *
from visualizer import *



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
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:

        #         if (abs(SQUASHER_BAR_X - )):
        #             gamestate.score += 1
        #         else:


def draw(screen: pygame.Surface, gamestate: GameState):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill(BG_COLOR)
    imp = pygame.image.load("windows.png").convert()
    screen.blit(imp, (0, 0))

    for hitcircle_loc in gamestate.rendered_hitcircle_locs:
        screen.blit(gamestate.hitcircle, (hitcircle_loc, NOTESTREAM_Y))
        
    pygame.display.update()
    

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
