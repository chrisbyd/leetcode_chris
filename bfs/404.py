from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    res = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def isLeaf(node):
            if node and not node.left and not node.right:
                return True
            return False
        
        def dfs(node):
            if isLeaf(node):
                return
            else:
                if isLeaf(node.left):
                    self.res += node.left.val
               
                if node.left: dfs(node.left)
                if node.right: dfs(node.right)
        dfs(root)
        return self.res