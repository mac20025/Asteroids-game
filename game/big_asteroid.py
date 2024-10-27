import arcade
from game.constants import *
from game.point import *
from game.velocity import *
from game.space_object import *
from game.ship import *
from game.asteroid import *
from game.medium_asteroid import *
from game.small_asteroid import *
from abc import abstractmethod

class BigAsteroid(Asteroid):
    """Sets a BigAsteroid class to represent the big space asteroids."""
    def __init__(self):
        """Initializes values from parent class"""
        super().__init__()
        """Initializes as a point in a random position"""
        self.radius = BIG_ASTEROID_RADIUS
        self.hits_left = 1        
        self.texture = arcade.load_texture("./images/meteorGrey_big1.png")
        self.width = self.texture.width
        self.height = self.texture.height
        self.point_awarded = 1
        self.damage = 3
        self.spinning = BIG_ASTEROID_SPIN          
        
    
    def gotHit(self):        
        """When the asteroid is hit, its not alive anymore, and returns the points awarded. It also splits into two medium asteroids and one small asteroid."""
        arcade.play_sound(self.sound)
        self.alive = False        
        medium_asteroid_1 = MediumAsteroid(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy + 3)
        medium_asteroid_2 = MediumAsteroid(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy - 3)
        small_asteroid_1 = SmallAsteroid(self.center.x, self.center.y, self.velocity.dx + 5, self.velocity.dy)
        asteroid_list = [medium_asteroid_1, medium_asteroid_2, small_asteroid_1]
        return asteroid_list

    def award(self):
        """Return points awarded"""
        return self.point_awarded