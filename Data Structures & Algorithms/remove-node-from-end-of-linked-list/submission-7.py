# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n)

        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next

        target = l - n - 1
        i = -1
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur:
            if i == target:
                tmp = cur.next
                cur.next = cur.next.next
                tmp.next = None
                break

            i += 1
            cur = cur.next

        return dummy.next
