class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num))
        for i in range(2, len(binary)):
            binary[i] = str(1 - int(binary[i]))
        ans = int(''.join(binary), 2)
        return ans
        
### with bit manipulation method
class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(len(bin(num)[2:])):
            num ^= 1<<i
        return num