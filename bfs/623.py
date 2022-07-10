from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val = val)
            new_root.left = root
            return new_root
        else:
            q = deque([])
            q.append(root)
            cur_depth = 1
            while q:
                length = len(q)
                for _ in range(length):
                    cur_node = q.popleft()
                    print(cur_node)
                    if cur_depth == depth - 1:
                        new_node_left = TreeNode(val = val)
                        new_node_right = TreeNode(val = val)
                        new_node_left.left = cur_node.left
                        new_node_right.right = cur_node.right
                        cur_node.left = new_node_left
                        cur_node.right = new_node_right
                    else:
                        if  cur_node.left: q.append(cur_node.left)
                        if  cur_node.right: q.append(cur_node.right)

                cur_depth += 1

            return root