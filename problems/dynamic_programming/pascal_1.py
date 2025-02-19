# Link: https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for i in range(1, numRows):
            L = [1]
            for j in range(i-1):
                L.append(res[i-1][j]+res[i-1][j+1])
            L.append(1)
            res.append(L)
        return res

