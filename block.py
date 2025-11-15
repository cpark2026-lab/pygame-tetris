from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, block_id):
        # to distinguish between different blocks
        self.block_id = block_id
        # to represent the cells that the block occupies in a 4x4 grid for all rotation states
        self.shapes = {}

        self.size = 30

        self.dy = 0
        self.dx = 0

        self.rotation_state = 0 
        self.colors = Colors.get_cell_colors()

    def move(self, delta_row, delta_col):
        # print("move method in block.py file")
        self.dy += delta_row
        self.dx += delta_col

    def get_cell_positions(self):
        # print("get_cell_position in block.py file")
        # print(self.rotation_state)
        current_shape = self.shapes[self.rotation_state]
        # print(tiles[0].row)
        move_tiles = []
        for pos in current_shape:
            # print(position.row)
            # print(position.column)
            # 새로운 포지션객체를 만드는데 거에 row는 이전 포지션 + 새로운 row offset, column은 이전 column + column offset
            new_pos = Position(pos.row + self.dy, pos.column + self.dx)
            move_tiles.append(new_pos)
            # print(move_tiles[0].row)
        return move_tiles

    def draw(self, screen):
        # print("draw method in block.py file")
        # we need to set the position
        # tiles = self.cells[self.rotation_state]
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.size + 1, tile.row * self.size + 1, self.size - 1, self.size - 1)
            pygame.draw.rect(screen, self.colors[self.block_id], tile_rect)
        

    def rotate(self):
        self.rotation_state += 1
        print(self.rotation_state)
        if self.rotation_state == len(self.shapes):
            self.rotation_state = 0       

    def undo_rotation(self):
        if self.rotation_state == 0:
            if len(f"{self.shapes = }") == 0:
                self.rotation_state = 0
            self.rotation_state = len(self.shapes) -1
        else:
            self.rotation_state -= 1
        
