"""
This module contains the solution for find the top k frequent
characters.

(c) Justin Lynn Reid
"""

class Solution:
    """
    Class that contains the solution for finding the top K elements
    """

    def top_k_frequent(self, nums, K):
        """
        Find top K frequent elements.
        """

        bucket = [[] for _ in range(len(nums) + 1)]
        result = []
        frequency_map = {}

        for n in nums:
            if n not in frequency_map:
                frequency_map[n] = 1
            else:
                frequency_map[n] += 1

        for key, frequency in frequency_map.items():
            bucket[frequency].append(key)

        
        for i in reversed(range(len(bucket))):
            if bucket[i]:
                for value in bucket[i]:
                    if len(result) < K:
                        result.append(value)
                    else:
                        return result

        return result