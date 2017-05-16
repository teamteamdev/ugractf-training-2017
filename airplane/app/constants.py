from sprite import Sprite


LANES_NUMBER = 3
LANE_WIDTH = 25
CANVAS_HEIGHT = 23
SHOW_FLAG_AFTER = 15000

LANE_SYMBOL = '|'
HELP_SPRITE = Sprite.from_file('help.txt')
BALLOON_SPRITE = Sprite.from_file('balloon.txt')
PLANE_SPRITE = Sprite.from_file('plane.txt')
GAME_OVER_SPRITE = Sprite('You are lose, game over')
FLAG_SPRITE = Sprite('uctf_you_have_won | Thanks to QCTF for this task')

DEFAULT_PORT = 8000
NO_INPUT_TIMEOUT = 50
MIN_TICK_LENGTH = 0.23
