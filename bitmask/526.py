class Solution:
    def countArrangement(self, n: int) -> int:
        ans = [0]
        def dfs(mask, index):
            if mask == (1 << n) -1 :
                ans[0] += 1
                return
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    if (i+1) % index ==0 or index % (i+1) == 0:
                        dfs(mask | (1 << i), index + 1)
            return
        dfs(0, 1 )
        return ans[0] 

class Solution:
    def countArrangement(self, n: int) -> int:
        ans = [0]
        @lru_cache(None)
        def dfs(mask, index):
            if mask == (1 << n) -1 :
                return 1
            ans = 0
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    if (i+1) % index ==0 or index % (i+1) == 0:
                        ans += dfs(mask | (1 << i), index + 1)
            return ans 
       
        return dfs(0, 1 )