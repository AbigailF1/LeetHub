class MagicDictionary:

    def __init__(self):
        self._list = []

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self._list.append(word)        

    def search(self, searchWord: str) -> bool:
        for i in range(len(self._list)):
            count = 0
            if len(self._list[i])!= len(searchWord):
               count = 0
            else:
                for j in range(min(len(self._list[i]), len(searchWord))):
                    
                    if self._list[i][j] != searchWord[j]:     
                        count += 1
                if count == 1:
                    return True

        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)