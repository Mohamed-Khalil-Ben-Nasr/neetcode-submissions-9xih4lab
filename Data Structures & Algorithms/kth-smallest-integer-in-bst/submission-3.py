# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def inOrderTraversal(root):
            if not root:
                return

            inOrderTraversal(root.left)
            nodes.append(root.val)
            inOrderTraversal(root.right)
            return
        
        inOrderTraversal(root)
        return nodes[k-1]
        