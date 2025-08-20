"""
Test to see if the anagram algorithm works properly.
"""

import pytest

from scripts.group_anagram import Solution


@pytest.fixture(scope='module')
def setup_fixture_data():
    """
    Set up fixtures used for the tests.
    """

    return {
        "full_list": ["eat","tea","tan","ate","nat","bat"],
        "empty_list": [""],
        "single_element_list": ["a"]
    }


def test_anagram(setup_fixture_data):
    """
    Test to see if anagram algorithm works correctly
    """

    solution_inst = Solution()

    assert solution_inst.group_anagrams(setup_fixture_data["empty_list"]) == [[""]]
    assert solution_inst.group_anagrams(setup_fixture_data["single_element_list"]) == [["a"]]
    assert solution_inst.group_anagrams(setup_fixture_data["full_list"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]

