class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:  return False
        b_number =  1<< 32
        b_list = list(bin(n | b_number)[3:])
        b_list = [int(i) for i in b_list]
        if sum(b_list) == 1:
            return True
        return False
        