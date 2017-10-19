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
    def _output_rows(self, rows):
        for row in rows:
            print "- " + row.get('text','unknown') + "-" + str(row.get('hit_points',0)) 

    def output(self):
        print self.horizontal_border 
        self._output_rows(self.board.get('rows',[]))
        print self.horizontal_border

    def load(self, f):
        with open(f) as data_file:    
            self.board = json.load(data_file)

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
    return (2,2)

def _draw_board(screen,grid,img):

    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    for row in grid:
        for rect in row: 
            img = pygame.transform.scale(img, (rect.size))
            screen.blit(img, rect)

def _start_gui(board):

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    width = 700
    height = 500 
    size = (width, height)
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Blashi")
    img = pygame.image.load('pics/cannon.png')
    done = False
 
    clock = pygame.time.Clock()

    number_of_rows,number_of_columns = _size_board(board)

    grid = _create_grid(width,height,number_of_rows, number_of_columns)
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        _draw_board(screen,grid,img) 
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()

def start_game(map_file):
    game_map = Map()
    game_map.load(map_file)

    game_map.output()

    _start_gui(game_map)
    
def main(story_file):
    start_game(story_file)

if __name__ == "__main__":
    main(sys.argv[1])
