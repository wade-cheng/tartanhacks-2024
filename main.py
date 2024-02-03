from gamestate import GameState
from constants import *
import pygame
import wave
from pygame.locals import *
from visualizer import *
from PIL import Image
import numpy 


def get_closest_note(gamestate : GameState) -> Note :
    if (len(gamestate.rendered_hitcircles) < 1):
        return None
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
            '''
            if event.key == pygame.MOUSEBUTTONDOWN:
                
            '''
            if event.key == pygame.K_SPACE:
                closest = get_closest_note(gamestate)
                if closest == None:
                    break
                # if the user misses completely
                if (abs(closest.x - SQUASHER_BAR_X) > ACCURACY_BUFFER):
                    gamestate.combo = 0
                    gamestate.gooseSquashedCounter = 0
                    gamestate.gooseSquashedState = 2
                else:
                    scaled_error = (closest.x - SQUASHER_BAR_X)/ACCURACY_BUFFER * numpy.pi # to fit the domain of cosine
                    score_scaling = 0.5 * (numpy.cos(scaled_error) + 1)
                    gamestate.score += int(score_scaling * (gamestate.combo + 1) * 100)
                    gamestate.combo += score_scaling * 10
                    closest.squashed = True
                    gamestate.gooseSquashedCounter = 0
                    gamestate.gooseSquashedState = 1

    

def draw(screen: pygame.Surface, font, gamestate: GameState):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill(BG_COLOR)
    screen.blit(gamestate.background, (0, 0))

    for hitcircle in gamestate.rendered_hitcircles:
        hitcircle.draw(screen)

    drawGoose(screen, gamestate)

    pygame.draw.line(screen, color=(255, 255, 255), start_pos=(SQUASHER_BAR_X, NOTESTREAM_Y - 100), end_pos=(SQUASHER_BAR_X, NOTESTREAM_Y + 100), width=5)

    score_text = font.render("Score: " + str(gamestate.score), True, (255, 255, 255))#, (0,0,0))
    combo_text = font.render("Combo: " + str(round(gamestate.combo,2)), True, (255, 255, 255))#, (0,0,0))
    screen.blit(score_text, (800, 50))
    screen.blit(combo_text, (800, 150))



    pygame.display.update()

def drawGoose(screen: pygame.Surface, gamestate: GameState): # draws the goose in frames and includes user input
    if gamestate.gooseSquashedCounter >= 10:
        gamestate.gooseSquashedCounter = 0
        gamestate.gooseSquashedState = 0

    if gamestate.gooseSquashedState == 1: # good
        imageToDisplay = pygame.image.load("assets/squashgood.png")
        gamestate.gooseSquashedCounter += 1

    elif gamestate.gooseSquashedState == 2: # bad
        imageToDisplay = pygame.image.load("assets/squashbad.png")
        gamestate.gooseSquashedCounter += 1

    else:
        gamestate.gooseIndex += 1
        gamestate.gooseIndex %= (len(gamestate.gooseArray) * 3)
        imageToDisplay = gamestate.gooseArray[int(gamestate.gooseIndex/3)]

    GOOSE_Y = NOTESTREAM_Y- 0.5 * Image.open("assets/Waddle1.png").height

    screen.blit(imageToDisplay, (0, GOOSE_Y))  

def playMusic(sound: pygame.mixer.Sound):
    pygame.mixer.find_channel().play(sound)

def main():
    '''
    intro_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, vsync=1)
    pygame.display.set_caption("Goose Rhythm Game")
    screen.fill((0,0,0))
    quitButton = font.render("Quit", True, (255,255,255), (0,0,0))
    welcome = font.render(")
    intro_screen.blit(quitButton,(400,600))
    intro_screen.blit(welcome, (350, 100))
    '''
    gamestate = GameState()
    print(gamestate)

    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 40)

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
        draw(screen, font, gamestate)
        dt = fpsClock.tick(fps)



if __name__ == "__main__":
    main()
