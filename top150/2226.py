from typing import List
### binary search
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k: return 0
        ans = 0
        maximum = max(candies)
        def validate(number):
            res = 0
            for num in candies:
                res += num // number
            return res >= k
        
        left, right = 1, maximum
        while left <= right:
            middle = (left + right) // 2
            if validate(middle):
                left = middle + 1
                ans = middle
            else:
                right = middle - 1
        return ans
        

from collections import defaultdict
class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.dict = defaultdict(int)
        self.count1 = 0
        self.flipv = 0

    def fix(self, idx: int) -> None:
        if not self.flipv:
            if self.dict[idx] == 0 :
                self.count1 += 1
            self.dict[idx] = 1
        else:
            if self.dict[idx] == 1:
                self.count1 += 1
            self.dict[idx]  = 0 
        
    def unfix(self, idx: int) -> None:
        if not self.flipv:
            if self.dict[idx] == 1:
                self.count1 -= 1
            self.dict[idx] = 0
        else:
            if self.dict[idx] == 0:
                self.count1 -= 1
            self.dict[idx] = 1

    def flip(self) -> None:
        self.count1 = self.size - self.count1
        self.flipv = 1 - self.flipv
        

    def all(self) -> bool:
        return self.count1 == self.size
        

    def one(self) -> bool:
        return self.count1 >= 1
        

    def count(self) -> int:
        return self.count1

    def toString(self) -> str:
        if not self.flipv:
            ans = ['0'] * self.size
            for idx in self.dict.keys():
                if self.dict[idx] ==1:
                    ans[idx] = '1'
        else:
            ans = ['1'] * self.size
            for idx in self.dict.keys():
                if self.dict[idx] ==1:
                    ans[idx] = '0'
        return "".join(ans)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()