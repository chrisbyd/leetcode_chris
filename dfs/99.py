# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tmp = []
        def dfs(node):
            if not node: return 
            dfs(node.left)
            tmp.append(node)
            dfs(node.right)
        dfs(root)
        nums = sorted([tmp[i].val for i in range(len(tmp))])
        for i in range(len(tmp)):
            if nums[i] != tmp[i].val:
                tmp[i].val = nums[i]
        return root
        