from game.big_asteroid import *

class Gameplay(arcade.Window):
    """
    This class handles all the gameplay.
    This class will then call the appropriate functions of
    each of the other classes.    
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.alive = True
        
        self.held_keys = set()

        self.background = arcade.load_texture("./images/nebula.jpg")

        self.background_y_offset = 0  # Starting position for background

        self.ship = Ship()

        self.score = 0     

        self.lasers = []

        self.asteroids = []          

        self.create_asteroids()   

    def create_asteroids(self):
        """Creates targets as asteroids"""
        for i in range(INITIAL_ASTEROID_COUNT):
            asteroid = BigAsteroid()
            self.asteroids.append(asteroid)      

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        
        arcade.start_render()

        # Draws the background twice for looping effect
        arcade.draw_lrwh_rectangle_textured(
            0, self.background_y_offset, SCREEN_WIDTH, SCREEN_HEIGHT, self.background
        )
        arcade.draw_lrwh_rectangle_textured(
            0, self.background_y_offset + SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, self.background
        )

        self.ship.draw()        
            
        for asteroid in self.asteroids:
            asteroid.draw()              

        for laser in self.lasers:
            laser.draw()            

        self.draw_score()  

        self.draw_status()

        if self.ship.lives <= 0:            
            self.game_over()
            self.play_again()            
        
        if self.score == 320:            
            self.victory()
            self.play_again()

        if len(self.asteroids) < 5:            
            self.create_asteroids()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 40
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=20, color=arcade.color.WHITE_SMOKE)

    def draw_status(self):
        """
        Puts the current status on the screen
        """
        status_text = "Status: {}%".format(self.ship.lives)
        start_x = SCREEN_WIDTH - 130
        start_y = SCREEN_HEIGHT - 40
        arcade.draw_text(status_text, start_x=start_x, start_y=start_y, font_size=20, color=arcade.color.YELLOW)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # Update background position based on ship's movement
        self.background_y_offset -= 2  # Adjust this value to match ship speed
        if self.background_y_offset <= -SCREEN_HEIGHT:
            self.background_y_offset = 0  # Reset to create a continuous loop

        self.ship.notWrapScreen()   
        
        for asteroid in self.asteroids:
            asteroid.spin()
            asteroid.advance()
            asteroid.wrapScreen()            

        for laser in self.lasers:
            laser.advance()    
        
        self.ship.advance()        

        self.check_collisions()

    def check_collisions(self):
        """        
        Updates scores and removes dead items.
        :return:
        """
        
        """Checks to see if lasers have hit asteroids. """
        for laser in self.lasers:
            for asteroid in self.asteroids:

                # Make sure they are both alive before checking for a collision
                if laser.alive and asteroid.alive:
                    too_close = laser.radius + asteroid.radius

                    if (abs(laser.center.x - asteroid.center.x) < too_close and
                                abs(laser.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        laser.alive = False
                        asteroid_list = asteroid.gotHit()
                        self.asteroids += asteroid_list
                        self.score += asteroid.award()
        
        """Checks if asteroids have hit the ship."""
        for asteroid in self.asteroids:   
            
            # Make sure they are both alive before checking for a collision
            if asteroid.alive and self.ship.alive:
                too_close = asteroid.radius + self.ship.radius
                
                if (abs(self.ship.center.x - asteroid.center.x) < too_close and
                            abs(self.ship.center.y - asteroid.center.y) < too_close):
                    # its a hit!
                    self.ship.gotHit()                                                                                                    
                    self.ship.lives -= asteroid.hit()                    

        """Checks if lasers have hit the ship."""
        for laser in self.lasers:   
            """Only lasers fired more than 30 frames ago will hit the ship"""
            # Make sure they are both alive before checking for a collision
            if laser.alive and laser.lifespan < 30 and self.ship.alive:
                too_close = laser.radius + self.ship.radius
                
                if (abs(self.ship.center.x - laser.center.x) < too_close and
                            abs(self.ship.center.y - laser.center.y) < too_close):
                    # its a hit!                                                                                                    
                    self.ship.gotHit()
                    self.ship.lives -= laser.hit()                    
                        # We will wait to remove the dead objects until after we
                        # finish going through the list
        
        """Checks if the ship is still alive"""
        if self.ship.lives <= 0:
            self.ship.alive = False            

        # Now, check for anything that is dead, and remove it
        self.cleanup()

    def cleanup(self):
        """
        Removes any dead lasers or targets from the list.
        :return:
        """
        for laser in self.lasers:            
            laser.is_alive()
            if laser.alive == False:
                self.lasers.remove(laser)        

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)         

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """        

        if arcade.key.LEFT in self.held_keys:
            self.ship.left_arrow()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.right_arrow()

        if arcade.key.UP in self.held_keys:
            self.ship.up_arrow()

        if arcade.key.DOWN in self.held_keys:
            self.ship.down_arrow()

        if arcade.key.SPACE in self.held_keys:            
            laser = self.ship.laser()
            self.lasers.append(laser)
            self.held_keys.remove(arcade.key.SPACE)

    def on_key_press(self, key, modifiers):
        """
        Puts the current key in the set of keys that are being held.        
        """
        if self.ship.alive:
            self.held_keys.add(key)   

        if self.alive == False and key == arcade.key.Y:
            self.restart()
        elif self.alive == False and key == arcade.key.N:
            arcade.close_window()    

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)                  

    def game_over(self):
        """When lives run out, the game is over"""
        game_over_message = "Game Over"
        game_over_message_x = 0
        game_over_message_y = SCREEN_HEIGHT // 2
        arcade.draw_text(game_over_message, start_x=game_over_message_x, start_y=game_over_message_y, font_size=80, color=arcade.color.WHITE, width=SCREEN_WIDTH, align="center")

    def victory(self):
        """When all asteroids are destroyed, it's victory"""
        victory_message = "Victory!"
        victory_message_x = 0
        victory_message_y = SCREEN_HEIGHT // 2
        arcade.draw_text(victory_message, start_x=victory_message_x, start_y=victory_message_y, font_size=80, color=arcade.color.WHITE, width=SCREEN_WIDTH, align="center")

    def play_again(self):
        """Asks plays if they want to play again"""
        self.alive = False
        play_again_message = "Want to play again? (Press Y or N)"
        play_again_message_x = 0
        play_again_message_y = SCREEN_HEIGHT // 2 - 100
        arcade.draw_text(play_again_message, start_x=play_again_message_x, start_y=play_again_message_y, font_size=30, color=arcade.color.WHITE, width=SCREEN_WIDTH, align="center")
        
    def restart(self):
        """Restarts the game on pressing Y"""
        
        self.alive = True        
        self.held_keys = set()
        self.background = arcade.load_texture("./images/nebula.jpg") #This is one of my above and beyond functionality. I decided to include a space picture as background instead of a black background.
        self.ship = Ship()
        self.score = 0     
        self.lasers = []
        self.asteroids = []  
        self.create_asteroids()