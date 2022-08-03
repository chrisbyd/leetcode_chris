from typing import Optional


# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def search(root, value):
            if not root:
                return False
            elif root.val == value:
                return True
            else:
                if value > root.val:
                    return search(root.right, value)
                else:
                    return search(root.left, value)
        q = deque([root])
        while q:
            node = q.popleft()
            if search(root, k - node.val) and k != 2* node.val:
                return True
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return False
        
###shibushi bieren bufahuo dehua jiu ba bierendangshazi a1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        storage = set()
        def search(root):
            if not root:
                return False
            elif k - root.val in storage:
                return True
            else:
                storage.add(root.val)
                return  search(root.left) or search(root.right)
        return search(root)
   