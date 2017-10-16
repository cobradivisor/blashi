import pytest
import blashi
from blashi import Map
from pygame.rect import Rect as Rectangle
def test_balishi_main(capsys):
    game_map = Map()
    game_map.load("tests/maps/empty_map.json")  
    game_map.output()
    out,_ = capsys.readouterr()
    expected_output = game_map.horizontal_border + "\n" + game_map.horizontal_border
    assert expected_output in out

def test_balishi_create_grid_with_one_element():
    grid = blashi._create_grid(100,100,1,1)
    assert grid == [[Rectangle(0,0,100,100)]]

def test_balishi_create_grid_with_2_X_2():
    grid = blashi._create_grid(100,100,2,2)
    print grid
    assert grid == [ [Rectangle(0,0,50,50), Rectangle(50,0,50,50)], [Rectangle(0,50,50,50), Rectangle(50,50,50,50)] ]
