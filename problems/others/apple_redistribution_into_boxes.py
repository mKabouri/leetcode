# Link: https://leetcode.com/problems/apple-redistribution-into-boxes/description/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple_sum = sum(apple)
        capacity.sort(reverse=True)
        nb_boxes = 0
        counter = 0
        while counter < apple_sum:
            counter += capacity[nb_boxes]
            nb_boxes += 1
        return nb_boxes
