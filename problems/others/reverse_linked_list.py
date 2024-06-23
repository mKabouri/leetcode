# Link: https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        store_values = []
        store_values.append(head.val)

        iterator = head
        while iterator.next != None:
            iterator = iterator.next
            store_values.append(iterator.val)
        
        res = ListNode(val=store_values[-1])
        iterator = res
        for i in range(len(store_values) - 2, -1, -1):
            iterator.next = ListNode(val=store_values[i])
            iterator = iterator.next
        
        return res
