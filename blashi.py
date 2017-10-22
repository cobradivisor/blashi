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

    def _load_grid(self):
        number_of_rows,number_of_columns = self._size_board()
        if number_of_rows > 0 and number_of_columns > 0:
            grid_height = self.height/number_of_rows
            grid_width = self.width/number_of_columns
            for row_index, row in enumerate(self.board['rows']):
                for column_index, item in enumerate(row):
                    item['rect'] = Rectangle(column_index*grid_width,row_index*grid_height,grid_width,grid_height)

    def _size_board(self):
        max_number_of_columns = 0
        for row in self.board["rows"]:
            max_number_of_columns = max(max_number_of_columns,len(row)) 
        return (len(self.board["rows"]),max_number_of_columns)

    def output(self):
        print self.horizontal_border 
        self._output_rows(self.board['rows'])
        print self.horizontal_border

    def load(self, f):
        with open(f) as data_file:    
            self.board = json.load(data_file)

        if "rows" not in self.board:
            self.board["rows"] = []

        self._load_grid()

def _draw_board(screen,board):
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    for row_index,row in enumerate(board['rows']):
        for column_index,item in enumerate(row):
            img = pygame.image.load(item['pic'])
            img = pygame.transform.scale(img, item['rect'].size)
            screen.blit(img, item['rect'])

def _add_grid_to_board(grid,board):
    pass

def _start_gui(game_board):

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    size = (game_board.width, game_board.height)
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Blashi")
    done = False
 
    clock = pygame.time.Clock()
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        _draw_board(screen,game_board.board) 
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()

def start_game(map_file):
    game_map = Map(700,500)
    game_map.load(map_file)

    game_map.output()

    _start_gui(game_map)
    
def main(map_file):
    start_game(map_file)

if __name__ == "__main__":
    main(sys.argv[1])
