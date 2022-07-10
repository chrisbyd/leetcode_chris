from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#### this solution is not correct since the inorder traversal doesnot mean they are correct
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return []
            else:
                return dfs(node.left) + [node.val] + dfs(node.right)
        return dfs(p) == dfs(q)
        

# Definition for a binary tree node.
### this is correct
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkSame(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is not None and node2 is not None:
                return checkSame(node1.left, node2.left) and node1.val == node2.val and checkSame(node1.right, node2.right)
            else:
                return False
        return checkSame(p, q)