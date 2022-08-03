class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        counter = 0
        anchor = 2
        for i in range(2, n+1):
            counter += 1
            if counter > anchor:
                anchor = 2 * anchor
                counter = 1
            dp[i] = 1 + dp[i - anchor]
        return dp
            
            
            
        