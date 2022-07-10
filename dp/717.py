from typing import  List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits == [0, 0]  or bits == [0] :
            return True
        elif bits == [1, 0]  or bits == [1, 1] :
            return False
        else:
            if bits[0] == 1:
                return self.isOneBitCharacter(bits[2:])
            else:
                return self.isOneBitCharacter(bits[1:])
        