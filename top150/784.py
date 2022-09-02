from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        dp = [[""]] * (len(s) +1)
        for idx, char in enumerate(s):
            if ord(char) >= ord('0') and ord(char) <= ord('9'):
                dp[idx + 1] = [string + char for string in dp[idx]]
            else:
                if char.isupper():
                    char = char.lower()
                dp[idx + 1] =  [string + char for string in dp[idx]] +[string + char.upper() for string in dp[idx]]
        return dp[-1]
        