# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorderTraversal(node):
            if not node: return []
            else:
                return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
        l1 = inorderTraversal(root1)
        l2 = inorderTraversal(root2)
        res = sorted(l1 + l2)
        return res