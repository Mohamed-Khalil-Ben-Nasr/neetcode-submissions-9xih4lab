# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        if length == 1:
            return head
        kGroupsCount = length // k
        cur = head
        lastNodeOfPreviousGroup = ListNode()
        newHead = lastNodeOfPreviousGroup
        for i in range(kGroupsCount):
            # we entered a new valid group that has enough nodes to be reversed
            # so i shouldnt worry about empty nodes
            firstNodeInTheGroupBeforeReverse = cur
            prev = cur
            cur = cur.next
            l = 0
            # reverse current group
            while l < k-1:
                tmp = cur.next
                cur.next = prev
                prev = cur 
                cur = tmp
                l += 1
            # now prev points to the last reversed node in the current group
            # which is the start of the current group after it was reversed
            # and cur points to the start of the next group that needs to be reversed
            firstNodeInTheGroupBeforeReverse.next = cur
            lastNodeOfPreviousGroup.next = prev
            # set up pointers to move to the next iteration
            lastNodeOfPreviousGroup = firstNodeInTheGroupBeforeReverse
        
        return newHead.next
            




