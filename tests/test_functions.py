# -*- coding: utf-8 -*-
"""
Test functions.
"""
from ninja_passwd.functions.gnrtr import random_string


def test_generator_length():
    """
    Testing length of generato is correct.
    """
    result = random_string(5)
    assert len(result) == 5
