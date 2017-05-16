#!/usr/local/bin/python3

import sys, tty, time, termios

from game import Game, Action
from constants import *


def getch():
    import termios, sys, tty
    
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return ch


game = Game()

while True:
    print('\n' * 100 + game.draw() + '\n')
    time.sleep(MIN_TICK_LENGTH)
    if game.game_over or game.draw_flag:
        break
    if game.show_help:
        s = input()
        game.tick(None)
        continue
    
    command = True
    while command and not(command in ['a', 'w', 'd', 'q']):
        command = getch()
    
    if not command:
        break
    
    if command == 'q':
        break
    elif command == 'a':
        action = Action.MOVE_LEFT
    elif command == 'd':
        action = Action.MOVE_RIGHT
    else:
        action = None
    
    game.tick(action)

