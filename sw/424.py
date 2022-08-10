from typing import List
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        start = 0
        res = 0
        
        for end, c in enumerate(s):
            counter[c] += 1
            most_common_val = counter.most_common()[0][1]
            while end - start + 1 - most_common_val > k:
                counter[s[start]] -= 1
                start += 1
            res = max(end - start + 1, res)
        
        return res


s = "ABAA"
k = 0
sol = Solution()
res = sol.characterReplacement(s, k)
print(res)
                
from typing import List
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        start, ans = 0, 0
        for end, char in enumerate(s):
            count[char] += 1
            while end - start +1 - max(count.values()) > k:
                count[s[start]] -= 1 
                start += 1
            ans = max(ans, end - start + 1)
        return ans


## sliding window with two pointers