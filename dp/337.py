from functools import cache
from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(cur_root):
            if not cur_root:
                return 0
            elif cur_root.left is None and cur_root.right is None:
                return cur_root.val
            elif cur_root.left and not cur_root.right:
                return max(cur_root.val+ dp(cur_root.left.left) + dp(cur_root.left.right),
                            dp(cur_root.left) + dp(cur_root.right))
            elif not cur_root.left and cur_root.right:
                return max(cur_root.val+ dp(cur_root.right.left) + dp(cur_root.right.right),
                            dp(cur_root.left) + dp(cur_root.right))
            else:
                return max(cur_root.val+ dp(cur_root.left.left) + dp(cur_root.left.right)+ dp(cur_root.right.left) + dp(cur_root.right.right),
                            dp(cur_root.left) + dp(cur_root.right))
                
        return dp(root)


# top down with memorization by directly hashing the node class

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(cur_root):
            if cur_root not in memo:
                if not cur_root:
                    res = 0
                elif cur_root.left is None and cur_root.right is None:
                    res = cur_root.val
                elif cur_root.left and not cur_root.right:
                    res =  max(cur_root.val+ dp(cur_root.left.left) + dp(cur_root.left.right),
                                dp(cur_root.left) + dp(cur_root.right))
                elif not cur_root.left and cur_root.right:
                    res= max(cur_root.val+ dp(cur_root.right.left) + dp(cur_root.right.right),
                                dp(cur_root.left) + dp(cur_root.right))
                else:
                    res= max(cur_root.val+ dp(cur_root.left.left) + dp(cur_root.left.right)+ dp(cur_root.right.left) + dp(cur_root.right.right),
                                dp(cur_root.left) + dp(cur_root.right))
                memo[cur_root] = res
                return res
            else:
                return memo[cur_root]
        return dp(root)

# my solution is complicated 
#try with another more concise solution
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node, canRob):
            if not node:
                return 0
            res = dp(node.left, True) + dp(node.right, True)
            if canRob:
                res = max(res, node.val + dp(node.left, False) + dp(node.right, False))
            return res
        return dp(root, True)



