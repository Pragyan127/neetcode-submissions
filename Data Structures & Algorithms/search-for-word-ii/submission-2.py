class Solution:
    def __init__(self):
        self.dic = {}
    
    def addword(self, word):
        d = self.dic
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = word
        return d


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        for n in words:
            self.addword(n)
        res = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, node):

            if r<0 or r>=rows or c <0 or c>=cols:
                return
            
            ch = board[r][c]
            if ch not in node:
                return
            
            node = node[ch]

            if '.' in node:
                res.add(node['.'])
            
            board[r][c] = '#'

            dfs(r+1,c,node)
            dfs(r,c+1,node)
            dfs(r-1,c,node)
            dfs(r,c-1,node)

            board[r][c] = ch

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,self.dic)
        
        return list(res)
        
