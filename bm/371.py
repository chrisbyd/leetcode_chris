class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry  = 0
        ans = ''
        while a or b:
           
            bit_1 = a & 1
            bit_2 = b & 1
          
            if bit_1 and bit_2:
                if carry:
                    this_bit = 1
                    carry = 1
                else:
                    this_bit = 0
                    carry = 1
            elif not bit_1 and not bit_2:
                this_bit = 1 if carry else 0
                carry = 0
            else:
                this_bit = 0 if carry else 1
            a = a >> 1
            b = b >> 1
            ans = str(this_bit) + ans
        ans = str(carry) + ans if carry else ans
        ans = '0b' + ans
        return int(ans,2)
                    
            
        
sol = Solution()
a, b = 100,  -1
res = sol.getSum(a, b)
print(res)


## with bit manipulation
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask  = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        while b != 0:
            a, b = (a ^ b) & mask, ((a &b ) << 1)& mask
        return a if a <= MAX else ~(a ^ mask)
        
            
            
        