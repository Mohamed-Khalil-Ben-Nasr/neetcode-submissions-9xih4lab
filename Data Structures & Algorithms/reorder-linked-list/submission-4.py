# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now slow will point to the start of the second half of the linked list
        # time to reverse the second half of the LL
        tail = slow.next
        slow.next = None
        cur = tail
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # now prev is the head of the reversed second half of the LL
        h2 = prev
        i = 0
        cur = ListNode()
        while head and prev:
            if i % 2 == 0:
                cur.next = head 
                head = head.next
            else:
                cur.next = h2
                h2 = h2.next
            i += 1
            cur = cur.next
        if head:
            cur.next = head
        elif h2:
            cur.next = h2


    