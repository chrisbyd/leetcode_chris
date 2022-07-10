from typing import Optional


# Definition for a binary tree node.
from collections import defaultdict
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        ans = []
        direction = 0
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if direction == 1:
                ans.append(level[::-1])
            else:
                ans.append(level)
            direction = 1 - direction
        return ans
                
            
            
            