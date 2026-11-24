class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        minutes = 0
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==2:
                    queue.append((r,c))

                if grid[r][c]==1:
                    fresh+=1

        while queue and fresh>0:

            size = len(queue)
            
            for _ in range(size):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1):
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh-=1

            minutes+=1

        if fresh>0:
            return -1

        return minutes
