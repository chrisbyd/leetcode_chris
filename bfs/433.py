from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        hset = set(bank)
        if end not in hset:
            return -1
        length = len(start)
        ans = 0
        for idx, val in enumerate(start):
            if start[idx] != end[idx]:
                ans += 1
        return ans
        
        
        



s = "AACCTTGG"
e = "AATTCCGG"
bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
sol = Solution()
res = sol.minMutation(s, e, bank= bank)
print(res)