"""
This module contains the implementation for the longest consecutive 
sub array.
"""

class Solution:
    def longest_consecutive(self, nums):
        """
        Find the longest consecutive sub array of a list of numbers.
        """

        longest_length = 0
        hashmap = {}

        for num in nums:
            hashmap[num] = None

        for num in nums:
            current_length = 1

            next_num  = num + 1
            while next_num in hashmap and not hashmap[next_num]:
                current_length += 1
                hashmap[next_num] = True
                next_num += 1

            prev_num = num - 1
            while next_num in hashmap and not hashmap[next_num]:
                current_length += 1
                hashmap[next_num] = True
                prev_num -= 1

            longest_length = max(longest_length, current_length)

        return longest_length