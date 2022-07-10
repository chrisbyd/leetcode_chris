from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = []
        for i in range(1, len(nums)-1):
            res.append(self.maxProduct(nums[:i]))
            res.append(self.maxProduct(nums[i+1:]))
        res.append(self.maxProduct(nums[1:]))
        res.append(self.maxProduct(nums[:-1]))
        ap = 1
        for item in nums:
            ap *= item
        res.append(ap)
        return max(res)



class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = -999999
        currProd = 1
        n = len(nums)
        for i in range(n):
            currProd = currProd * nums[i]
            if currProd > maxProd:
                maxProd = currProd
            if nums[i] == 0:
                currProd = 1
        currProd = 1
        for i in range(n-1,-1,-1):
            currProd = currProd * nums[i]
            if currProd > maxProd:
                maxProd = currProd
            if nums[i] == 0:
                currProd = 1
        return maxProd



# double pointer
def maxProduct(self, nums: List[int]) -> int:
	ans = nums[0]
	l, r = 1, 1

	for i in range(len(nums)):
		j = -1-i

		l *= nums[i]
		r *= nums[j]
		ans = max(ans, l, r)

		if l == 0:
			l = 1
		if r == 0:
			r = 1

	return ans


nums = [2,0,-1,2,-1,2]
sol = Solution1()
res = sol.maxProduct(nums)
print(res)