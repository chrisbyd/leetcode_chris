from typing import List
from typing import Optional

# Definition for a binary tree node.
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def validate(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and node2:
                return validate(node1.right, node2.left) and node1.val == node2.val and validate(node1.left, node2.right)
            else:
                return False
        return validate(root.left, root.right)
        
        
        