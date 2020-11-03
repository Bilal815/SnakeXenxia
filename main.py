import pygame, sys

#   clear the program
#   update the game
#   draw the game


#   1)  Behaviour
#   2)  Constants
#   3)  Data Definitons
#   4)  Functions

'''
    Behaviours:-
        Gameover:
            - snake hits the edge of the screen
            - snake touches itself
        Snake Movement:
            - body trails its head
        Snake:
            - Eats food and grows by one
        Score:
            - How much food has been eaten
        Menu Screen:
            - Shows one time at the beginning of game
            - disappears on any keypress
        Game over:
            - Displays when snake hits wall or eats itself
            - will go back a new game on any keypress
        Key input:
            - arrow keys and wasd change snake direction

'''


'''
Constants:-
    - Colors
    - Window dimensions
    - size of cells
    - frame rate
    - Cell width and height
'''

# [{"x": 1, "y": 2}]


pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600))
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Wormy')

def main():
    game = Game()
    game.run()
    sys.exit