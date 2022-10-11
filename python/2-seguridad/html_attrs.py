from urllib.parse import parse_qs, urlparse


def get_attribute_value(url, attr):
    parts = urlparse(url)
    query_params = parse_qs(parts.query)  # self.parts.query)
    value = query_params.get(attr)[0]
    return value


def create_html_page_colored_text(url):
    unsafe_color = get_attribute_value(url, 'color')
    contents = '<h1 style="color:%s">This is colorful text.</h1>' % unsafe_color
    return contents

