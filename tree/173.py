# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.v_list = self.dfs(root)
        self.cur = 0
        

    def next(self) -> int:
        if self.hasNext():
            ans = self.v_list[self.cur]
            self.cur += 1
            return ans
        return -1

    def hasNext(self) -> bool:
        if self.cur >= len(self.v_list):
            return False
        return True
    
    def dfs(self, node):
        if not node: return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()