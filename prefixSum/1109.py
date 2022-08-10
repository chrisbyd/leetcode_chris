from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        psum = {0: - 1}
        cum = 0
        ans = 0
        for idx,  hour in enumerate(hours):
            cum += 1 if hour > 8 else - 1
            if cum > 0:
                ans = max(ans, idx +1)
            else:
                if cum - 1 in psum:
                    prev_idx = psum[cum-1]
                    ans = max(ans , idx - prev_idx)
                if cum not in psum:
                    psum[cum] = idx
        return ans
            
            