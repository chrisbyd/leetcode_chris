class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        left = s_list
        ans = []
        
        def reverse(num):
            left = 0
            right = min(len(num) -1, k-1)
            while left < right:
                num[left], num[right] = num[right], num[left]
                left += 1
                right -= 1
        ans = ""
        while left:
            cur = left[:2*k]
            reverse(cur)
            ans += ''.join(cur)
            left = left[2*k:]
        return ans
            
            