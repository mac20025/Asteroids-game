import arcade
import math
import random
from game.constants import *
from game.point import *
from game.velocity import *
from game.space_object import *
from game.ship import *
from game.asteroid import *
from game.big_asteroid import *
from abc import ABC
from abc import abstractmethod

class SmallAsteroid(Asteroid):
    """Sets a SmallAsteroid class to represent the small space asteroids."""
    def __init__(self, x, y, dx, dy):
        """Initializes values from parent class"""
        super().__init__()
        """Initializes as a point in the same position as the asteroid it came from"""
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy
        self.radius = SMALL_ASTEROID_RADIUS
        self.hits_left = 1        
        self.texture = arcade.load_texture("./images/meteorGrey_small1.png")
        self.width = self.texture.width
        self.height = self.texture.height 
        self.point_awarded = 5           
        self.spinning = SMALL_ASTEROID_SPIN
        self.damage = 1

    
    
    def gotHit(self):        
        """When the asteroid is hit, its not alive anymore, and returns the points awarded. It also splits into two medium asteroids and one small asteroid."""
        arcade.play_sound(self.sound)
        self.alive = False  
        asteroid_list = []
        return asteroid_list 

    def award(self):
        """Return points awarded"""
        return self.point_awarded