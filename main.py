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


# def print_map_buttons(screen: pygame.Surface):
#     mapholder = MapHolder()
#     map_num = 1
#     button_y = 200
#     for map in mapholder.map_list:
#         buttonName = "Map " + str(map_num)
#         map_num += 1
#         mapButton = font.render(buttonName, True, (255,255,255), (0,0,0))
#         screen.blit(mapButton, (350, button_y))
#         button_y += 50


def update_game(gamestate: GameState):
    notesstream(gamestate)
    for event in pygame.event.get():
        if event.type == QUIT:
            gamestate.entered_map = False
            gamestate.playing = False
            pygame.mixer.pause()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                gamestate.entered_map = False
                pygame.mixer.pause()
            if event.key == pygame.K_SPACE:
                closest = get_closest_note(gamestate)
                press_x = 0
                if closest == None:
                    press_x = 9999
                else:
                    press_x = closest.x
                # if the user misses completely
                if (abs(press_x - SQUASHER_BAR_X) > ACCURACY_BUFFER):
                    gamestate.combo = 0
                    gamestate.gooseSquashedCounter = 0
                    gamestate.gooseSquashedState = 2
                    gamestate.hitstate = 0
                else:
                    scaled_error = (press_x - SQUASHER_BAR_X)/ACCURACY_BUFFER * numpy.pi # to fit the domain of cosine
                    score_scaling = 0.5 * (numpy.cos(scaled_error) + 1)
                    gamestate.score += int(score_scaling * (gamestate.combo + 1) * 100)
                    gamestate.combo += int(score_scaling * 10)
                    closest.squashed = True
                    gamestate.hitstate = int(abs(scaled_error)) + 1 # theoretically between 1 and 4 
                    gamestate.hitEffectCounter = 0
                    gamestate.gooseSquashedCounter = 0
                    gamestate.gooseSquashedState = 1

    

def draw_game(screen: pygame.Surface, gamestate: GameState):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill(BG_COLOR)
    screen.blit(gamestate.background, (0, 0))
    if (gamestate.hitEffectCounter <= HIT_EFFECT_TIMER and gamestate.hitstate > 0):
        match gamestate.hitstate:
            case 1:
                effect_text = gamestate.font.render("perfect!!", True, (255, 255, 255))
            case 2:
                effect_text = gamestate.font.render("awesome!!", True, (100, 255, 100))
            case 3:
                effect_text = gamestate.font.render("nice!", True, (255, 100, 100))
            case 4:
                effect_text = gamestate.font.render("good", True, (50, 50, 200))
        screen.blit(effect_text, (500, 150))
        gamestate.hitEffectCounter += 1

    
    if gamestate.combo > gamestate.nextComboVal:
        gamestate.comboCounter = 0
        gamestate.nextComboVal += 100


    if (gamestate.comboCounter <= COMBO_EFFECT_TIMER):
        gamestate.comboCounter += 1
        combo_text = gamestate.font.render(str(gamestate.nextComboVal - 100) + "x Combo!!!", True, (255, 255, 255))
        screen.blit(combo_text, (500, 250))

        
        

    for hitcircle in gamestate.rendered_hitcircles:
        hitcircle.draw(screen)

    drawGoose(screen, gamestate)

    pygame.draw.line(screen, color=(255, 255, 255), start_pos=(SQUASHER_BAR_X, NOTESTREAM_Y - 100), end_pos=(SQUASHER_BAR_X, NOTESTREAM_Y + 100), width=5)

    score_text = gamestate.font.render("Score: " + str(gamestate.score), True, (255, 255, 255))#, (0,0,0))
    combo_text = gamestate.font.render("Combo: " + str(round(gamestate.combo,2)), True, (255, 255, 255))#, (0,0,0))
    screen.blit(score_text, (800, 50))
    screen.blit(combo_text, (800, 150))

    

    pygame.display.update()

def drawGoose(screen: pygame.Surface, gamestate: GameState): # draws the goose in frames and includes user input
    if gamestate.gooseSquashedCounter >= GOOSE_SQUASH_TIMER:
        gamestate.gooseSquashedCounter = 0
        gamestate.gooseSquashedState = 0

    match gamestate.gooseSquashedState:
        case 0: #running
            gamestate.gooseIndex += 1
            gamestate.gooseIndex %= (len(gamestate.gooseArray) * 3)
            imageToDisplay = gamestate.gooseArray[int(gamestate.gooseIndex/3)]
        case 1: # good hit
            imageToDisplay = pygame.image.load("assets/squashgood.png")
            gamestate.gooseSquashedCounter += 1
        case 2: #bad hit
            imageToDisplay = pygame.image.load("assets/squashbad.png")
            gamestate.gooseSquashedCounter += 1

    GOOSE_Y = NOTESTREAM_Y- 0.5 * Image.open("assets/Waddle1.png").height

    screen.blit(imageToDisplay, (0, GOOSE_Y))  

def playMusic(sound: pygame.mixer.Sound):
    pygame.mixer.find_channel().play(sound)

def start_screen(font: pygame.font, screen: pygame.Surface) -> None:
    # pygame.font.init()
    # #intro_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, vsync=1)
    # pygame.display.set_caption("Goose Rhythm Game")
    # screen.fill((0,0,0))
    # quitButton = font.render("Quit", True, (255,255,255), (0,0,0))
    # chooseMapButton = font.render("Choose Map", True, (255,255,255), (0,0,0))
    # welcome = font.render("Welcome!", True, (255,255,255), (0,0,0))
    # screen.blit(quitButton,(400,600))
    # screen.blit(welcome, (250, 100))
    # screen.blit(chooseMapButton, (300,600))
    pass

    pygame.font.init()
    #intro_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, vsync=1)
    pygame.display.set_caption("Loosey Goosey")
    pygame.image.load("assets/title.png")
    screen.fill((0,0,0))
    quitButton = font.render("Quit", True, (255,255,255), (0,0,0))
    chooseMapButton = font.render("Choose Map", True, (255,255,255), (0,0,0))
    welcome = font.render("Welcome!", True, (255,255,255), (0,0,0))
    screen.blit(quitButton,(400,600))
    screen.blit(welcome, (250, 100))
    screen.blit(chooseMapButton, (300,600))

def play_map(gamestate: GameState, screen, fpsClock, fps):
    playMusic(gamestate.maps.get_selected_map().audio)

    while gamestate.entered_map:
        update_game(gamestate)
        draw_game(screen, gamestate)
        fpsClock.tick(fps)

def update_titlescreen(gamestate: GameState) -> None:
    for event in pygame.event.get():
        if event.type  == QUIT:
            gamestate.playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cursor_x, cursor_y = pygame.mouse.get_pos()
            print(gamestate.leftarrow.get_rect())
            if gamestate.LARROW_RECT.collidepoint(cursor_x, cursor_y):
                gamestate.maps.select_prev()
            if gamestate.RARROW_RECT.collidepoint(cursor_x, cursor_y):
                gamestate.maps.select_next()
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_RETURN:
                    gamestate.reset_map_gamestate(gamestate.maps.get_selected_map())
                    gamestate.entered_map = True
                case pygame.K_LEFT:
                    gamestate.maps.select_prev()
                case pygame.K_RIGHT:
                    gamestate.maps.select_next()
def draw_titlescreen(screen: pygame.Surface, gamestate: GameState):
    # screen.fill((0,0,0))
    screen.blit(gamestate.titlebackground, (0, 0))
    quitButton = gamestate.font.render("Quit", True, (255,255,255), (0,0,0))
    chooseMapButton = gamestate.font.render(gamestate.maps.get_selected_map().title, True, (255,255,255), (0,0,0))
    welcome = gamestate.font.render("Welcome!", True, (255,255,255), (0,0,0))
    pressSpaceToPlay = gamestate.font.render("Press Enter to Play!", True, (255,255,255), (0,0,0))
    screen.blit(quitButton,(400,750))
    screen.blit(welcome, (250, 100))
    screen.blit(chooseMapButton, (300,600))
    screen.blit(pressSpaceToPlay, (350, 500))
    screen.blit(gamestate.leftarrow, (gamestate.LARROW_X, gamestate.ARROW_Y))
    screen.blit(gamestate.rightarrow, (gamestate.RARROW_X, gamestate.ARROW_Y))
    pygame.display.update()

def main():
    pygame.init()
    pygame.font.init()

    gamestate = GameState()
    
    print(gamestate)

    
    fps = FPS
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, vsync=1)

    pygame.display.set_caption("Loosey Goosey")
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED, vsync=1)
    screen.fill(BG_COLOR)
    pygame.display.update()

    #goose = pygame.image.load(), upload goose images to repo to pull
    while gamestate.playing:
        update_titlescreen(gamestate)
        
        if gamestate.entered_map:
            play_map(gamestate, screen, fpsClock, fps)
        
        draw_titlescreen(screen, gamestate)
        fpsClock.tick(fps)



if __name__ == "__main__":
    main()
