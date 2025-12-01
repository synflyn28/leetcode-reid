"""
Tests for code that implements the longest consecutive
subsequence LeetCode problem.

(c) Justin Reid
"""

import pytest
from scripts import longest_con

@pytest.fixture(scope='module')
def set_up():
    """
    Set up data used for these tests
    """

    return {
        'big_short': [100,4,200,1,3,2],
        'short': [1,0,1,2],
        'long': [0,3,7,2,5,8,4,6,0,1],
        'Solution': longest_con.Solution()
    }


def test_big_short(set_up):
    """
    Test data for big short list case
    """

    assert set_up['Solution'].longest_consecutive(set_up['big_short'])


def test_short(set_up):
    """
    Test data for short list case
    """

    assert set_up['Solution'].longest_consecutive(set_up['short'])


def test_long(set_up):
    """
    Test data for long list case
    """

    assert set_up['Solution'].longest_consecutive(set_up['long'])