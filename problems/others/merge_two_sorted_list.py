# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        res = ListNode()
        iterator = res
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                iterator.val = list1.val
                list1 = list1.next
                if list1:
                    iterator.next = ListNode()
                    iterator = iterator.next
            else:
                iterator.val = list2.val
                list2 = list2.next
                if list2:
                    iterator.next = ListNode()
                    iterator = iterator.next


        if list1 == None:
            iterator.next = list2
        if list2 == None:
            iterator.next = list1
        return res


        # def mergeTwoListsFunc(list1, list2, res):
        #     if list1 == None and list2 == None:
        #         return res
        #     if list1 and list2:
        #         if list1.val <= list2.val:
        #             res.val = list1.val
        #             res.next = ListNode()
        #             res = res.next
        #             return mergeTwoListsFunc(list1.next, list2, res)
        #         if list1.val >= list2.val:
        #             res.val = list2.val
        #             res.next = ListNode()
        #             res = res.next
        #             return mergeTwoListsFunc(list1, list2.next, res)
        #     if list1 == None and list2:
        #         res.val = list2.val
        #         res.next = ListNode()
        #         res = res.next
        #         return mergeTwoListsFunc(list1, list2.next, res)
        #     elif list1 and list2 == None:
        #         res.val = list1.val
        #         res.next = ListNode()
        #         res = res.next
        #         return mergeTwoListsFunc(list1.next, list2, res)
        # return mergeTwoListsFunc(list1, list2, ListNode())
