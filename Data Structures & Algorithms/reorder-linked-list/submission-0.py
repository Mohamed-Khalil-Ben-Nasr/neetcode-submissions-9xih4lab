# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        # find middle node
        # if len(list) % 2 == 1 => f will reach null 
        # if len(list) % 2 == 0 => f will stop at the last node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHead = slow.next
        # the first half needs to end with Null
        slow.next = None

        # reverse the second half of the linked list
        prev = None
        while secondHead:
            tmp = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = tmp
        
        # merge
        # we know from slow/fast that the secondHead list is shorter
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1
        





