class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[float('inf')] * (len(word2)+1) for i in range(len(word1)+1)]

        for i in range(len(word2)+1):
            matrix[len(word1)][i] = len(word2) - i
        for j in range(len(word1)+1):
            matrix[j][len(word2)] = len(word1) - j

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    matrix[i][j] = matrix[i+1][j+1]
                else:
                    matrix[i][j] = 1 + min(matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])

        return matrix[0][0]
# TC = SC = O(m*n)
