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
from game.small_asteroid import *
from abc import ABC
from abc import abstractmethod

class MediumAsteroid(Asteroid):
    """Sets a MediumAsteroid class to represent the medium space asteroids."""
    def __init__(self, x, y, dx, dy):
        """Initializes values from parent class"""
        super().__init__()
        """Initializes as a point in the same position as the BigAsteroid it came from"""
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy
        self.radius = MEDIUM_ASTEROID_RADIUS
        self.hits_left = 1        
        self.texture = arcade.load_texture("./images/meteorGrey_med1.png")
        self.width = self.texture.width
        self.height = self.texture.height 
        self.point_awarded = 3          
        self.spinning = MEDIUM_ASTEROID_SPIN   
        self.damage = 2 
    
    
    
    def gotHit(self):        
        """When the asteroid is hit, its not alive anymore, and returns the points awarded. It also splits into two medium asteroids and one small asteroid."""
        arcade.play_sound(self.sound)
        self.alive = False        
        small_asteroid_1 = SmallAsteroid(self.center.x, self.center.y, self.velocity.dx + 5.5, self.velocity.dy + 5.5)
        small_asteroid_2 = SmallAsteroid(self.center.x, self.center.y, self.velocity.dx - 5.5, self.velocity.dy - 5.5)
        
        asteroid_list = [small_asteroid_1, small_asteroid_2]
        return asteroid_list
    
    def award(self):
        """Return points awarded"""
        return self.point_awarded