#!/usr/bin/env python
import json
import sys
from pprint import pprint
import pygame
import os
from pygame.rect import Rect as Rectangle

class Map(object):
    horizontal_border = "--------------------------------------"
    board = {}
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        pass

    def _output_rows(self, rows):
        for row in rows:
            line = "-"
            for item in row:
                 line = line + " " + item.get('text','unknown') + "-" + str(item.get('hit_points',0))

            print line 

    def _load_grid(self,width,height,board):
        for row in board['rows']:
            for item in row:
                item['rect'] = Rectangle(0,0,0,0)

    def output(self):
        print self.horizontal_border 
        self._output_rows(self.board['rows'])
        print self.horizontal_border

    def load(self, f):
        with open(f) as data_file:    
            self.board = json.load(data_file)

        if "rows" not in self.board:
            self.board["rows"] = []

        self._load_grid(self.width,self.height,self.board)

def _create_grid(width,height,number_of_rows, number_of_columns):
    grid = []
    grid_height = height/number_of_rows
    grid_width = width/number_of_columns
    for r in range(number_of_rows):
        row = []
        for c in range(number_of_columns):
            row.append(Rectangle(c*grid_width,r*grid_height,grid_width,grid_height))
         
        grid.append(row)
    return grid

def _size_board(board):
    max_number_of_columns = 0
    for row in board["rows"]:
        max_number_of_columns = max(max_number_of_columns,len(row)) 
    return (len(board["rows"]),max_number_of_columns)

def _draw_board(screen,grid,board):
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    for row_index,row in enumerate(board['rows']):
        for column_index,item in enumerate(row):
            rect = grid[row_index][column_index]
            img = pygame.image.load(item['pic'])
            img = pygame.transform.scale(img, (rect.size))
            screen.blit(img, rect)

def _add_grid_to_board(grid,board):
    pass

def _start_gui(board):

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    width = 700
    height = 500 
    size = (width, height)
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Blashi")
    done = False
 
    clock = pygame.time.Clock()

    number_of_rows,number_of_columns = _size_board(board)

    grid = _create_grid(width,height,number_of_rows, number_of_columns)
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        _draw_board(screen,grid,board) 
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()

def start_game(map_file):
    game_map = Map()
    game_map.load(map_file)

    game_map.output()

    _start_gui(game_map.board)
    
def main(map_file):
    start_game(map_file)

if __name__ == "__main__":
    main(sys.argv[1])
