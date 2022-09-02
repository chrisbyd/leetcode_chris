from typing import List
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        nums1, nums2 = num1.split('+'),  num2.split('+')
        r1, r2, im1, im2 = int(nums1[0]), int(nums2[0]), int(nums1[1][:-1]), int(nums2[1][:-1])
        r = r1 * r2  - im1 * im2
        im = r1 * im2 + r2 * im1
        return str(r) + '+' + str(im) + 'i'
        