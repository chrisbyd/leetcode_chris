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

from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = set([start])
        step = 0
        q = deque([start])
        while q:
            length = len(q)
            for _ in range(length):
                this = q.popleft()
                if this == end:
                    return step
                for gene in 'ACGT':
                    for i in range(8):
                        multation = this[:i] + gene + this[i+1:]
                        if multation in bank and multation not in visited:
                            q.append(multation)
                            visited.add(multation)
            step += 1
        return -1
            
                            
                            