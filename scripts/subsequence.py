"""
This module contains the solution for the subsequence LeetCode
problem.
"""

class Solution:
    def is_subsequence(self, str1, str2):
        """
        Return true if the string s is a subsequence of string t.
        """

        itr1, itr2 = 0, 0

        while itr1 < len(str1) and itr2 < len(str2):
            if str1[itr1] == str2[itr2]: 
                itr1 += 1
                itr2 += 1
            else:
                itr2 += 1

        return itr1 == len(str1)

