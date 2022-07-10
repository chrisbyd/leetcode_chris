# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, cur_path):
            if not node:
                return
            elif not node.left and not node.right:
                cur_path.append(node.val)
                if sum(cur_path) == targetSum:
                    res.append(cur_path)
            else:
                dfs(node.left, cur_path + [node.val])
                dfs(node.right, cur_path + [node.val])
        dfs(root, [])
        return res
                
        