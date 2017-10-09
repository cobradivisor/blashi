import pytest
import blashi
from blashi import Map

def test_should_output_a_border_with_an_empty_map(capsys):
    m = Map()
    m.load("tests/maps/empty_map.json")
    m.output()  
    out,_ = capsys.readouterr()
    expected_output = Map().horizontal_border + "\n" + Map().horizontal_border
    assert expected_output in out

def test_exception_thrown_if_map_file_does_not_exist():
    m = Map()
    with pytest.raises(IOError):
        m.load("bogus.file")

def test_should_create_2_by_2_map_with_no_objects(capsys):
    m = Map()
    m.load("tests/maps/simple_map.json")
    m.output()
    out,n = capsys.readouterr()
    expected_output = Map().horizontal_border + "\n- XX XX\n- XX XX\n" + Map().horizontal_border
    assert expected_output in out    
