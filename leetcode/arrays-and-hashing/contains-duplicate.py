"""
Problem: 0217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Pattern: Arrays & Hashing (Hash Set)

Approach:
- Initialize an empty set `seen` to track elements encountered so far.
- Iterate through each number in `nums`:
  - If the number is already in `seen`, return `True` immediately.
  - Otherwise, add it to `seen` and keep scanning.
- If the loop finishes without finding a duplicate, return `False`.

Complexity:
- Time: O(n) — We iterate through the list once, and each set lookup/insertion takes O(1) average time.
- Space: O(n) — In the worst case (all elements unique), `seen` stores up to n elements.
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1, 2, 3, 4, 4]))  # True
    print(sol.hasDuplicate([1, 2, 3, 4]))     # False