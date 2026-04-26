class WordDictionary:

    def __init__(self):
        self.dic = {}

    def addWord(self, word: str) -> None:
        d = self.dic
        for  c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d ['.'] = '.'
        

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if len(word) == i:
                return '.' in node
            
            c = word[i]

            if c == '.':
                for key in node:
                    if key != '.' and dfs(node[key], i+1):
                        return True
                return False
            else:
                if c not in node:
                    return False
                return dfs(node[c], i+1)
            
        return dfs(self.dic, 0)