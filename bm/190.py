class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 0xFFFFFFFF
        a = bin((1<< 32) | n)[3:][::-1]
      
        return int(a,2)
        
        
   