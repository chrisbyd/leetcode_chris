# Definition for a binary tree node.
from copy import copy
from typing import List
from typing import Optional


# wrong anser
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
#         ans = []

#         def copyTree(tocopy, copy):
#             copy.val = tocopy.val
#             if tocopy.left:
#                 copy.left = TreeNode()
#                 copyTree(tocopy.left, copy.left)
#             elif tocopy.right:
#                 copy.right = TreeNode()
#                 copyTree(tocopy.right, copy.right)
        
#         def addNode(curNode, value):
#             if curNode.val < value and not curNode.right:
#                 curNode.right = TreeNode(val= value)
#             elif curNode.val > value and not curNode.left:
#                 curNode.left = TreeNode(val= value)
#             elif curNode.val < value:
#                 addNode(curNode.right, value)
#             else:
#                 addNode(curNode.left, value)

#         def rmleafNode(curNode, value):
#             if value > curNode.val and curNode.right.val == value:
#                 curNode.right = None
#             elif value > curNode.val:
#                 rmleafNode(curNode.right, value)
#             elif value < curNode.val and curNode.left.val == value:
#                 curNode.left = None
#             else: rmleafNode(curNode.left, value)


#         def dfs(num_list, root):
#             if len(num_list) == 0:
#                 newRoot = TreeNode()
#                 copyTree(root, newRoot)
#                 ans.append(newRoot)
#             else:
#                 for idx, value in enumerate(num_list):
#                     addNode(root, value)
#                     n_list = num_list[:idx] + num_list[idx+1:]
#                     dfs(n_list, root)
#                     rmleafNode(root,value)
#         n_list = [i for i in range(1, n+1)]
#         for idx, root_value in enumerate(n_list):
#             root = TreeNode(root_value)
#             num_list = n_list[:idx] + n_list[idx+1:]
#             dfs(num_list, root)
#         return len(ans)

sol = Solution()
n = 3
res = sol.generateTrees(n)
print(res)
                    




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def copy(cur_node):
            if cur_node is None:
                return None
            newNode = TreeNode(cur_node.val)
            newNode.left = copy(cur_node.left)
            newNode.right = copy(cur_node.right)
            return newNode
        
        ans = []
        ans.append(TreeNode(1))
        for i in range(2, n+1): 
            tem = []
            for j in range(len(ans)):
                #if the i th value is set to be the root
                newRoot = TreeNode(i)
                newRoot.left = copy(ans[j])
                tem.append(newRoot)

                # else the ith node is set 
                cur = ans[j]
                old_root = cur
                while cur:
                    newNode = TreeNode(i)
                    originalRight = cur.right
                    cur.right = newNode
                    newNode.left = originalRight
                    tem.append(copy(old_root))
                    cur.right = originalRight
                    cur = cur.right
            ans = tem
        return ans

            




# with top-down dynamic programming


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def clone(curNode):
            if not curNode:
                return None
            newNode = TreeNode(curNode.val)
            newNode.left = clone(curNode.left)
            newNode.right = clone(curNode.right)
            return newNode

        def dp(n):
            if n == 1:
                return [TreeNode(1)]
            else:
                tem = []
                newNode = TreeNode(n)
                subNodeList = dp(n-1)
                for rNode in subNodeList:
                    newNode.left = rNode
                    tem.append(clone(newNode))
                    newNode.left = None
                    thisRoot = rNode
                    while rNode:
                        oriRight = rNode.right
                        rNode.right = newNode
                        newNode.left = oriRight
                        tem.append(clone(thisRoot))
                        rNode.right = oriRight
                        rNode = rNode.right
                return tem
        return dp(n)

                
                


        