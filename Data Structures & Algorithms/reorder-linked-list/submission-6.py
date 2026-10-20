# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        cur = slow.next
        prev = None
        slow.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        head2 = prev
        dummy = ListNode()
        cur = dummy
        while head and head2:
            cur.next = head
            head = head.next
            cur.next.next = head2
            head2 = head2.next
            cur = cur.next.next
        if (head):
            cur.next = head
        elif head2 :
            cur.next = head2
        