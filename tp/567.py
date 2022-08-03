###although it passes, it is still too complicated in terms of time complexity
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if len(s2) < length:
            return False
        left, right = 0, length - 1
        s1 = sorted(list(s1))
        s2 = list(s2)
        while right < len(s2):
            if sorted(s2[left: right + 1]) == s1:
                return True
            left += 1
            right += 1
        return False

        
sol = Solution()
s1 = 'adc'
s2 = 'dcda'
res = sol.checkInclusion(s1,s2)
print(res)