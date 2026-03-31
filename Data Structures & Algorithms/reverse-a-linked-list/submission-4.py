# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        cur = head
        if cur.next:
            newHead = self.reverseList(cur.next)
            cur.next.next = cur
        cur.next = None
        return newHead
