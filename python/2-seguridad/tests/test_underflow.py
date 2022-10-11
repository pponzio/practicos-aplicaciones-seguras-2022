

def test_underflow_example():
    a = 10000000000000000.0
    b = 2
    c = 1
    print(a)
    print(a+b)
    print(a+b-c)
    print(a+b-c-a)
    assert 1 == (((a+b)-c)-a)
