# Definition for a binary tree node.
from typing import List
###my solution is way too complicated
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dp(preorder, postorder ):
            if not preorder and not postorder:
                return None
            elif len(preorder) == 1:
                return TreeNode(val = preorder[0])
            else:
                root = TreeNode(val = preorder[0])
                leftroot = preorder[1]
                rightroot = postorder[-2]
                if rightroot == leftroot:
                    root.left = dp(preorder[1:] , postorder[:-1])
                    return root
                else:
                    print(leftroot, rightroot)
                    leftpreorder = preorder[1:  preorder.index(rightroot)]
                    leftpostorder = postorder[: postorder.index(leftroot) + 1 ]
                    rightpreorder = preorder[preorder.index(rightroot) :]
                    rightpostorder = postorder[postorder.index(leftroot) +1 : -1]
                    print(leftpreorder, leftpostorder, rightpreorder, rightpostorder)
                    root.left = dp(leftpreorder, leftpostorder)
                    root.right = dp(rightpreorder, rightpostorder)
                    return root
        return dp(preorder, postorder)

####more consie way
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dp(pre, post):
            if not pre:
                return None
            if len(pre) == 1:
                return TreeNode(val = post.pop())
            root = TreeNode(val = post.pop())
            print(pre, post)
            index = pre.index(post[-1])
            root.right = dp( pre[index:] , post)
            root.left = dp(pre[1:index ], post)
            return root
        return dp(preorder, postorder)
            
        