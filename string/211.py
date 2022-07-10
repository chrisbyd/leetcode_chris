

from cgitb import reset


class Node:
    def __init__(self, is_key = False) -> None:
        self.isKey = False
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
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
                if word == '.' and len(curNode.next) !=0:
                    res = False
                    for node in curNode.next.values():
                        res = res or node.isKey
                    return res
                elif word == '.' and len(curNode.next) ==0:
                    return False
                elif word in curNode.next and curNode.next[word].isKey:
                    return True
                else:
                    return False
            else:
                if word[0] == '.' and len(curNode.next) == 0:
                    return False
                elif word[0] == '.' and len(curNode.next) != 0:
                    res = False
                    for key in curNode.next.keys():
                        res = res or search_word(word[1:], curNode.next[key])
                    return res

                else:
                    if word[0] in curNode.next:
                        return search_word(word[1:], curNode.next[word[0]])
                    else:
                        return False
        return search_word(word, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

word = ["good", "goo", "hello", 'goose']
obj = WordDictionary()
obj.addWord(word[0])
obj.addWord(word[1])
obj.addWord(word[2])
obj.addWord(word[3])
res = obj.search('h..lo')
print(res)


# another probably more concise solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode() 
            curr = curr.children[char]
        curr.endOfWord = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.helper(0, self.root, word)

    def helper(self, j, root, word):
        curr = root
        for i in range(j, len(word)):
            char = word[i]
            if char == ".":
                for child in curr.children.values():
                    if self.helper(i+1, child, word):
                        return True
                return False
            else:
                if char not in curr.children:
                    return False
                curr = curr.children[char]
        return curr.endOfWord
