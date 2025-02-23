# Link: https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        index_dict = {}
        for i in range(n):
            if target - nums[i] in index_dict:
                return [i, index_dict[target - nums[i]]]
            else:
                index_dict[nums[i]] = i


class Solution:
    from collections import defaultdict
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        new_nums = [target-x for x in nums]
        index_dict = defaultdict(list)
        for i in range(n):
            index_dict[nums[i]].append(i)

        for i in range(n):
            indices = index_dict[new_nums[i]]
            for idx in indices:
                if new_nums[i] == nums[idx] and i != idx:
                    return [i, idx]
