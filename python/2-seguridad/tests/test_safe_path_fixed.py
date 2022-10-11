import pytest
from safe_path_fixed import safe_path
from pathlib import Path


home = str(Path.home())
dir_path = home + '/code/curso-seguridad-2022/teoricos-aplicaciones-seguras-2022/python'


def test_valid_path():
    filename = 'file.jpg'
    res = safe_path(filename)
    assert res == dir_path + '/file.jpg'


def test_invalid_path():
    filename = '../secret'
    with pytest.raises(ValueError) as exc_info:
        safe_path(filename)


def test_invalid_path2():
    filename = '/secret'
    with pytest.raises(ValueError) as exc_info:
        safe_path(filename)


def test_invalid_path3():
    filename = './../file.jpg'
    with pytest.raises(ValueError) as exc_info:
        safe_path(filename)
