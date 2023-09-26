class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()           
            cur = cur.children[i]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        stack = [(cur, 0)]
        while stack:
            curr, indx = stack.pop()
            if indx == len(word):
                if curr.isEndOfWord:
                    return True
            elif word[indx] == ".":
                for x in curr.children.values():
                    stack.append((x, indx+1))
            elif word[indx] in curr.children:
                stack.append((curr.children[word[indx]], indx+1))

        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)