# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = nestedList
        self.flatten_list = []
        self.flatten()
        self.n = len(self.flatten_list)
        self.current = 0
        
    def flatten(self):
        def dfs(current):
            if current.isInteger():
                self.flatten_list.append(current.getInteger())
            else:
                for nei in current.getList():
                    dfs(nei)
        for nei in self.list:
            dfs(nei)
    
            
        
    def next(self) -> int:
        if self.current <= self.n - 1:
            ans = self.flatten_list[self.current]
            self.current += 1
            return ans
        else:
            return False
        