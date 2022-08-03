class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list(s)
        left, right = 0, len(s)-1 
        while left < right:
            if not s_list[left].isalpha() and not s_list[left].isnumeric():
                left += 1
            elif not s_list[right].isalpha() and not s_list[right].isnumeric():
                right -= 1
            else:
                if s_list[left].lower() != s_list[right].lower():
                    return False
                left += 1
                right -= 1
        return True
        