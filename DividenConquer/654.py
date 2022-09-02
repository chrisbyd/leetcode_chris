# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dp(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(val = nums[0])
            maxnum = max(nums)
            index = nums.index(maxnum)
            leftnums = nums[:index]
            rightnums = nums[index+1:]
            root = TreeNode(val = maxnum)
            root.left = dp(leftnums)
            root.right = dp(rightnums)
            return root
        return dp(nums)
        