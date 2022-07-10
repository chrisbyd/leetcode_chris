from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    isBalanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(node):
            if not node: return 0
            else:
                lh = dfs(node.left)
                lr = dfs(node.right)
                difference = abs(lh - lr)
                print('Node is ', node.val, 'difference is', difference)
                if difference > 1:
                    self.isBalanced = False
                return max(lh, lr) + 1
        
        dfs(root)
        return self.isBalanced