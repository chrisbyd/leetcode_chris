from typing import List
from typing import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    res = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
      #  res = 0
        
        def dfs(node, cur_path):
            if not node: return 
            else:
                c_sum = node.val
                if c_sum == targetSum:
                    self.res += 1
                for num in cur_path[::-1]:
                    c_sum += num
                    if c_sum == targetSum:
                        self.res += 1
                dfs(node.left, cur_path + [node.val])
                dfs(node.right, cur_path + [node.val])
        dfs(root, [])
        ans = self.res
        self.res = 0
        return ans

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    res = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def find(node, csum):
            if not node: return
            csum -= node.val
            if csum == 0:
                self.res += 1
            find(node.left, csum)
            find(node.right, csum)
                
        def dfs(node):
            if not node: return 
            else:
                find(node, targetSum)
                dfs(node.left)
                dfs(node.right)
                 
        dfs(root)
        ans = self.res
        self.res = 0
        return ans
                        
                        