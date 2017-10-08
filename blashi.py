#!/usr/bin/env python


class Map(object):
    horizontal_border = "--------------------------------------"

    def output(self):
        print self.horizontal_border 
        print "-"
        print "-"
        print self.horizontal_border

    def load(self, f):
        pass
    
def start_game(m):
    game_map = Map()
    with open(m,'r') as map_file:
        game_map.load(map_file)

    game_map.output()
    
def main(story_file):
    start_game(story_file)

if __name__ == "__main__":
    main(sys.argv[1])
