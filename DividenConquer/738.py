# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    
        def getmax(node):
            if not node.right:
                return node.val
            else:
                return getmax(node.right)
        
        def getmin(node):
            if not node.left:
                return node.val
            else:
                return getmin(node.left)
        
        def dfs(node):
            if not node.left and not node.right:
                return float('inf')
            else:
                ans = float('inf')
                if node.left:
                    ans = min(ans,  node.val - getmax(node.left))
                    res1 = dfs(node.left)
                    ans = min(ans, res1)
                if node.right: 
                    ans = min(ans, getmin(node.right) - node.val)
                    res2 = dfs(node.right)
                    ans = min(ans, res2)
                return ans
        return dfs(root)
            