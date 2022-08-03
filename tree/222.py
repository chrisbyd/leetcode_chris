# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfs(node):
            if not node: return 0
            return 1 + dfs(node.left) + dfs(node.right)
        return dfs(root)
            

        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def isComplete(root):
            cur = root
            left_depth, right_depth = 0, 0
            while cur:
                cur = cur.left
                left_depth += 1
            cur = root
            while cur:
                cur = cur.right
                right_depth += 1
            if left_depth == right_depth:
                return left_depth
            else:
                return 0
        def dfs(node):
            if not node: return 0
            if isComplete(node):
                return 2 ** isComplete(node) - 1
            else:
                return dfs(node.left) + 1 + dfs(node.right)
        return dfs(root)
            
                
            