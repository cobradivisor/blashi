#!/usr/bin/env python
import json
from pprint import pprint

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

def start_game(map_file):
    game_map = Map()
    game_map.load(map_file)

    game_map.output()
    
def main(story_file):
    start_game(story_file)

if __name__ == "__main__":
    main(sys.argv[1])
