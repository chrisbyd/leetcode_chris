from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        def dfs(n):
            if n == 1:
                return [TreeNode()]
            else:
                ans = []
                for i in range(1, n-1):
                    root = TreeNode()
                    if i % 2 == 0:
                        continue
                    else:
                        for left in dfs(i):
                            for right in dfs(n-1-i):
                                root = TreeNode()
                                root.left = left
                                root.right = right
                                ans.append(root)
                return ans
        res = dfs(n)
        print(len(res))
        return dfs(n)

sol = Solution()
n = 7
res = sol.allPossibleFBT(n)
print(res)



### dynamic programming a bottom up approach
from collections import defaultdict
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = defaultdict(list)
        dp[1].append(TreeNode())
        def copy(node):
            if node is None:
                return None
            else:
                new_node = TreeNode()
                new_node.left = copy(node.left)
                new_node.right = copy(node.right)
                return new_node

        for i in range(3,n+1):
            if i % 2 == 0:
                continue
            ans = []
            for left in range(1, i-1):
                right = i-1 - left
                for left_node in dp[left]:
                    for right_node in dp[right]:
                        root = TreeNode()
                        root.left = copy(left_node)
                        root.right = copy(right_node)
                        ans.append(root)
            dp[i] = ans
        return dp[n]


sol = Solution()
n = 7
res = sol.allPossibleFBT(n)
print(res)
      





