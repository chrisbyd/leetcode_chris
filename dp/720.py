from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key = len)
        print(words)
        words_set = set(words)
        dp = {"": True}
        for word in words:
            if word[:-1] in dp:
                dp[word] = dp[word[:-1]]
            else:
                dp[word] = False
        ans = []
        size = 0
        for i in range(len(words)-1, -1, -1):
            if dp[words[i]] and size == 0:
                size = len(words[i])
            if dp[words[i]] and len(words[i]) == size: 
                ans.append(words[i])

        return min(ans) if ans else ""

sol = Solution()
words = ["a","banana","app","appl","ap","apply","apple"]
words = ["t","ti","tig","tige","tiger","e","en","eng","engl","engli","englis","english","h","hi","his","hist","histo","histor","history"]
res = sol.longestWord(words)
print(res)
        
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False
    
    def addword(self, word):
        
        
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        pass


        





        