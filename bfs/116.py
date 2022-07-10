from typing import Optional

from typing import List, Optional
from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        q = deque([root])
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                node.next = q[0] if i < length - 1 else None
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root