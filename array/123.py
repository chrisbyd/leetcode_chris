from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BST(nums):
            if len(nums) == 0:
                return None
            m_index = len(nums)//2
            thisNode = TreeNode(val= nums[m_index])
            nums_l = nums[: m_index]
            nums_r = nums[m_index+1: ]
            thisNode.left = BST(nums_l)
            thisNode.right = BST(nums_r)
            return thisNode
        return BST(nums)


        