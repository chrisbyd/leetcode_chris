from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed = set(allowed)
        for string in words:
            consis = True
            for character in string:
                if character not in allowed:
                    consis = False
                    break
            if consis:
                ans += 1
        return ans
sol = Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
res = sol.countConsistentStrings(allowed, words)
print(res)