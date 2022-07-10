from typing import List

# Accepted !! Bravo !
#You are smart bro!
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        candidates = ['(', ')']
        dic = { ')': '('}
        ans = []
        def backtrack(count ,stack, c_string):
            if len(c_string) == 2*n:
                ans.append(c_string[:])
            for i in range(len(candidates)):
                if stack and dic.get(candidates[i]) == stack[-1]:
                    tem = stack.pop()
                    backtrack(count, stack, c_string + candidates[i])
                    stack.append(tem)
                elif candidates[i] == '(' and count < n:
                    count += 1
                    stack.append(candidates[i])
                    backtrack(count, stack, c_string + candidates[i])
                    stack.pop()
                    count -= 1
        backtrack(0, [], "")
        return ans

sol = Solution()
n = 1
res =  sol.generateParenthesis(n)
print(res)


