# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:    
    def mergeTwo(self, l1, l2):
        # in case odd num of lists
        if not l2:
            return l1

        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        
        return dummy.next


    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        lists = deque(lists)

        while len(lists) > 1:
            l1 = lists.popleft()
            l2 = lists.popleft()
            new = self.mergeTwo(l1, l2)
            lists.append(new)

        return lists[0]    




        