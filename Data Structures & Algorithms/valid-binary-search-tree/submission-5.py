# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self, root, curMin, curMax):
        if not root:
            return True
        
        if root.val <= curMin or root.val >= curMax:
            return False
        
        return self.isValid(root.left, curMin, root.val) and self.isValid(root.right, root.val, curMax)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float("-inf"), float("inf"))