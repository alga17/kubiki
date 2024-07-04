import json
from player import Cube
def test_init():
    a = Cube()
    assert a.side in ['tank', 'deathray', 'deathray', 'human', 'cow', 'chicken']
    b = Cube('tank')
    assert b.side == 'tank'

def test_repr():
    c = Cube()
    assert type(c) == Cube

def test_load():
    x = Cube.load('tank')
    assert x.up == 'tank'

