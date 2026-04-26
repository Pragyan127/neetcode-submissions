class PrefixTree:

    def __init__(self):
        self.dic = {}
    def insert(self, word: str) -> None:
        d = self.dic
        for i in word:
            if i not in d:
                d[i] = {}
            d = d[i]
        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.dic 
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return '.' in d
        
    def startsWith(self, prefix: str) -> bool:
        d = self.dic 
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True

        
        