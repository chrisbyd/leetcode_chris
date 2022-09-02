# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node):
            if (node.val - p.val)* (node.val - q.val) <= 0:
                return node
            elif p.val < node.val:
                return search(node.left)
            else:
                return search(node.right)
        return search(root)
            
            
        