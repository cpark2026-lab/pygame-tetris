import pygame, sys
from grid import Grid
from blocks import *
from game import Game
# import blocks

# Initialize pygame and its modules.
pygame.init()
dark_blue_color = (44, 44, 127)

# Set up the display window with a width of 300 pixels and a height of 600 pixels.
# The display surface is stored in the variable `screen`.
screen = pygame.display.set_mode((300, 600))

# Set the title of the window to "Python Tetris".
# This text appears in the title bar of the window.
pygame.display.set_caption("Python Tetris")

# Create a clock object to control the frame rate of the game loop.
# This ensures the game runs at a consistent speed, regardless of the system's performance.
clock = pygame.time.Clock()


game = Game()

current_block = game.current_block



# user event is a special type that can create custom event.
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Start the main game loop.
# This loop will continue running until the game is exited.
while True:
    # Check for any events that have occurred (e.g., user input or system requests).
    for event in pygame.event.get():
        # If the user clicks the close button on the window,
        # the `QUIT` event is triggered.
        if event.type == pygame.QUIT:
            # Safely shut down all pygame modules to free up resources.
            pygame.quit()
            # Exit the program completely using the `sys` module.
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.gameover == True:
                game.gameover = False
                game.reset()
            if event.key == pygame.K_LEFT and game.gameover == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.gameover == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.gameover == False:
                game.move_down()
            if event.key == pygame.K_UP and game.gameover == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.gameover == False:
            game.move_down()
            pass


    # game_grid.print_grid()

    screen.fill(dark_blue_color)
    
    # grid drawing method
    game.draw(screen)

    # Update the contents of the display to reflect any changes.
    # This function must be called in every iteration of the game loop.
    pygame.display.update()
     
    # Limit the frame rate of the game loop to 50 frames per second (FPS).
    # This ensures the game runs at a controlled and smooth pace.
    clock.tick(60)



# How pygame draws on the screen?
# We have three basics concepts to learn.
# Display Surface, Surface, Rect

# Display surface is the surface where we see all the game objects
# It is like blank Canvas. We can only have one per game.
# It is created when we call the set_mode() function and it's the object
# we use when we call the update() function

# Surface is a surface that we can draw on it.
# We can have many surfaces per game.

# Rect
# Rectangles are used for positioning, collision detection and for drawing objects.

# This rectangle will be invisible but it will help us draw the cell on the screen.

