class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n, m = len(matrix), len(matrix[0])
        i, j = 0,0

        RIGHT, DOWN, LEFT, UP = 0,1,2,3

        upwall = 0
        rightwall = m
        leftwall = -1
        downwall = n
        directions = RIGHT
        while len(ans) != m*n:

            if directions == RIGHT:
                while j<rightwall:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                rightwall -= 1
                directions = DOWN
            elif directions == DOWN:
                while i<downwall:
                    ans.append(matrix[i][j])
                    i += 1
                i,j = i-1, j-1
                directions = LEFT
                downwall -= 1
            elif directions == LEFT:
                while j>leftwall:
                    ans.append(matrix[i][j])
                    j -= 1
                i,j = i-1, j+1
                leftwall += 1
                directions = UP
            else:
                while i > upwall:
                    ans.append(matrix[i][j])
                    i -= 1
                i,j = i+1, j+1
                upwall += 1
                directions = RIGHT
        return ans
