# Definition for a binary tree node.
# Definition for a binary tree node.

            

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node, cur, res):
            if not node:
                return
            if not node.left and not node.right:
                res.append(cur * 10 + node.val)
                return 
            dfs(node.left, cur* 10 + node.val, res)
            dfs(node.right, cur*10 + node.val, res)
        dfs(root, 0, res)
        return sum(res)
        