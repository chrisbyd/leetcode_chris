from typing import List


# standard backtrack with TLE error
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def backtrack(s):
            if not s:
                return True
            else:
                ans = False
                for i in range(len(s)):
                    if s[:i+1] in wordDict:
                       ans = ans or backtrack(s[i+1:])
                return ans
        return backtrack(s)

# sol = Solution()
# s = "leetcodea"
# wordDict = ["leet","code"]
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# res = sol.wordBreak(s, wordDict)
# print(res)


# backtracking with memory for saving repeated computation       
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def backtrack(s):
            if len(s) not in memo:
                if not s:
                    memo[len(s)] = True
                    return True
                else:
                    ans = False
                    for i in range(len(s)):
                        if s[:i+1] in wordDict:
                            ans = ans or backtrack(s[i+1:])
                    memo[len(s)] = ans
                    return ans 
            return memo[len(s)]
        return backtrack(s)

sol = Solution1()
s = "leetcodea"
wordDict = ["leet","code"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
res = sol.wordBreak(s, wordDict)
print(res)
