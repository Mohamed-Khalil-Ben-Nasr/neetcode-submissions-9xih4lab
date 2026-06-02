# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        # build the string via bfs
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur == None:
                res.append("N")
                continue
            res.append(str(cur.val))
            # append both children even if they are None
            q.append(cur.left)
            q.append(cur.right)

        # node values can be multiple digits so im gonna use a delimiter
        return "#".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = data.split("#")
        root = TreeNode(val = lst[0]) if lst[0] != "N" else None
        q = deque([root])
        j = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == None:
                    continue
                cur.left  = TreeNode(val = lst[j]) if j < len(lst) and lst[j] != "N" else None
                if cur.left:
                    q.append(cur.left)
                cur.right = TreeNode(val = lst[j+1]) if j+1 < len(lst) and lst[j+1] != "N" else None
                if cur.right:
                    q.append(cur.right)
                j += 2
        return root



            

    
        
