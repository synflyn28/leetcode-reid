"""
This script contains the implementation of the group anagram solution.
"""

class Solution:

    def get_frequency_string(self, alpha_string):
        """
        Get string representing the frequecy of all letter characters inside
        a given string
        """

        freq_list = [0] * 26

        for char in alpha_string:
            freq_list[ord(char) - ord("a")] += 1

        frequency_string = []

        char = 'a'

        for position in freq_list:
            frequency_string.append(char)
            frequency_string.append(str(position))
            char = chr(ord(char) + 1)
        
        return ''.join(frequency_string)



    def group_anagrams(self, strs: list[str]):
        """
        Find the anagram groups.
        """

        if not strs:
            return []
        
        hashmap = {}

        for test_string in sorted(strs):
            frequency_string = self.get_frequency_string(test_string)
            if frequency_string not in hashmap:
                hashmap[frequency_string] = []
            
            hashmap[frequency_string].append(test_string)

        return list(sorted(list(hashmap.values()), key=len))
        
