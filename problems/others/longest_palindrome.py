# Link: https://leetcode.com/problems/longest-palindrome/description/

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        longest_pal = 0
        max_odd = 0
        for v in count.values():
            longest_pal += (v//2)*2
            if v%2 == 1:
                max_odd = 1
        return longest_pal + max_odd
