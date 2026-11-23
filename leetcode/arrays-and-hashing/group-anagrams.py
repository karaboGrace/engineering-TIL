"""
Problem: 0049. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Pattern: Arrays & Hashing (Canonical Key / Grouping Hash Map)

Approach:
- Use a hash map (`anagrams`) to group strings that share the same anagram signature.
- For each string `s` in `strs`, sort its characters and join them into a string (`sorted_word`) to serve as a canonical key.
- If `sorted_word` is not yet in `anagrams`, initialize an empty list `[]` for that key.
- Append the original string `s` (not `sorted_word`) to `anagrams[sorted_word]`.
- Return `list(anagrams.values())` containing all grouped anagram lists.

Complexity:
- Time: O(n * k log k) — Where n is the number of strings in `strs` and k is the maximum string length; sorting each string takes O(k log k) across n strings.
- Space: O(n * k) — Storing all keys and grouped strings across the hash map and output list.
"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_word = "".join(sorted(s))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(s)
        return list(anagrams.values())