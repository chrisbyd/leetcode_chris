from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increasing = True
        if len(arr) < 3:
            return False
        if arr[1] < arr[0]:
            return False
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            elif arr[i] < arr[i-1]:
                increasing = False
            if increasing and arr[i] < arr[i-1]:
                return False
            if not increasing and arr[i] > arr[i-1]:
                return False
        return not increasing 