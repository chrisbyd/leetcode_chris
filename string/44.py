from typing import List

# recursion
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(text, pattern):
            if not pattern:
                return not text
            first_match = (bool(text) and pattern[0] in [text[0], '?', '*'] ) 
            if first_match and p[0] == '*':
                return self.isMatch(text[1:], pattern) or self.isMatch(text[1:], pattern[1:]) or self.isMatch(text, pattern[1:])
            elif first_match and p[0] in [s[0], '?']:
                return self.isMatch(text[1:], pattern[1:])
            elif not first_match and (not bool(text) and pattern[0] == '*'):
                return self.isMatch(text, pattern[1:])
            else:
                return False
        return dfs(s, p)

# dynamic programming:`12`
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        memo= {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                    memo[i,j] = ans
                    return ans
                else:
                    first_match = i < len(s) and p[j] in [s[i], '?'] 

                    if j + 1 < len(p) and p[j] == '*' and i < len(s) - 1:
                        ans = dp(i+1, j) or  dp(i, j+ 1) or dp(i+1, j+1)

                    elif j + 1 < len(p) and p[j] == '*' and i == len(s) -1:
                        ans =  dp(i, j+ 1)
                    elif j + 1 == len(p) and p[j] == "*" and i < len(s) - 1:
                        ans = dp(i +1, j)
                    elif j + 1 == len(p) and p[j] == '*' and i == len(s) -1:
                        ans = dp(i+1, j+1)
                    elif p[j] == '*':
                        ans = dp(i, j+1)
                    else:
                        ans = first_match and dp(i+1, j+1)
                    memo[i,j] = ans
                    return ans

            else:
                return memo[i,j]
        
        return dp(0, 0)




sol = Solution1()
s = ""
p ="*?*"
res = sol.isMatch(s, p)
print(res)







        