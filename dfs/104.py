from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 1
        def dfs(node):
            if not node: return 0
            return max(dfs(node.left), dfs(node.right)) + 1
        return dfs(root)
            
        