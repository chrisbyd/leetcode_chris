from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    index = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def construct_node(inorder):
            if len(inorder) != 0 :
                this_value = preorder[self.index]
                self.index = self.index +1
       
                this_node = TreeNode(val=this_value, left= None, right= None)
                if len(inorder) == 0:
                    this_node.left = None
                    this_node.right = None
                else:
        
                    index_inorder = inorder.index(this_value)
                   
                    inorder_left = inorder[:index_inorder]
                    inorder_right = inorder[index_inorder+1:]
                    this_node.left = construct_node( inorder_left)
                    this_node.right = construct_node( inorder_right)
                return this_node
            else:
                return None
        if len(preorder) == 0:
            return None
        root = construct_node(inorder)
        return root

sol = Solution()
pre = [3,9,20,15,7] 
inorder = [9,3,15,20,7]
res = sol.buildTree(pre, inorder)
print(res)









        



        