# -*- coding: utf-8 -*-
"""
Test functions.
"""
from ninja_passwd.functions import gnrtr


def test_generator_length():
    """
    Testing length of generato is correct.
    """
    result = gnrtr(5)
    assert len(result) == 5
