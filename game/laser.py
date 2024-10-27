import arcade
import math
from game.constants import *
from game.point import *
from game.velocity import *
from game.space_object import *
from game.laser import *


class Laser(SpaceObject):
    """Defines the child class Laser, related to the SpaceObject parent class"""
    def __init__(self, angle, x, y, dx, dy):        
        """Initializes values from parent class"""
        super().__init__()
        """Initializes laser"""        
        self.center.x = x
        self.center.y = y
        self.rotation = angle
        self.angle = angle
        self.ship_dx = dx
        self.ship_dy = dy
        self.velocity.dx = math.cos(math.radians(self.rotation)) * LASER_SPEED
        self.velocity.dy = math.sin(math.radians(self.rotation)) * LASER_SPEED
        self.texture = arcade.load_texture("./images/laserBlue01.png")
        self.width = self.texture.width
        self.height = self.texture.height        
        self.radius = LASER_RADIUS
        self.sound = arcade.load_sound("./sounds/lasersound.wav")        
        self.lifespan = LASER_LIFE
        self.damage = 1

    def is_alive(self):
        """Descreases lifespan by 1 per frame. When lifespan reaches 0, kills the laser."""
        self.lifespan -= 1

        if self.lifespan == 0:
            self.alive = False
    
    def hit(self):
        """Kills the laser and causes 1 damage"""
        self.alive = False
        return self.damage

    def fire(self):
        """The laser produces sound when shot"""
        arcade.play_sound(self.sound)