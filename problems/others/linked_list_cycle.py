# Link: https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        elements = set()
        while head != None:
            if head in elements:
                return True
            elements.add(head)
            head = head.next
        return False
