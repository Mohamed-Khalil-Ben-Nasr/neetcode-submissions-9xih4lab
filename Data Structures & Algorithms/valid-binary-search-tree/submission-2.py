# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidSubtree(root, minimum, maximum):
            if not root:
                return True

            if not (minimum < root.val < maximum):
                return False
            
            left = isValidSubtree(root.left, minimum, root.val)
            right = isValidSubtree(root.right, root.val, maximum)
            # when we reach this stage, that means this condition is already valid
            # since we checked it earlier:
            # (minimum < root.val < maximum)
            return left and right

        return isValidSubtree(root, float("-inf"), float("inf"))
            