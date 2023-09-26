class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEndOfWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
               

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            indx = ord(i) - ord('a')
            if not cur.children[indx]:
                cur.children[indx] = TrieNode()           
            cur = cur.children[indx]
        cur.isEndOfWord = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            indx = ord(i) - ord('a')
            if not cur.children[indx]:
                return False         
            cur = cur.children[indx]
        return cur.isEndOfWord
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            indx = ord(i) - ord('a')
            if not cur.children[indx]:
                return False         
            cur = cur.children[indx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)