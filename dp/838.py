


#adjacent symbols


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [ (i,x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        print(symbols)

        
       
        ans = []
        for (i,x), (j, y) in zip(symbols[:-1], symbols[1:]):

            if x == y:
                for index in range(i+1, j+1):
                    ans.append(x)
            elif x == 'L' and y == 'R':
                for index in range(i+1, j):
                    print('HI')
                    ans.append('.')
                ans.append('R')
            else:
                for index in range(i+1, j):
                    if j - index < index - i:
                        ans.append('L')
                    elif j - index > index - i:
                        ans.append('R')
                    else:
                        ans.append('.')
                ans.append('L')
           

        return ''.join(ans[:-1])

sol = Solution()
dominoes = ".L.R...LR..L.."
res = sol.pushDominoes(dominoes=dominoes)
print(res)
                    

# The above solution is too complicated! try to reorganized it!








        

        


