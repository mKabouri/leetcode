# Link: https://leetcode.com/problems/pascals-triangle-ii/description/

from math import comb

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, k) for k in range(rowIndex+1)]
