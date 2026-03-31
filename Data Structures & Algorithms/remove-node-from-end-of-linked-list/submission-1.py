# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        slow = head
        fast = head
        i = 0
        while i < n:
            i += 1
            fast = fast.next
        
        # with this intialization
        # fast - slow = n
        # and slow - prev = 1
        # fast will mark the null node / final node of the linked list
        # slow will be the node that needs to be deleted
        # prev is the node thats right in front of slow and will be used to delete slow

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        # delete node that slow points to
        if prev:
            prev.next = slow.next
        else:
        # this is thanks to this hint:
        #I n Example 3 (head = [1, 2], n = 2), the node to remove is 1. 
        # After your first while loop, fast becomes None immediately. 
        # Since the second while loop never runs, prev remains None. 
        # What should you return in this scenario?
            return slow.next

        return head if head else None
