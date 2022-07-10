from typing import Optional,List


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root
        q = deque([root])
        ans = []
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i == length - 1:
                    ans.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
        return ans
                
    