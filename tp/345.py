class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(char):
            if char in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U'}:
                return True
            return False
        vowels = []
        for char in s:
            if isVowel(char):
                vowels.append(char)
        vowels = vowels[::-1]
        index = 0
        list_string = list(s)
        for idx, char in enumerate(list_string):
            if isVowel(char):
                list_string[idx] = vowels[index]
                index += 1
        return ''.join(list_string)
            

#using two pointer
class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) -1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        while left < right:
            if s[left].lower() in vowels:
                if s[right].lower() in vowels:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return ''.join(s)
