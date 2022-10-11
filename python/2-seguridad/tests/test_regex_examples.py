import re


def test_regex_example():
    text = "Argentina ganó el mundial en los años 1978 y 1986"
    first = re.search("\d\d\d\d", text)
    assert "1978" == first.group()


def test_regex_example2():
    text = "Argentina ganó el mundial en los años 1978 y 1986"
    res = re.findall("\d\d\d\d", text)
    assert ['1978', '1986'] == res


def test_regex_example3():
    text = "El primer número es 7473, el segundo 29 y 378 es el tercero."
    res = re.findall("\d+", text)
    assert ['7473', '29', '378'] == res


def test_regex_example4():
    text = "Pepe tiene DNI 7.983.567 y Juan DNI 14.342.055"
    res = re.findall("\d?\d\.\d\d\d\.\d\d\d", text)
    assert ['7.983.567', '14.342.055'] == res


def test_regex_example5():
    text = "Pepe tiene DNI 7.983.567 y Juan DNI 14.342.055"
    res = re.findall("\d{1,2}\.\d{3,3}\.\d{3,3}", text)
    assert ['7.983.567', '14.342.055'] == res



