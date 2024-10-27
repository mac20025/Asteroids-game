# Overview

A simple asteroids-like game with Python.

Use arrows for movement and spacebar for shooting.

# Development Environment

For this software, I used:
- Visual Studio Code 1.91.1
- Python 3.10
- arcade library
- ABC library

# The project has 3 folders
- game: Contains the code that will run the game
- images: Contains images used for the spaceship, background, asteroids, and laser bullet.
- sounds: Contains sound effects files.

# The project is split into 12 files
- main.py: Gets the game running
- constants.py: Sets the values of a few constants used in the game
- point.py: Creates a Point class to represent the location of flying objects in an XY plan
- velocity.py: Creates a Velocity class to set flying objects movement speed
- space_object: Sets a SpaceObject class to represent commmon characteristics shared by ship, lasers and asteroids
  - ship.py: Sets a Spaceship class to represent the spaceship
  - laser.py: Defines the child class Laser, related to the SpaceObject parent class, to handle the laser bullets
  - asteroid.py: Sets a Asteroid class to represent the space asteroids
    - big_asteroid.py: Sets a BigAsteroid class to represent the big space asteroids
    - medium_asteroid.py: Sets a MediumAsteroid class to represent the medium space asteroids
    - small_asteroid.py: Sets a SmallAsteroid class to represent the small space asteroids

# Features
- User can press Y to play again or N to quit the game

# Installation Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


# Useful Websites

* [Visual Studio Code](https://code.visualstudio.com/)
* [Python](https://www.python.org/)
