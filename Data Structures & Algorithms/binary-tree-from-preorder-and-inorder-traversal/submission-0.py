# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case for null nodes
        if not preorder or not inorder:
            return None
        
        root = TreeNode(val = preorder[0])
        root_index = inorder.index(root.val)
        # in inorder array, everything to left of root belongs to left subtree
        # and to the right belongs to right subtree
        # length of the left subtree = root_index
        root.left =  self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root