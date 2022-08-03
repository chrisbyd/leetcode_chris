from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node: return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            depth = max(right_depth, left_depth) + 1
            if abs(right_depth - left_depth) > 1:
                self.balanced = False
            return depth
        dfs(root)
        return self.balanced