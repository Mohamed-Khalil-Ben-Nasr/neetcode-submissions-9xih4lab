# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and (not list2):
            return list1
        
        if list2 and (not list1):
            return list2
        
        if (not list1) and (not list2):
            return list1 
        
        newH = None
        if list1.val <= list2.val:
            newH = list1
            list1 = list1.next
        else:
            newH = list2
            list2 = list2.next

        cur = newH
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1 and (not list2):
            cur.next = list1
        
        if list2 and (not list1):
            cur.next = list2
        
        return newH
        