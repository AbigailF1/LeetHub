class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0 
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map ={}
        

    def insert(self, key: str, val: int) -> None:
        new_val = val
        if key in self.map:     
            new_val = val - self.map[key]

        self.map[key] = val
        
        cur = self.root
        for i in key:
            if i not in cur.children:
                cur.children[i] = TrieNode()           
            cur = cur.children[i]
            cur.prefix_count += new_val
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        return cur.prefix_count 
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)