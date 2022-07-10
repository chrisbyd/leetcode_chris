from typing import List

# backtracking method
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        for k in digit_to_letters.keys():
            digit_to_letters[k] = list(digit_to_letters[k])
        ans = []
        if not digits:
            return ""
        def dfs(digit, cur):
            if len(cur) == len(digits):
                ans.append(cur[:])
            else:
                for letter in  digit_to_letters[int(digit[0])]:
                    dfs(digit[1:], cur + letter)
        dfs(digits ,"")
        return ans





sol = Solution() 
digits = ""
res = sol.letterCombinations(digits)
print(res)

# another implementation of backtracking

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        for k in digit_to_letters.keys():
            digit_to_letters[k] = list(digit_to_letters[k])
        ans = []
        if not digits:
            return ""
        def dfs(digit, cur):
            if len(cur) == len(digits):
                ans.append(cur[:])
            else:
                for letter in  digit_to_letters[int(digit[0])]:
                    dfs(digit[1:], cur + letter)
        dfs(digits ,"")
        return ans
