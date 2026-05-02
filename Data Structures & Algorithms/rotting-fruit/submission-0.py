class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0
        rotten = deque()
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                
                elif grid[r][c] == 2:
                    rotten.append((r,c))
        
        dirt = [[0,1], [1,0], [0,-1], [-1,0]]

        while rotten and fresh > 0:
            for i in range(len(rotten)):
                r,c = rotten.popleft()

                for rr, rc in dirt:
                    nr, nc = r+rr, c+rc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten.append((nr,nc))

            count += 1
        return count if fresh == 0 else -1

# TC, SC = O(r*c)
            