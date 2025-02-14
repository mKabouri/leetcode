# Link: https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        search_index = 0
        for el_s in s:
            if not el_s in t[search_index:]:
                return False
            search_index += t[search_index:].find(el_s) + 1
        return True
