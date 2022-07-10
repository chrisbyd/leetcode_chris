from collections import defaultdict
from collections import Counter
### brutal force
class Solution:
    def getBeauty(self, s):
        dic = Counter(s)
        maxi = max(dic.values())
        mini = min(dic.values())
        return maxi- mini
    
    def beautySum(self, s: str) -> int:
        dic = defaultdict(int)
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans += self.getBeauty(s[i:j+1])
        return ans
                
        
        