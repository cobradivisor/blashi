import pytest
import blashi
from blashi import Map

def test_balishi_main(capsys):
    blashi.start_game("tests/maps/empty_map.json")  
    out,_ = capsys.readouterr()
    expected_output = Map().horizontal_border + "\n-\n-\n" + Map().horizontal_border
    assert expected_output in out

def test_exception_thrown_if_map_file_does_not_exist():
    with pytest.raises(IOError):
        blashi.start_game("bogus.file")
