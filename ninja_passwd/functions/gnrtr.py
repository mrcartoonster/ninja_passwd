# -*- coding: utf-8 -*-
"""
Random string function.
"""

import secrets
import string

# Characters
character = "".join([string.ascii_letters, string.punctuation[:21]])


def random_string(x: int) -> list[str]:
    """
    String generator.
    """
    return "".join([secrets.choice(character) for _ in range(x)])
