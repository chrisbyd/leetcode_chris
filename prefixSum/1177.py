from collections import defaultdict
from typing import List
#####ok it is accepted but there is a better way
## lets work it out
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        count = [0] * (len(s) + 1)
        d = defaultdict(int)
        count[0] = d.copy()
        for idx, char in enumerate(s):
            d[char] += 1
            count[idx+1] = d.copy()
        ans = []
        for l, r, k in queries:
            ncount = count[r+1].copy()
            for key in count[l].keys():
                ncount[key] -= count[l][key]
            even = False
            
            if  (r - l + 1) % 2 == 0:
                even = True
            odd_count = 0
            for key in ncount.keys():
                n_occ = ncount[key]
                if n_occ % 2 != 0:
                    odd_count += 1
            if even:
                ans.append(odd_count <= 2* k)
            else:
                ans.append((odd_count - 1) <= 2* k)
        return ans
                
            
sol = Solution()
s = "abcda"
queries =[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
res = sol.canMakePaliQueries(s, queries)
print(res)


#####hello worlds
from collections import defaultdict
from typing import List
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def countDif(a, b):
            odd_count = 0
            for i in range(32):
                aa = (a >> i) & 1
                bb = (b>>i) & 1
                if aa != bb:
                    odd_count += 1
            return odd_count

        count = 0
        presum = [0]
        for idx, char in enumerate(s):
            count = count ^ (1 <<(ord(char) - ord('a')))
            presum.append(count)
        
        ans = []
        for l, r, k in queries:
            oc = countDif(presum[l], presum[r+1])
            if (r - l + 1)% 2 == 0:
                ans.append( oc <= 2* k)
            else:
                ans.append(oc - 1 <= 2* k)
        return ans
sol = Solution()
s = "abcda"
queries =[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
res = sol.canMakePaliQueries(s, queries)
print(res)