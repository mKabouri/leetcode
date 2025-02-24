# Link: https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(array: List[int], target: int):
            start, end = 0, len(array)-1
            best_res = None
            while start <= end:
                mid = (start+end)//2
                if array[mid] == target:
                    return array[mid]
                elif array[mid] < target:
                    best_res = array[mid]
                    start = mid + 1
                else:
                    end = mid - 1
            return best_res 

        m = len(queries)
        answer = [0]*m
        nums.sort()

        prefix_sum_dict = dict()
        counter = 0
        for i in range(len(nums)):
            counter += nums[i]
            prefix_sum_dict[counter] = i+1
        prefix_sums = list(prefix_sum_dict.keys())

        for i in range(m):
            if queries[i] < prefix_sums[0]:
                answer[i] = 0
            else:
                answer[i] = prefix_sum_dict[binary_search(prefix_sums, queries[i])]
        return answer
