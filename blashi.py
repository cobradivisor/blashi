#!/usr/bin/env python
import json
import sys
from pprint import pprint
import pygame

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

def _start_gui():

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
 
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Blashi")
    img = pygame.image.load('pics/cannon.png')
    done = False
 
    clock = pygame.time.Clock()
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
        screen.fill(WHITE)
        screen.blit(img, pygame.rect.Rect(0,0, 16, 16))
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()

def start_game(map_file):
    game_map = Map()
    game_map.load(map_file)

    game_map.output()

    _start_gui()
    
def main(story_file):
    start_game(story_file)

if __name__ == "__main__":
    main(sys.argv[1])
