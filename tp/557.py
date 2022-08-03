class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseWord(word):
            
            left, right = 0, len(word) -1
            while left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -=1
        words = s.split()
        ans = []
        for word in words:
            word = list(word)
            reverseWord(word)
            ans.append(" ")
            ans.append(''.join(word))
            
        return ''.join(ans[1:])
            
        