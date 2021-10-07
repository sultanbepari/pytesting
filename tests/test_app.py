from app import csv2json, jpg2gif


def test_index1():
    assert csv2json() == 0

def test_index2():
    assert jpg2gif() == 0

