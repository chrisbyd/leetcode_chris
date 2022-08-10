### brutal force solution with TLE

from collections import Counter
import sys
## brutal force solution
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        htable = Counter(s)
        n, ans = len(s),  - sys.maxsize
        for i in range(n):
            for j in range(i, n):
                htable = Counter(s[i:j+1])
                valid = True
                for v in htable.values():
                    if v < k:
                        valid = False
                        break
                if valid:
                    ans = max(ans, j - i + 1) 
        return ans
           
                
### divide and conquer solution
from collections import Counter
import sys
## brutal force solution
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def divideRecur(start, end):
            countMap = Counter(s[start: end+1])
            for i in range(start, end+1):
                if countMap[s[i]] >= k:
                    continue
                else:
                    return max(divideRecur(start, i - 1), divideRecur(i+1, end))
            return end - start + 1
        return divideRecur(0, len(s)-1 )
                    
                
### SLIDING WINDOW solution
            
from collections import Counter
import sys
## brutal force solution
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxUnique, length = len(list(Counter(s).keys())), len(s)
        ans = 0
        print(maxUnique)
        for curUnique in range(1, maxUnique + 1):
            unique, start, end, count = 0, 0, 0, 0
            cmap = dict()
            while end < length:
                print('current unique',curUnique,"start",start, 'end' ,end,'this unique', unique)
                if unique <= curUnique:
                    print(cmap)
                    if s[end] not in cmap or cmap[s[end]] == 0:
                        unique += 1
                        cmap[s[end]] = 1
                    else:
                        print('hello')
                        cmap[s[end]] += 1

                    if cmap[s[end]] == k:
                        count += 1
                    end += 1
                else:
                    
                    if cmap[s[start]] == k:
                        count -= 1
                    cmap[s[start]] -= 1

                    if cmap[s[start]] == 0:
                        unique -= 1
                    start += 1
                if unique == curUnique and unique == count:
                    ans = max(ans, end - start)
                    print("this time", ans)
        return ans
s = "baaabcb"
k = 3
sol = Solution()
res = sol.longestSubstring(s, k)
print(res)      
                

        
    
                    
                
        
                
            
        