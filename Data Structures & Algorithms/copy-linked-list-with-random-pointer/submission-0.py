"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        oldToNew = {}
        cur = head
        while cur:
            new = Node(cur.val)
            oldToNew[cur] = new
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                oldToNew[cur].next = oldToNew[cur.next]
            if cur.random:
                oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next
        return oldToNew[head]