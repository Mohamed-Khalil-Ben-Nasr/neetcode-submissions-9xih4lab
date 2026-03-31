# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        # split the linked list in 2 using slow and fast pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linked list

        cur = slow.next
        # sever connection between halves
        slow.next = None
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        head2 = prev

        # create the new reordered list
        i = 1
        cur = head
        head = head.next
        # im doing this cuz i didnt cutoff the last node of the first half 
        # from the the first node of the second half        
        while head and head2:
            if i % 2 == 0:
                cur.next = head
                head = head.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
            i += 1
        if head:
            cur.next = head
        else:
            cur.next = head2