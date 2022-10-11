import re

var_regex = '^[A-Za-z_][A-Za-z0-9_]*'


def is_valid_python_var(string):
    if re.search(var_regex, string):
        return True
    else:
        return False
