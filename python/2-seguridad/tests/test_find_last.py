import pytest

from array_routines import find_last, last_zero


def test_find_last1():
    arr = [1, 2, 3, 4]
    y = 4
    res = find_last(arr, y)
    assert 3 == res


def test_find_last2():
    arr = None
    y = 4
    with pytest.raises(ValueError) as exc_info:
        find_last(arr, y)


def test_find_last3():
    arr = [1, 2, 3, 4]
    y = 5
    res = find_last(arr, y)
    assert -1 == res


def test_find_last4():
    arr = [1, 2, 3]
    y = 1
    res = find_last(arr, y)
    assert 0 == res

