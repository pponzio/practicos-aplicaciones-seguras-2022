from html_attrs_fixed import create_html_page_colored_text


def test_get_color_ok():
    url = 'https://www.example.com/page?color=green'
    contents = create_html_page_colored_text(url)
    assert contents == '<h1 style="color:green">This is colorful text.</h1>'


def test_get_color_exploit():
    url = 'https://www.example.com/page?color=green"><SCRIPT>alert("Gotcha!")</SCRIPT><span id="dummy'
    contents = create_html_page_colored_text(url)
    print('\n', contents)
    #  Expected:
    #  <h1 style="color:green&quot;&gt;&lt;SCRIPT&gt;alert(&quot;Gotcha!&quot;)&lt;/SCRIPT&gt;&lt;span id=&quot;dummy">
    #   This is colorful text.
    #  </h1>
