from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        charMap = defaultdict(int)
        for index, char in enumerate(s):
            if char not in charMap:
                charMap[char]  = [index, index]
            else:
                charMap[char][1] = index
        ans = 0
   
        for start, end in charMap.values():
            charset = set(s[start+1: end])
            ans += len(charset)
        return ans