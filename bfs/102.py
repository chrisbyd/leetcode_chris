from typing import Optional
from typing import List


from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        ans = defaultdict(list)
        
        def preorder(node, depth):
            if not node: return
            ans[depth].append(node.val)
            preorder(node.left, depth + 1)
            preorder(node.right, depth + 1)
        preorder(root, 0)
        res = []
        for key in ans.keys():
            res.append(ans[key])
        return res