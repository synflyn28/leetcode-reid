"""
This module contains the tests for the subsequence LeetCode
problem.

(c) Justin Reid
"""

import pytest

from scripts.subsequence import Solution

@pytest.fixture(scope='module')
def setup_fixture():
    """
    Set up test fixture
    """

    return {
        'solution': Solution(),
        'is_sub': ['abc', 'ahbgdc'],
        'no_sub': ['axc', 'ahbgdc']
    }


def test_no_sub(setup_fixture):
    """
    Test to see if a subsequence fail case returns False.
    """

    assert setup_fixture['solution'].is_subsequence(*setup_fixture['no_sub']) == False


def test_is_sub(setup_fixture):
    """
    Test to see if a valid subsequence case returns True.
    """

    assert setup_fixture['solution'].is_subsequence(*setup_fixture['is_sub']) == True