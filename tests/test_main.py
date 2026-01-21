import pytest
from src.main import add


def test_add_valid_integers():
    assert add(7, 2) == 9
    assert add(1, 6, 3) == 10
    assert add(0, 0, 0) == 0
    assert add(10, 0, 0) == 10
    assert add(10, 10, 10) == 30


def test_add_valid_floats():
    assert add(1.5, 2.5) == 4.0
    assert add(1.2, 3.4, 5.6) == 10.2
    assert add(0.0, 10.0, 0.0) == 10.0


def test_add_type_error_returns_minus_1():
    assert add("1", 2) == -1
    assert add(1, "2", 3) == -1
    assert add(1, 2, "3") == -1
    assert add(None, 2, 3) == -1
    assert add(1, None, 3) == -1
    assert add(1, 2, None) == -1


def test_add_out_of_range_returns_minus_2():
    assert add(-0.1, 2, 3) == -2
    assert add(0, 10.1, 0) == -2
    assert add(0, 0, 11) == -2
    assert add(10, 10, -1) == -2


def test_add_type_error_priority_over_range():
    # 型がダメなら -1（範囲以前）
    assert add("100", 2, 3) == -1
    assert add(1, 2, "11") == -1
