# Link:


# Solution 1: Observe a pattern
from math import log2

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        save = [1, 2]
        res = [1, 2]
        for i in range(int(log2(n))):
            save += [x+1 for x in save]
            res += save
            if len(res) > n-2:
                break
        res = [0, 1] + res
        return res[:n+1]

# Solution 2: Naive
class Solution:
    def countBits(self, n: int) -> List[int]:
        def num_ones(n: int):
            counter = 0
            while n != 0:
                counter += n%2
                n = n//2
            return counter

        def num_ones_rec(n: int, counter: int=0):
            if n == 0:
                return counter
            else:
                return num_ones_rec(n//2, counter+n%2)


        res = []
        for i in range(n+1):
            res.append(num_ones_rec(i))            
        return res
