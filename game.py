from grid import Grid
from blocks import *
import random
from block import *

class Game:
    def __init__(self):
        self.grid = Grid()
        # to create an attribute to hold the current block that is visible on the screen
        # we have to select a random block from all the available blocks
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.choice = [1, 2, 3, 4, 5, 6, 7]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.gameover = False
    
    def get_random_block(self):
        # if len(self.choice) == 0:
        #     self.choice = [1, 2, 3, 4, 5, 6, 7]
        # random_value = random.choice(self.choice)
        # self.choice.remove(random_value)
        # return self.blocks[random_value - 1]
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        # tils is cotaining all the position intances of current block
        for tile in tiles:
            # if its I block our for loop will loop 4 times
            # first loop : first tile
            # second loop : second tile
            if self.grid.is_inside(tile.row, tile.column) == False:
                print("not insde inside")
                return False
        print("inside inside")
        return True
    
    # def move_left(self):
    #     self.current_block.move(0, -1)

    # def move_right(self):
    #     self.current_block.move(0, 1)

    # def move_down(self):
    #     self.current_block.move(1, 0)

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        """
        Moves the current block one column to the right.
        If the movement causes the block to go outside the game boundaries
        or overlap with existing blocks, it reverts the move.
        """
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        """
        Moves the current block one row down.
        If the movement causes the block to go outside the game boundaries
        or overlap with existing blocks, it reverts the move and locks the block in place.
        """
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()


    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
    
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            print("not inside")
            self.current_block.undo_rotation()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.block_id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full_rows()
        if self.block_fits() == False:
            self.gameover = True

    
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
    
    def reset(self):
        self.grid.reset()
        
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()