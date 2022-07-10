from typing import List
from typing import Optional
# Definition for a binary tree node.

##### this code will not pass since it is consumes too much time
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    ans = 0
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dp(cnode, direction):
            if direction == 0 and cnode.left is None:
                return 0
            elif direction == 1 and cnode.right is None:
                return 0
            else:
                return 1 + dp(cnode.right, 1- direction) if direction else 1 + dp(cnode.left, 1 - direction)
        
       
        def traversal(cnode):
            if cnode.left == None and cnode.right == None:
                return
            else:
                self.ans = max(self.ans, dp(cnode, 0), dp(cnode, 1)) 
                if cnode.left is not None:
                    traversal(cnode.left)
                if cnode.right is not None:
                    traversal(cnode.right)
        traversal(root)
        return self.ans


# Definition for a binary tree node.
# correct
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    ans = 0
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dp(cnode, direction):
            if cnode.left is not None and cnode.right is not None:
                left = 1 + dp(cnode.left, 1)
                right = 1 + dp(cnode.right, 0)
                self.ans = max(max(left, right), self.ans)
                return left if direction == 0 else right
            elif cnode.left is not None:
                res = 1 + dp(cnode.left, 1)
                self.ans = max(self.ans, res)
                if direction == 0:
                    return res
                else:
                    return 0
            elif cnode.right is not None:
                res = 1 + dp(cnode.right, 0)
                self.ans = max(self.ans, res)
                if direction == 1:
                    return res
                else:
                    return 0
            else:
                return 0
        dp(root, 0)
        return self.ans
                