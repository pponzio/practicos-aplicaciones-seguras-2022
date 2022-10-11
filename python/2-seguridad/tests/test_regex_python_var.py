from regex_python_var import is_valid_python_var


def test_valid_var1():
    var = 'abc'
    res = is_valid_python_var(var)
    assert res


def test_valid_var2():
    var = '_abc'
    res = is_valid_python_var(var)
    assert res


def test_invalid_var1():
    var = '1abc'
    res = is_valid_python_var(var)
    assert not res


def test_invalid_var2():
    var = '#abc'
    res = is_valid_python_var(var)
    assert not res