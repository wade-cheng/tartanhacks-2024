BG_COLOR = (255, 255, 255)
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
FPS = 60

BEATS_ON_SCREEN = 12 # how far ahead do we want to display notes
SQUASHER_BAR_X = SCREEN_WIDTH * 0.3 # width of goose and also the hit bar 
NOTESTREAM_Y = int(SCREEN_HEIGHT * 0.5) # height of notes on screen
BEAT_WIDTH = int(SCREEN_WIDTH/BEATS_ON_SCREEN)

HIT_EFFECT_TIMER = int(0.5 * FPS)
GOOSE_SQUASH_TIMER = int(0.25 * FPS)

ACCURACY_BUFFER = 20 # in pixels 