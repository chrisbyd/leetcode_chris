from typing import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(node):
            if not node: return []
            return [node.val] + preorder(node.left) + preorder(node.right)
        
        traversal = preorder(root)
        print(traversal)
        if len(traversal) <= 1:
            return root
        root.val = traversal[0]
        root.left = None
        cur_node = root
        for val in traversal[1:]:
        
            node = TreeNode(val)
            cur_node.right = node
            cur_node = cur_node.right
      

        return root
            
            