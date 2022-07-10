from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0
            elif not node.left and not node.right: return 1 
            elif node.left and node.right:
                return min(dfs(node.left), dfs(node.right)) + 1
            elif node.left and not node.right:
                return dfs(node.left) + 1
            else:
                return dfs(node.right) + 1
                
        return dfs(root)
        

#### another solution thats somewhat better
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      
      
      
        def HeightBalance(root):
          
          if root:
            h_l,h_r = HeightBalance(root.left),HeightBalance(root.right)
            if h_l!=-1 and h_r!=-1 and abs(h_l-h_r)<=1:
              return 1+max(h_l,h_r)
            return -1
          else:
            return 0
          
          
          
        return HeightBalance(root)!=-1