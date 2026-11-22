"""
Problem: 0001. Two Sum
Link: https://leetcode.com/problems/two-sum/
Pattern: Arrays & Hashing (Hash Map Lookup)
Difficulty: Easy

Approach:
- Iterate through the array while tracking seen numbers and their indices in a dictionary.
- For each element `num`, compute `complement = target - num`.
- If `complement` exists in the hash map, return `[seen[complement], i]`.
- Otherwise, store `seen[num] = i` and continue.

Complexity:
- Time: O(n) — Single pass through the list with O(1) average hash map lookups.
- Space: O(n) — Worst-case storage of n - 1 elements in the hash map.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []