class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        minutes = -1
        fresh = 0

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        if fresh==0:
            return 0 

        while queue:
            minutes+=1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        queue.append((nr,nc))
                        fresh-=1

        return minutes if fresh==0 else -1
        
