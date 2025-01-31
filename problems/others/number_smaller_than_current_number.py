# Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

# Solution 1:
from collections import defaultdict

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        nums_table = defaultdict(int)
        nums_table[sorted_nums[0]] = 0
        cumul = 0
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i-1] < sorted_nums[i]:
                nums_table[sorted_nums[i]] = nums_table[sorted_nums[i-1]] + 1 + cumul
                if cumul != 0:
                    cumul = 0
            elif sorted_nums[i-1] == sorted_nums[i]:
                cumul += 1
                nums_table[sorted_nums[i]] = nums_table[sorted_nums[i-1]]

        return [nums_table[x] for x in nums]

# Solution 2:
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        nums_table = dict()
        count = 0
        for i, num in enumerate(sorted_nums):
            if num not in nums_table:
                nums_table[num] = count
            count += 1
        return [nums_table[num] for num in nums]
