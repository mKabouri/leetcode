# Link: https://leetcode.com/problems/unique-binary-search-trees/description/

class Solution:
    def numTrees(self, n: int) -> int:
        def numSubTrees(ng: int, nd: int) -> int:
            return ng*nd
        if n < 2:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5 
        else:
            sum = 0
            if n%2 == 0:
                for i in range(n//2):
                    sum += 2*numSubTrees(self.numTrees(n-i-1), self.numTrees(i))
            else:
                for i in range(n//2):
                    sum += 2*numSubTrees(self.numTrees(n-i-1), self.numTrees(i))
                sum += numSubTrees(self.numTrees(n-(n//2)-1), self.numTrees((n//2)))
            return sum
