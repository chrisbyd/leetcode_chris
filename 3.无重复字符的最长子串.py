#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        i, j = 0, 0

        while j < len(s):
            res = s[i:j]
            if not s[j] in res:
                j += 1
                new_res = s[i: j]
                lenghth = len(new_res)
                if lenghth > max_length:
                    max_length = lenghth
            else:
                i += 1
        
        return max_length





        
# @lc code=end

