from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.index = len(postorder) - 1
        def constructNode(inorder):
            if len(inorder) == 0:
                return None
            else:
                this_value = postorder[self.index]
                self.index -= 1
                this_node = TreeNode(val=this_value, left= None, right= None)
                this_index = inorder.index(this_value)
                inorder_left = inorder[: this_index]
                inorder_right = inorder[this_index+1 :]
                this_node.right = constructNode(inorder_right)
                this_node.left = constructNode(inorder_left)
                return this_node
        if len(postorder) ==  0:
            return None
        return constructNode(inorder) 
        

inorder = [9,3,15,20,7] 
postorder = [9,15,7,20,3]
sol = Solution()
res = sol.buildTree(inorder, postorder)