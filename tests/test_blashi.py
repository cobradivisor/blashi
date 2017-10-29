import pytest
import blashi
import pygame
from blashi import Map
from pygame.rect import Rect as Rectangle
def test_balishi_main(capsys):
    game_map = Map()
    game_map.load("tests/maps/empty_map.json")  
    game_map.output()
    out,_ = capsys.readouterr()
    expected_output = game_map.horizontal_border + "\n" + game_map.horizontal_border
    assert expected_output in out

def test_map_default_width_height():
    assert Map().width == 100
    assert Map().height == 100

def test_map_assigns_grid_to_board():
    game_map = Map(100,100)
    game_map.load("tests/maps/simple_map.json")
    assert len(game_map.board['rows']) == 2
    assert len(game_map.board['rows'][0]) == 1    
    assert game_map.board['rows'][0][0]['rect'] == Rectangle(0,0,100,50)
    assert game_map.board['rows'][1][0]['rect'] == Rectangle(0,50,100,50)

def test_map_assigns_grid_to_board_2_X_1():
    game_map = Map(100,100)
    game_map.load("tests/maps/variable_columns_map.json")    
    assert len(game_map.board['rows']) == 2
    assert len(game_map.board['rows'][0]) == 2
    assert len(game_map.board['rows'][1]) == 1    
    assert game_map.board['rows'][0][0]['rect'] == Rectangle(0,0,50,50)
    assert game_map.board['rows'][0][1]['rect'] == Rectangle(50,0,50,50)
    assert game_map.board['rows'][1][0]['rect'] == Rectangle(0,50,50,50)

