"""
Problem: 0347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Pattern: Arrays & Hashing / Sorting (Frequency Map + Custom Sort Key)

Approach:
- Build a frequency dictionary `dic` mapping each number in `nums` to its occurrence count.
- Sort `dic.keys()` using `key=lambda x: dic[x]` so elements are ordered by their frequency rather than their raw value.
- Set `reverse=True` to order from highest frequency to lowest, then slice `[:k]` to return the top `k` elements.

Complexity:
- Time: O(n log n) — Counting frequencies takes O(n), and sorting up to n unique keys takes O(n log n) in the worst case.
- Space: O(n) — The hash map and sorted key list each store up to n elements in the worst case.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        return sorted(dic.keys(),key = lambda x:dic[x],reverse =True)[:k]