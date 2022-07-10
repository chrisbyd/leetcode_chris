from typing import Optional
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(level)
        return ans[::-1]
    