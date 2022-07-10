import heapq
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1: 0}
        def dp(number):
            if number not  in cache:
                if number == 1:
                    return 0
                elif number % 2 == 0:
                    ans = 1 + dp(number // 2)
                    
                else:
                    ans = 1 + dp(number * 3 + 1)
                cache[number] = ans
                return ans
            else:
                return cache[number]
        heap = []
        for i in range(lo, hi+1):
            print(dp(i))
            heapq.heappush(heap, (dp(i),i))
        for _ in range(k):
            _,ans = heapq.heappop(heap)
        return ans
            
sol = Solution()
lo = 12
hi = 15
k = 2
res = sol.getKth(lo, hi, k)
print(res)