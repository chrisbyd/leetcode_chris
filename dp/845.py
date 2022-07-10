from typing import List


# a typical two pointer problem
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = start  = 0

        while start < n:
            end = start
            if end + 1 < n  and arr[end] < arr[end + 1]:
                # set end to the peak of this potential mountain
                while end + 1 < n and arr[end] < arr[end + 1]:
                    end += 1
                
                if end + 1 <n and arr[end] > arr[end +1]:
                    while  end + 1 < n and arr[end+1] < arr[end]:
                        end += 1
                    ans = max(ans, end - start +1)
            start = max(end, start +1)
        return ans

sol  = Solution()
arr = [2,1,4,7,3,2,5]
res = sol.longestMountain(arr)
print(res)










  




    