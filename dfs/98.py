# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def maxBst( node):
            if node.right is None:
                return node.val
            else:
                return maxBst(node.right)
            
        def minBst(node):
            if node.left is None:
                return node.val
            else:
                return minBst(node.left)
        
        def dp(node):
            if node.left is None and node.right is None:
                return True
            else:
                if node.left is None and node.right is not None:
                    return dp(node.right) and node.val < minBst(node.right)
                elif node.left is not None and node.right is None:
                    return dp(node.left) and node.val > maxBst(node.left)
                else:
                    return dp(node.left) and dp(node.right) and node.val > maxBst(node.left) and node.val < minBst(node.right)
        return dp(root)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if node is None:
                return True
            else:
                if node.val <= left or node.val >= right:
                    return False
                else:
                    return validate(node.left, left, node.val ) and validate(node.right, node.val, right)
        return validate(root, -float('inf'), float('inf'))
                
        