class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, ans, cum  = 0, 0, 0
        for r in range(len(s)):
            dif = abs (ord(s[r]) - ord(t[r])) 
            cum += dif
            while cum > maxCost:
                cum -=  abs (ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans , r - left + 1)
        return ans
            