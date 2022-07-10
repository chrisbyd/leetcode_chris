# Definition for a binary tree node.
from  typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traverse(curNode):
            if curNode is None:
                return []
            else:
                return traverse(curNode.left) + [ curNode.val] + traverse(curNode.right)
        nums = traverse(root)
        nums.sort() 
        ans = nums[1] - nums[0]
        for i in range(2, len(nums)):
            ans = min(ans, nums[i] - nums[i-1])
        return ans
            
        
                