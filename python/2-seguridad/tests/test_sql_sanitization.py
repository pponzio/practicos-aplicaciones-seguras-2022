from sqlescapy import sqlescape


def test_remove_quotes():
    untrusted_input = "Robert'); DROP TABLE Students;--"
    assert untrusted_input.replace("'", "") == "Robert); DROP TABLE Students;--"


def test_sqlscape():
    example = """I don't like "special" chars -- ¯_(?)_/¯"""
    print("\n", example)
    print("\n", sqlescape(example))


def test_sql_vulnerability():
    untrusted_input = "Robert'); DROP TABLE Students;--"
    # Código vulnerable
    sql_stmt = "INSERT INTO Students (name) VALUES ('" + untrusted_input + "');"
    print("\n", sql_stmt)


def test_sql_fixed():
    untrusted_input = "Robert'); DROP TABLE Students;--"
    safe_input = sqlescape(untrusted_input)
    sql_stmt = "INSERT INTO Students (name) VALUES ('" + safe_input + "');"
    assert sql_stmt == "INSERT INTO Students (name) VALUES ('Robert); DROP TABLE Students;--');"
