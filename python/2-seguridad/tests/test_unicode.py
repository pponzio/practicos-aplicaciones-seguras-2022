import unicodedata
from sqlescapy import sqlescape


def test_unicode_encoding():
    latin_c = '\u00C7'
    latin_c2 = '\u0043\u0327'
    assert latin_c != latin_c2


def test_unicode_encoding_norm():
    latin_c = '\u00C7'
    latin_c2 = '\u0043\u0327'
    norm_latin_c = unicodedata.normalize("NFKD", latin_c)
    norm_latin_c2 = unicodedata.normalize("NFKD", latin_c2)
    assert norm_latin_c == norm_latin_c2


def test_unicode_case_conversion():
    c1 = 'foo@mıx.com'
    c2 = 'foo@mix.com'
    assert c1 != c2
    C1 = c1.upper()
    C2 = c2.upper()
    assert C1 == C2


def test_unicode_quotation_mark():
    q = "\uFF07"
    real_q = "'"  # \u0027
    assert q != real_q
    norm_q = unicodedata.normalize("NFKD", q)
    assert norm_q == real_q


def test_unicode_normalization_sql_injection():
    injection_str = "chloe\uFF07); DROP TABLE Students; --"
    esc_injection_str = sqlescape(injection_str)
    assert esc_injection_str == injection_str
    norm_injection_str = unicodedata.normalize("NFKD", esc_injection_str)
    assert norm_injection_str == "chloe'); DROP TABLE Students; --"
