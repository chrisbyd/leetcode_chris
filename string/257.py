from typing import List
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(this_node, cur_path):
            if this_node.left == None and this_node.right == None:
                cur_path += '->' + str(this_node.val)
                ans.append(cur_path)
            else:
                cur_path += '->' +str(this_node.val)
                if this_node.left:
                    dfs(this_node.left, cur_path)
                if this_node.right:
                    dfs(this_node.right, cur_path )
        if root.left:
            dfs(root.left, str(root.val))
        if root.right:
            dfs(root.right, str(root.val))
        if not root.left and not root.right:
            ans = [str(root.val)]
        return ans

a = TreeNode(1)
# a.left = TreeNode(2)
# a.left.right = TreeNode(5)
# a.right = TreeNode(3)
sol = Solution()
res = sol.binaryTreePaths(a)
print(res)