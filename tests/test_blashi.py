import pytest
from blashi import Map

def test_balishi_main(capsys):
    game_map = Map()
    game_map.load("tests/maps/empty_map.json")  
    game_map.output()
    out,_ = capsys.readouterr()
    expected_output = game_map.horizontal_border + "\n" + game_map.horizontal_border
    assert expected_output in out

