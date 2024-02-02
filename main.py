from gamestate import GameState
from constants import *
import pygame
from pygame.locals import *

def update(dt, gamestate: GameState):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    for event in pygame.event.get():
        if event.type == QUIT:
            gamestate.playing = False
        elif event.type == -1: # a constant like PLAYER_MOVE_EVENT = pygame.USEREVENT + 1
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_SPACE:
                    print("pressed space")


def draw(screen: pygame.Surface, gamestate: GameState):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill(BG_COLOR)

    pygame.display.update()


def main():
    gamestate = GameState()

    pygame.init()

    fps = 60.0
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, vsync=1)
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED, vsync=1)
    screen.fill(BG_COLOR)
    pygame.display.update()

    dt = 1 / fps
    while gamestate.playing:
        update(dt, gamestate)
        draw(screen, gamestate)

        dt = fpsClock.tick(fps)


if __name__ == "__main__":
    main()
