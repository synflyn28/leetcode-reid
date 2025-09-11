"""
This code contains the tests for the test k freq implementation.
"""

import pytest

from scripts.k_freq import Solution

@pytest.fixture(scope='module')
def setup_data():
    """
    Set up fixture data for tests.
    """

    return {
        'short_list': [1,1,1,2,2,3],
        'full_list': [1,2,1,2,1,2,3,1,3,2],
        'single_list': [1],
        'solution': Solution()
    }



def test_single_list(setup_data):
    """
    Test single list case.
    """

    assert setup_data['solution'].top_k_frequent(setup_data['single_list'], 1) == [1]


def test_short_list(setup_data):
    """
    Test short list case.
    """

    assert setup_data['solution'].top_k_frequent(setup_data['short_list'], 2) == [1, 2]


def test_full_list(setup_data):
    """
    Test short list case.
    """

    assert setup_data['solution'].top_k_frequent(setup_data['full_list'], 2) == [1, 2]

