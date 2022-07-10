from typing import List

class Node:
    def __init__(self, is_key = False) -> None:
        self.isKey = False
        self.next = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        thisNode = self.root
        while word:
            if word[0] not in thisNode.next:
                thisNode.next[word[0]] = Node()
                thisNode = thisNode.next[word[0]]
            else:
                thisNode = thisNode.next[word[0]]
            word = word[1:]
        thisNode.isKey = True
            
    def search(self, word: str) -> bool:
        def search_word(word, curNode):
            if len(word) == 1:
                if word in curNode.next and curNode.next[word].isKey:
                    return True
                else:
                    return False
            else:
                if word[0] in curNode.next:
                    return search_word(word[1:], curNode.next[word[0]])
                else:
                    return False
        return search_word(word, self.root)

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        while prefix:
            if prefix[0] in curNode.next:
                curNode = curNode.next[prefix[0]]
                prefix = prefix[1:]
            else:
                return False
        return True

        
        
    def all_startsWith(self, prefix: str) -> bool:
        ans = []
        curNode = self.root
        new_prefix = prefix
        while prefix:
            if prefix[0] in curNode.next:
                curNode = curNode.next[prefix[0]]
                prefix = prefix[1:]
            else:
                return ans

        def dfs(curNode, curWord):
            if curNode.isKey:
                ans.append(curWord)
            for key in curNode.next.keys():
                cnode = curNode.next[key]
                dfs(cnode, curWord + key)

        dfs(curNode, new_prefix)
        return ans




        
    

# Your Trie object will be instantiated and called as such:
word = ["good", "goo", "hello", 'goose']
obj = Trie()
obj.insert(word[0])
obj.insert(word[1])
obj.insert(word[2])
obj.insert(word[3])
param_2 = obj.search('goode')
res = obj.startsWith('goose')
print(param_2)
print(res)
#param_3 = obj.startsWith(prefix)