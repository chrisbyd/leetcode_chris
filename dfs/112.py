from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur_sum):
            if not node.left and not node.right:
                if cur_sum + node.val == targetSum:
                    return True
                return False
            elif node.left and not node.right:
                return dfs(node.left, cur_sum + node.val)
            elif not node.left and node.right:
                return dfs(node.right, cur_sum + node.val)
            else:
                return dfs(node.left, cur_sum + node.val) or dfs(node.right, cur_sum + node.val)
        
        return dfs(root, 0) if root else False
            