
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return root
        q = deque([root])
        ans = []
        while q:
            length = len(q)
            c_sum = 0
            for i in range(length):
                node = q.popleft()
                c_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(c_sum / length)
        return ans
        
from collections import defaultdict, deque
