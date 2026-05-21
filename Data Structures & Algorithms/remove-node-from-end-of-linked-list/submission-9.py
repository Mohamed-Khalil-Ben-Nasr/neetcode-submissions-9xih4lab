# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        k = n + 1
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next

        # there needs to be a gap of n + 1 so that we reach the n-1th node to delete the nth node
        slow = ListNode() 
        slow.next = head
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head

