import textwrap


def pretty_print(str):
    return textwrap.fill(str)


def test_xml_expression_too_large():
    """
        big7 = '&big7;&big7;&big7;&big7;&big7;&big7;&big7;&big7;'
        big6 = '&big6;&big6;&big6;&big6;&big6;&big6;&big6;&big6;'
        big5 = '&big5;&big5;&big5;&big5;&big5;&big5;&big5;&big5;'
        big4 = '&big4;&big4;&big4;&big4;&big4;&big4;&big4;&big4;'
        big3 = '&big3;&big3;&big3;&big3;&big3;&big3;&big3;&big3;'
        big2 = '&big2;&big2;&big2;&big2;&big2;&big2;&big2;&big2;'
        big1 = 'big!'
    """

    res = '&big7;&big7;&big7;&big7;&big7;&big7;&big7;&big7;'.replace(
                '&big7;', '&big6;&big6;&big6;&big6;&big6;&big6;&big6;&big6;')
    l1 = len(res)
    print('\n', pretty_print(res))

    res = res.replace('&big6;', '&big5;&big5;&big5;&big5;&big5;&big5;&big5;&big5;')
    l2 = len(res)
    print('\n', pretty_print(res))

    res = res.replace('&big5;', '&big4;&big4;&big4;&big4;&big4;&big4;&big4;&big4;')
    print('\n', pretty_print(res))
    l3 = len(res)

    res = res.replace('&big4;', '&big3;&big3;&big3;&big3;&big3;&big3;&big3;&big3;')
    print('\n', pretty_print(res))
    l4 = len(res)

#    res = res.replace('&big3;', '&big2;&big2;&big2;&big2;&big2;&big2;&big2;&big2;')
#    print('\n', pretty_print(res))
#    l5 = len(res)

    print(l1, l2, l3, l4)
