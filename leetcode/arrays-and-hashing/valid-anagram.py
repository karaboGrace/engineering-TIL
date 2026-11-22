"""
Problem: 0242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Pattern: Arrays & Hashing (Frequency Hash Map)

Approach:
- If `s` and `t` have different lengths, they cannot be anagrams, so return `False` immediately.
- Use two hash maps (`words` and `wordt`) to count the frequency of each character in `s` and `t`.
- Compare both frequency dictionaries at the end; they are equal if and only if both strings contain the exact same characters with identical counts.

Complexity:
- Time: O(n) — Where n is the length of the strings (equal after the length check). Building each frequency map takes O(n), and comparing the dictionaries takes at most O(n) unique keys.
- Space: O(n) — Two hash maps store character counts, each holding at most n distinct characters (or O(1) if bounded by a fixed alphabet size).
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        wordt = {}
        words = {}
        for char in t:
            wordt[char] = wordt.get(char,0)+1
        for chars in s:
            words[chars] = words.get(chars,0)+1
        return wordt == words
t = "car"
s = "rac"
sol = Solution()
print(sol.isAnagram(s,t))