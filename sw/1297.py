from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = defaultdict(int)
        l, r, ans, n  = 0, 0, 0, len(s)
        unique = 0
        occur = defaultdict(int)
        while r <  n:
            if counter[s[r]] == 0:
                unique += 1
            counter[s[r]] += 1
            if r - l + 1 == minSize:
                if unique  <= maxLetters:
                     occur[s[l: r+1]] += 1
                
                if counter[s[l]] == 1:
                    unique -= 1
                counter[s[l]] -= 1
                l += 1
            r += 1
        return max(occur.values()) if occur else 0 
                
            
            
        
        
            
        
sol = Solution()
s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
res  = sol.maxFreq(s, maxLetters, minSize, maxSize)
print(res)