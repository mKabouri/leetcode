# Link: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        j = 0
        for i in range(k):
            nums[j] = -nums[j]
            if j + 1 < n:
                if nums[j+1] < nums[j]:
                    j += 1
        return sum(nums)
