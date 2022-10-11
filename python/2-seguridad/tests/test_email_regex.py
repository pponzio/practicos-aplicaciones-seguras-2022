import re

import pytest


def test_regex_email1():
    text = "user alice@google.com has sent you an email"
    match = re.search("\w+@\w+\.\w+", text)
    assert match is not None
    assert "alice@google.com" == match.group()


def test_regex_email2():
    text = "user invalid_name has sent you an email"
    match = re.search(r"\w+@\w+.\w+", text)
    assert match is None


def test_regex_email3():
    text = "user bob-gordon@google.com has sent you an email"
    match = re.search(r"[\w\-]+@\w+.\w+", text)
    assert match is not None
    assert "bob-gordon@google.com" == match.group()


