class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['.'] = word

        results = set()

        def dfs(r, c, node):
            # 1. boundary check
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            # 2. character check
            ch = board[r][c]
            if ch not in node:
                return

            # move in trie
            node = node[ch]

            # 3. word found check
            if '.' in node:
                results.add(node['.'])
                

            # 4. backtracking
            board[r][c] = '#'

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = ch

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie)

        return list(results)