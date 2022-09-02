from typing import List

class Solution:
    def sort(self, nums: List) -> None:
        def recur(nums):
            if len(nums) == 1:
                return nums
            n = len(nums)
            left = recur(nums[:n // 2])
            right = recur(nums[n // 2:])
            l, r = 0, 0
            ans = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    ans.append(left[l])
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1
            if l != len(left):
                ans = ans + left[l:]
            if r != len(right):
                ans = ans + right[r:]
            return ans
        return recur(nums)

sol = Solution()
nums = [3,7,1,5,2,9,10]
res = sol.sort(nums)
print(res)

class Solution:
    def sort(self, nums: List):
        def mergeSort(i, j):
            if i == j:
                return
            middle = i + (j - i) // 2
            mergeSort(i, middle)
            mergeSort(middle + 1, j)
            l, r = i, middle + 1 
            ans = []
            while l <= middle and r <= j:
                if nums[l] <= nums[r]:
                    ans.append(nums[l])
                    l += 1
                else:
                    ans.append(nums[r])
                    r += 1
            if l <= middle:
                ans += nums[l: middle + 1]
            if r <= j:
                ans += nums[r: j+ 1]
            index = 0
            for c in range(i, j+1):
                nums[c] = ans[index]
                index += 1
        mergeSort(0, len(nums)-1)
    
sol = Solution()
nums = [3,7,1,3,5,2,9,10]
sol.sort(nums)
print(nums)