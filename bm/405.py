class Solution:
    def toHex(self, num: int) -> str:
        sign = 1 if num >0 else -1
        if num == 0: return '0'
        num = 2** 31 - abs(num) if sign == -1 else num

        ans = ""
        d_to_c = {10: 'a', 11: 'b', 12: 'c', 13:'d', 14:'e', 15: 'f'}
        while num != 0:
            cur = num % 16
            if cur >= 10:
                cur = d_to_c[cur]
            ans = str(cur) + ans
            num = num // 16
        print(ans)
        if sign == -1:
            if len(ans) == 8:
                first = d_to_c[ 8 + int(ans[0])] if 8 + int(ans[0]) >= 10 else str(8 + int(ans[0]))
                ans = first + ans[1:]
            else:
                ans = '8' + (7 - len(ans)) * '0' + ans
          
                
        return ans
                
        
sol = Solution()
n = -1
res = sol.toHex(n)
print(res)
###a much clearer way
class Solution:
    def toHex(self, num: int) -> str:
        sign = 1 if num >0 else -1
        if num == 0: return '0'
        num = 2** 32 - abs(num) if sign == -1 else num

        ans = ""
        d_to_c = {10: 'a', 11: 'b', 12: 'c', 13:'d', 14:'e', 15: 'f'}
        while num != 0:
            cur = num % 16
            if cur >= 10:
                cur = d_to_c[cur]
            ans = str(cur) + ans
            num = num // 16

                
        return ans
                
        
            
        
        