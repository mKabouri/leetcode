# Link: https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        def is_k_repeating(sequence: str, word: str, k: int) -> bool:
            k_word = word*k
            return k_word in sequence

        k = 0
        while is_k_repeating(sequence, word, k):
            k+=1
        return k-1
