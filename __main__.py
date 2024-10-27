import arcade
from game.gameplay import *

"""
File: __main__.py
This file runs the Asteroids game.
"""

# Creates the game and starts it going
window = Gameplay(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()